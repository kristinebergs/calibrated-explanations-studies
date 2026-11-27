from __future__ import annotations
import math
import time
from dataclasses import dataclass
from typing import Any, Iterable, Literal
import numpy as np
import pandas as pd
# ==============================================================

@dataclass(frozen=True)
class EnsureRunConfig:
    test_size: int = 100
    calibration_sizes: tuple[int, ...] = (100, 300, 500)
    random_state: int = 42

    # Conjunction controls
    n_top_features: int = 5
    max_rule_size: int = 2

    # Ranking analysis weights (paper)
    ranking_weights: tuple[float, ...] = (-1.0, -0.5, 0.0, 0.5, 1.0)

    # Plain regression normalization for ensured scoring
    normalize_plain_regression: bool = True

    # Regression interval percentiles for plain regression
    low_high_percentiles: tuple[int, int] = (5, 95)


def selection_score(prediction: np.ndarray, uncertainty: np.ndarray, w: float) -> np.ndarray:
    """Article score: (1-|w|)(1-U)+|w|D_w, D_w=P or 1-P.

    Inputs are already on the intended ranking scale. Plain regression uses
    within-set min-max coordinates; classification coordinates are probabilities.
    """
    if not -1.0 <= w <= 1.0:
        raise ValueError("w must be in [-1, 1]")
    p = np.asarray(prediction, dtype=float)
    u = np.asarray(uncertainty, dtype=float)
    direction = p if w >= 0 else 1.0 - p
    return (1.0 - abs(w)) * (1.0 - u) + abs(w) * direction


POLICY_DISAGREEMENT_PAIRS: dict[str, tuple[float, float]] = {
    # Required rows for the policy-disagreement table.
    # U-only is w=0. C-only is the confidence-increasing boundary w=1.
    "u_only_vs_c_only": (0.0, 1.0),
    "w05_vs_w0": (0.5, 0.0),
    "w05_vs_w1": (0.5, 1.0),
    "wm05_vs_w05": (-0.5, 0.5),
}


def _clean_float(value: Any) -> float | None:
    if value is None:
        return None
    try:
        out = float(value)
    except (TypeError, ValueError):
        return None
    if math.isnan(out):
        return None
    return out


def _min_max_scale(values: np.ndarray) -> np.ndarray:
    """Apply a simple min-max normalization to a 1D array."""
    values = np.asarray(values, dtype=float)
    if values.size == 0:
        return values

    finite_mask = np.isfinite(values)
    if not np.any(finite_mask):
        return np.full(values.shape, np.nan, dtype=float)

    finite_values = values[finite_mask]
    min_value = float(np.min(finite_values))
    max_value = float(np.max(finite_values))
    if np.isclose(max_value, min_value):
        scaled = np.zeros(values.shape, dtype=float)
        scaled[finite_mask] = 0.0
        return scaled

    scaled = np.full(values.shape, np.nan, dtype=float)
    scaled[finite_mask] = (finite_values - min_value) / (max_value - min_value)
    return np.clip(scaled, 0.0, 1.0)


def _normalize_rank_inputs(
    prediction: np.ndarray,
    uncertainty: np.ndarray,
    *,
    normalize: bool,
) -> tuple[np.ndarray, np.ndarray]:
    """Normalize ranking inputs once so the score and disagreement logic use the same scale."""
    prediction = np.asarray(prediction, dtype=float)
    uncertainty = np.asarray(uncertainty, dtype=float)

    if not normalize:
        return prediction, uncertainty

    return _min_max_scale(prediction), _min_max_scale(uncertainty)


def _argmax_index(
    score: np.ndarray,
    indexes: Iterable[int] | None = None,
) -> int | None:
    """Return the original candidate index of the maximum finite score."""
    score = np.asarray(score, dtype=float)
    if score.size == 0:
        return None

    if indexes is None:
        idx = np.arange(score.size, dtype=int)
    else:
        idx = np.asarray(list(indexes), dtype=int)
        if idx.size == 0:
            return None

    vals = score[idx]
    valid = ~np.isnan(vals)
    if not np.any(valid):
        return None

    idx = idx[valid]
    vals = vals[valid]
    return int(idx[int(np.argmax(vals))])


