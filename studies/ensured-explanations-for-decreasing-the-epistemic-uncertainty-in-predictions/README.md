# Ensured Explanations Study

## Paper

Löfström, H., Löfström, T., and Hallberg Szabadváry, J. (2024).
**Ensured: Explanations for Decreasing the Epistemic Uncertainty in Predictions.**
arXiv preprint arXiv:2410.05479.
URL: [arxiv.org/abs/2410.05479](https://arxiv.org/abs/2410.05479)

## Overview

Evaluates ensured explanations — a mechanism for filtering explanation candidates to
decrease epistemic uncertainty in predictions — across binary classification, multiclass
classification, and regression tasks.

## Environment

```bash
conda env create -f environment.yml
conda activate ce-ensured
```

> **Pin `calibrated-explanations` to the version stated in the paper** before running.
> Replace `<VERSION>` in `environment.yml` with that version number.

## Experiments

Run from the **repo root**. Use `--limit-datasets N` for a quick sanity run.

```bash
# Binary classification
python -m studies.ensured.experiments.experiment_ensure_binary
python -m studies.ensured.experiments.experiment_ensure_binary --limit-datasets 2

# Multiclass classification
python -m studies.ensured.experiments.experiment_ensure_multiclass

# Regression
python -m studies.ensured.experiments.experiment_ensure_regression
```

Key parameters (same flags on all three runners):

| Flag | Default | Description |
|---|---|---|
| `--test-size` | 100 | Number of test instances |
| `--calibration-sizes` | 100 300 500 | Calibration set sizes to sweep |
| `--n-top-features` | 5 | Top features for conjunctions |
| `--max-rule-size` | 2 | Maximum conjunction size |
| `--out` | `results/results_ensure_<task>.pkl` | Output path |

## Export LaTeX tables

After generating `.pkl` result files:

```bash
python -m studies.ensured.experiments.export_ensure_tables_latex
```

## Analysis

```bash
jupyter notebook studies/ensured/experiments/analysis_ensure.ipynb
```

## Results

No pre-computed result archives are included — run the experiments to generate them.
Results are written to `results/` by default.

## Data

Datasets are loaded from `data/` at the repo root.
