# Fast Calibrated Explanations Study

## Paper

Löfström, T., Rabia Yapicioglu, F., Stramiglio, A., Löfström, H., and Vitali, F. (2024).
**Fast Calibrated Explanations: Efficient and Uncertainty-Aware Explanations for Machine Learning Models.**
In: Guidotti, R., Schmid, U., Longo, L. (eds) *Explainable Artificial Intelligence. xAI 2025.*
Communications in Computer and Information Science, vol 2580. Springer, Cham.
DOI: [10.1007/978-3-032-08333-3_16](https://doi.org/10.1007/978-3-032-08333-3_16)

## Overview

Benchmarks the fast feature filtering and parallel execution paths of calibrated explanations,
demonstrating speedups while preserving explanation fidelity. Covers classification, multiclass,
and regression tasks across many datasets.

## Environment

```bash
conda env create -f environment.yml
conda activate ce-fast-ce
```

> **Pin `calibrated-explanations` to the version stated in the paper** before running.
> Replace `<VERSION>` in `environment.yml` with that version number.
>
> LIME and SHAP are optional comparators. They are pinned in `environment.yml`; omit
> them if you only need the CE-only benchmarks.

## Experiments

Run from the **repo root**. All scripts accept `--help` for a full parameter reference.

### Setup and architecture ablation

```bash
python -m studies.fast-ce.experiments.setup_ablation
```

### Fast feature filtering

```bash
# Timing ablation (with/without fast filtering)
python -m studies.fast-ce.experiments.fast_feature_filtering_ablation

# Multi-dataset version (under fast_filtering/)
python -m studies.fast-ce.experiments.fast_filtering.fast_feature_filtering_ablation_multi

# Feature-overlap fidelity
python -m studies.fast-ce.experiments.fast_filtering.fast_filtering_feature_overlap

# Top-k sweep
python -m studies.fast-ce.experiments.fast_filtering.fast_filtering_topk_sweep

# Dimensionality scaling
python -m studies.fast-ce.experiments.fast_filtering.synthetic_feature_sweep
```

### FastCE acceleration (timing)

```bash
python -m studies.fast-ce.experiments.fastCE.Fast_Experiment_Ablation
python -m studies.fast-ce.experiments.fastCE.Fast_Regression_Experiment
```

## Analysis

| Notebook | Purpose |
|---|---|
| `experiments/fastCE/Fast_Analysis_Times.ipynb` | Timing analysis and figures |
| `experiments/fastCE/Fast_Regression_Analysis.ipynb` | Regression timing analysis |

Analyse fast-filtering results:

```bash
python -m studies.fast-ce.experiments.fast_filtering.analyze_results --plots
```

## Results

| File | Contents |
|---|---|
| `setup_ablation_results.json` | Setup/architecture ablation results |
| `fast_feature_filtering_ablation_results.json` | Fast filtering timing results |
| `caching_ablation_results.json` | Caching ablation results |
| `chunk_size_ablation_results.json` | Chunk size ablation results |
| `parallel_ablation_results.json` | Parallel execution ablation results |
| `conjunction_ablation_results.json` | Conjunction ablation results |
| `synthetic_feature_sweep_results.json` | Dimensionality scaling results |

## Data

Datasets are loaded from `data/` at the repo root.