def _selection_change_record(
    prediction: np.ndarray,
    uncertainty: np.ndarray,
    left_idx: int | None,
    right_idx: int | None,
) -> dict[str, float | int | None]:
    """Compare two selected candidates for the same instance.

    Delta values are absolute and are only populated when the selected
    candidate changes. This makes the exported medians conditional on
    actual policy disagreement rather than diluted by zero-change cases.
    """
    if left_idx is None or right_idx is None:
        return {
            "valid": 0,
            "changed": None,
            "delta_prediction": None,
            "delta_uncertainty": None,
        }

    changed = int(left_idx != right_idx)
    if not changed:
        return {
            "valid": 1,
            "changed": 0.0,
            "delta_prediction": None,
            "delta_uncertainty": None,
        }

    return {
        "valid": 1,
        "changed": 1.0,
        "delta_prediction": abs(float(prediction[left_idx]) - float(prediction[right_idx])),
        "delta_uncertainty": abs(float(uncertainty[left_idx]) - float(uncertainty[right_idx])),
    }


def _selection_outcome_change_record(
    prediction: np.ndarray,
    uncertainty: np.ndarray,
    left_idx: int | None,
    right_idx: int | None,
    *,
    atol: float = 1e-12,
) -> dict[str, float | int | None]:
    """Compare two selected candidates by their realized outcome."""
    if left_idx is None or right_idx is None:
        return {
            "valid": 0,
            "changed": None,
            "delta_prediction": None,
            "delta_uncertainty": None,
        }

    delta_prediction = abs(float(prediction[left_idx]) - float(prediction[right_idx]))
    delta_uncertainty = abs(float(uncertainty[left_idx]) - float(uncertainty[right_idx]))
    changed = int(delta_prediction > atol or delta_uncertainty > atol)

    if not changed:
        return {
            "valid": 1,
            "changed": 0.0,
            "delta_prediction": None,
            "delta_uncertainty": None,
        }

    return {
        "valid": 1,
        "changed": 1.0,
        "delta_prediction": delta_prediction,
        "delta_uncertainty": delta_uncertainty,
    }


def _summarize_change_records(
    records: list[dict[str, Any]],
) -> dict[str, float | int]:
    """Aggregate same-instance selection-change records."""
    valid_records = [r for r in records if r and int(r.get("valid", 0)) == 1]
    if not valid_records:
        return {
            "n_valid": 0,
            "n_changed": 0,
            "disagreement_pct": float("nan"),
            "median_abs_delta_prediction": float("nan"),
            "median_abs_delta_uncertainty": float("nan"),
        }

    changed = []
    delta_p = []
    delta_u = []

    for record in valid_records:
        changed_value = _clean_float(record.get("changed"))
        if changed_value is not None:
            changed.append(float(changed_value))

        delta_prediction = _clean_float(record.get("delta_prediction"))
        if delta_prediction is not None:
            delta_p.append(float(delta_prediction))

        delta_uncertainty = _clean_float(record.get("delta_uncertainty"))
        if delta_uncertainty is not None:
            delta_u.append(float(delta_uncertainty))

    return {
        "n_valid": int(len(valid_records)),
        "n_changed": int(np.sum(changed)) if changed else 0,
        # Stored as a share in [0, 1]. The exporter converts to percent.
        "disagreement_pct": float(np.mean(changed)) if changed else float("nan"),
        # Conditional medians among changed selections.
        "median_abs_delta_prediction": float(np.median(delta_p)) if delta_p else float("nan"),
        "median_abs_delta_uncertainty": float(np.median(delta_u)) if delta_u else float("nan"),
    }


