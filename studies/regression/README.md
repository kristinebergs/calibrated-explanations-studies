# Regression Study

## Paper

Löfström, T., Löfström, H., Johansson, U., Sönströd, C., and Matela, R. (2025).
**Calibrated Explanations for Regression.**
*Machine Learning* 114, 100.
DOI: [10.1007/s10994-024-06642-8](https://doi.org/10.1007/s10994-024-06642-8)

## Overview

Reproduces the regression explanation study covering stability and robustness benchmarks
across multiple regression datasets, with conformal and probabilistic interval variants.

## Environment

```bash
conda env create -f environment.yml
conda activate ce-regression
```

> **Pin `calibrated-explanations` to the version stated in the paper** before running.
> Replace `<VERSION>` in `environment.yml` with that version number.

## Experiments

Run from the **repo root**:

```bash
python -m studies.regression.experiments.Regression_Experiment_stab_rob
```

## Analysis

| Notebook | Purpose |
|---|---|
| `analysis/Regression_Analysis.ipynb` | Full regression results and paper figures |

## Results

| File | Contents |
|---|---|
| `results_regression_test.pkl` | Regression test run results |
| `results_rob_paper.pkl` | Robustness results (paper baseline) |
| `results_stab_paper.pkl` | Stability results (paper baseline) |
| `results/paper results formatted.xlsx` | Formatted paper tables |

## Data

Regression datasets are loaded from `data/reg/` at the repo root.