def _safe_test_size(n_samples: int, requested: int) -> int:
    if n_samples <= 3:
        return 1
    # Keep at least 2 samples for training+calibration pool.
    max_allowed = max(1, n_samples - 2)
    if requested <= 0:
        return 1
    if requested <= max_allowed:
        return requested
    # Fall back to 20% when dataset is small.
    return max(1, n_samples // 5)


def _safe_calibration_pool_size(n_train: int, requested_max: int, *, min_remaining: int = 2) -> int:
    """Choose a calibration-pool size that leaves enough samples for training.

    Parameters
    ----------
    n_train:
        Number of samples available before splitting into proper-train and
        calibration-pool.
    requested_max:
        Upper bound (e.g., max calibration size).
    min_remaining:
        Minimum number of samples that must remain in the proper-training
        split.
    """

    min_remaining = max(1, int(min_remaining))
    max_allowed = max(1, n_train - min_remaining)
    return min(int(requested_max), int(max_allowed))


def subsample_calibration(
    x_cal_pool: np.ndarray,
    y_cal_pool: np.ndarray,
    cal_size: int,
    *,
    random_state: int,
) -> tuple[np.ndarray, np.ndarray]:
    if cal_size >= len(x_cal_pool):
        return x_cal_pool, y_cal_pool

    # Attempt a stratified calibration subsample to preserve class coverage
    try:
        from sklearn.model_selection import train_test_split

        # Only stratify when y_cal_pool is 1D and has more than one unique value
        if y_cal_pool.ndim == 1 and len(np.unique(y_cal_pool)) > 1:
            # train_test_split here returns the 'calibration' subset of the
            # requested size using `test_size=cal_size` semantics on the pool.
            _, x_cal, _, y_cal = train_test_split(
                x_cal_pool,
                y_cal_pool,
                test_size=cal_size,
                random_state=random_state,
                stratify=y_cal_pool,
            )
            return x_cal, y_cal
    except Exception:
        # Fallback to randomized sampling below
        pass

    rng = np.random.RandomState(random_state)
    idx = rng.choice(len(x_cal_pool), size=cal_size, replace=False)
    return x_cal_pool[idx], y_cal_pool[idx]


def compute_thresholds_from_non_test_targets(
    y_non_test: np.ndarray, percentiles: Iterable[int]
) -> dict[str, float]:
    """Compute threshold values from non-test targets (avoids test leakage)."""

    thresholds: dict[str, float] = {}
    for p in percentiles:
        thresholds[f"p{p}"] = float(np.percentile(y_non_test, p))
    return thresholds


def _rules_frame(explanation: Any) -> pd.DataFrame:
    """Return a normalized DataFrame of alternative rules.

    Uses public `get_rules()` representation.
    """

    rules = explanation.get_rules()
    if not rules or len(rules.get("rule", [])) == 0:
        return pd.DataFrame(
            columns=[
                "rule",
                "predict",
                "predict_low",
                "predict_high",
            ]
        )
    return pd.DataFrame(
        {
            "rule": list(rules["rule"]),
            "predict": np.asarray(rules["predict"], dtype=float),
            "predict_low": np.asarray(rules["predict_low"], dtype=float),
            "predict_high": np.asarray(rules["predict_high"], dtype=float),
        }
    )


def ablation_counts(explanation: Any) -> dict[str, int]:
    """Compute per-instance counts used in the paper tables.

    Delegates entirely to the public filter API on the explanation object so
    counts are always consistent with what the API surfaces to callers.
    """
    total = len(explanation)
    if total == 0:
        return {
            "total": 0,
            "ensured": 0,
            "counterfactual": 0,
            "counterpotential": 0,
            "semifactual": 0,
            "semipotential": 0,
            "superfactual": 0,
            "superpotential": 0,
            "pareto": 0,
        }

    super_with = len(explanation.super(include_potential=True))
    super_without = len(explanation.super(include_potential=False))

    semi_with = len(explanation.semi(include_potential=True))
    semi_without = len(explanation.semi(include_potential=False))

    counter_with = len(explanation.counter(include_potential=True))
    counter_without = len(explanation.counter(include_potential=False))

    ensured_with = len(explanation.ensured(include_potential=True))

    pareto_with = len(explanation.pareto(include_potential=True))

    return {
        "total": total,
        "ensured": ensured_with,
        "counterfactual": counter_without,
        "counterpotential": counter_with - counter_without,
        "semifactual": semi_without,
        "semipotential": semi_with - semi_without,
        "superfactual": super_without,
        "superpotential": super_with - super_without,
        "pareto": pareto_with,
    }


def _spearman(a: np.ndarray, b: np.ndarray) -> float:
    if len(a) < 2 or len(b) < 2:
        return float("nan")
    # pandas handles ties/ranking correctly.
    return float(pd.Series(a).corr(pd.Series(b), method="spearman"))


def ranking_validation_for_instance(
    explanation: Any,
    *,
    weights: Iterable[float],
    normalize: bool,
) -> dict[str, Any]:
    """Compute ranking validation and policy-disagreement stats for one instance."""
    df = _rules_frame(explanation)
    if df.empty:
        return {
            "n_rules": 0,
            "per_w": {},
            "policy_disagreement": {},
            "pareto_first": {},
        }

    prediction = np.asarray(df["predict"], dtype=float)
    predict_low = np.asarray(df["predict_low"], dtype=float)
    predict_high = np.asarray(df["predict_high"], dtype=float)
    uncertainty = predict_high - predict_low
    prediction, uncertainty = _normalize_rank_inputs(
        prediction,
        uncertainty,
        normalize=normalize,
    )

    per_w: dict[str, Any] = {}
    selections: dict[str, dict[str, int | None]] = {}

    for w in weights:
        w_float = float(w)
        w_key = str(w_float)

        score = selection_score(prediction, uncertainty, w_float)
        score = np.asarray(score, dtype=float)

        if score.size == 0 or np.all(np.isnan(score)):
            continue

        pareto_indexes = _policy_pareto_indexes(
            prediction,
            predict_low,
            predict_high,
            w_float,
            normalize=normalize,
        )
        pareto_set = set(pareto_indexes)

        top_idx = _argmax_index(score)
        top_pareto_idx = _argmax_index(score, pareto_indexes)

        top_is_pareto = (
            float(top_idx in pareto_set)
            if top_idx is not None
            else float("nan")
        )

        pareto_first_record = _selection_outcome_change_record(
            prediction,
            uncertainty,
            top_idx,
            top_pareto_idx,
        )

        per_w[w_key] = {
            "spearman_score_uncertainty": _spearman(score, uncertainty),
            "spearman_score_prediction": _spearman(score, prediction),
            "top_is_pareto": top_is_pareto,
            "pareto_first_changes": pareto_first_record["changed"],
            "top_index": top_idx,
            "top_pareto_index": top_pareto_idx,
        }

        selections[w_key] = {
            "top_index": top_idx,
            "top_pareto_index": top_pareto_idx,
        }

    policy_disagreement: dict[str, Any] = {}
    for name, (left_w, right_w) in POLICY_DISAGREEMENT_PAIRS.items():
        left = selections.get(str(float(left_w)), {}).get("top_index")
        right = selections.get(str(float(right_w)), {}).get("top_index")
        policy_disagreement[name] = _selection_change_record(
            prediction,
            uncertainty,
            left,
            right,
        )

    pareto_first: dict[str, Any] = {}
    for w in weights:
        w_key = str(float(w))
        left = selections.get(w_key, {}).get("top_index")
        right = selections.get(w_key, {}).get("top_pareto_index")
        pareto_first[w_key] = _selection_outcome_change_record(
            prediction,
            uncertainty,
            left,
            right,
        )

    return {
        "n_rules": int(len(df)),
        "per_w": per_w,
        "policy_disagreement": policy_disagreement,
        "pareto_first": pareto_first,
    }


def summarize_ranking_validation(
    per_instance: list[dict[str, Any]],
    *,
    weights: Iterable[float],
) -> dict[str, Any]:
    """Aggregate per-instance validation into dataset-level summary."""
    per_w_summary: dict[str, Any] = {}

    for w in weights:
        w_key = str(float(w))
        rows = [d.get("per_w", {}).get(w_key) for d in per_instance]
        rows = [r for r in rows if r is not None]

        if not rows:
            continue

        def _mean(field: str) -> float:
            vals = [r.get(field) for r in rows]
            vals = [
                v for v in vals
                if v is not None and not (isinstance(v, float) and math.isnan(v))
            ]
            return float(np.mean(vals)) if vals else float("nan")

        per_w_summary[w_key] = {
            "spearman_score_uncertainty": _mean("spearman_score_uncertainty"),
            "spearman_score_prediction": _mean("spearman_score_prediction"),
            "pareto_consistency_pct": _mean("top_is_pareto"),
            "pareto_first_change_pct": _mean("pareto_first_changes"),
        }

    policy_disagreement_summary: dict[str, Any] = {}
    for name in POLICY_DISAGREEMENT_PAIRS:
        records = [
            d.get("policy_disagreement", {}).get(name)
            for d in per_instance
        ]
        policy_disagreement_summary[name] = _summarize_change_records(
            [r for r in records if r is not None]
        )

    pareto_first_summary: dict[str, Any] = {}
    for w in weights:
        w_key = str(float(w))
        records = [
            d.get("pareto_first", {}).get(w_key)
            for d in per_instance
        ]
        pareto_first_summary[w_key] = _summarize_change_records(
            [r for r in records if r is not None]
        )

    return {
        "per_w": per_w_summary,
        "policy_disagreement": policy_disagreement_summary,
        "pareto_first": pareto_first_summary,
    }


def _policy_pareto_indexes(
    pred: np.ndarray,
    low: np.ndarray,
    high: np.ndarray,
    w: float,
    *,
    atol: float = 1e-12,
    normalize: bool = False,
) -> list[int]:
    """Return policy-oriented Pareto-frontier indexes for the supplied weight.

    The frontier is computed on the same normalized ranking space used by the
    ENSURED score so the manuscript's ranking rule and disagreement table are
    consistent.
    """

    outputs = np.asarray(pred, dtype=float)
    predict_low = np.asarray(low, dtype=float)
    predict_high = np.asarray(high, dtype=float)

    uncertainty = predict_high - predict_low
    outputs, uncertainty = _normalize_rank_inputs(
        outputs,
        uncertainty,
        normalize=normalize,
    )

    rule_count = int(len(outputs))
    if rule_count <= 1:
        return list(range(rule_count))

    w_float = float(w)
    if w_float == 0.0:
        return list(range(rule_count))

    if w_float > 0.0:
        oriented_prediction = outputs
    else:
        oriented_prediction = -outputs

    kept_indexes: list[int] = []
    for candidate_index in range(rule_count):
        candidate_prediction = float(oriented_prediction[candidate_index])
        candidate_uncertainty = float(uncertainty[candidate_index])
        dominated = False

        for other_index in range(rule_count):
            if other_index == candidate_index:
                continue

            other_prediction = float(oriented_prediction[other_index])
            other_uncertainty = float(uncertainty[other_index])

            if (
                other_prediction >= candidate_prediction - atol
                and other_uncertainty <= candidate_uncertainty + atol
                and (
                    other_prediction > candidate_prediction + atol
                    or other_uncertainty < candidate_uncertainty - atol
                )
            ):
                dominated = True
                break

        if not dominated:
            kept_indexes.append(int(candidate_index))

    return sorted(kept_indexes)


def _pareto_indexes(
    pred: np.ndarray,
    low: np.ndarray,
    high: np.ndarray,
) -> list[int]:
    return _policy_pareto_indexes(pred, low, high, 0.5, normalize=False)


def timed_call(fn, *args, **kwargs):
    """Return (result, elapsed_seconds)."""

    tic = time.time()
    out = fn(*args, **kwargs)
    return out, float(time.time() - tic)


def can_run_dataset(
    *,
    n_samples: int,
    task: Literal["binary", "multiclass", "regression"],
    config: EnsureRunConfig,
    n_classes: int | None = None,
) -> tuple[bool, str]:
    """Decide whether the dataset is suitable for running the ensured evaluation.

    Returns (ok, reason). If ok is False, reason describes why it's skipped.
    """

    if n_samples <= 3:
        return False, f"too few samples ({n_samples})"

    test_size = _safe_test_size(n_samples, config.test_size)
    if test_size >= n_samples:
        return False, f"test size {test_size} >= n_samples {n_samples}"

    # After removing test, need calibration + minimum training samples
    remaining = n_samples - test_size
    min_cal = max(config.calibration_sizes) if config.calibration_sizes else 100
    min_train = max(100, int(n_classes)) if task in ("binary", "multiclass") and n_classes else 100
    min_needed = min_cal + min_train

    if remaining < min_needed:
        return False, (
            f"not enough remaining samples after test ({remaining} < "
            f"{min_cal} cal + {min_train} train)"
        )

    # For classification, ensure at least one sample per class remains for stratify
    if task in ("binary", "multiclass"):
        if n_classes is None:
            return False, "n_classes required for classification checks"
        if remaining <= int(n_classes):
            return False, (
                f"not enough samples for {n_classes} classes "
                f"(remaining={remaining})"
            )

    return True, "ok"
