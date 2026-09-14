# Binary Classification Study

## Paper

Löfström, H., Löfström, T., Johansson, U., and Sönströd, C. (2024).
**Calibrated Explanations: with Uncertainty Information and Counterfactuals.**
*Expert Systems with Applications.*
DOI: [10.1016/j.eswa.2024.123154](https://doi.org/10.1016/j.eswa.2024.123154)

## Overview

Reproduces the 25-dataset binary classification study comparing calibrated explanations
against LIME and SHAP (state-of-the-art), together with an ablation over design choices
and a stability/robustness benchmark.

## Environment

```bash
conda env create -f environment.yml
conda activate ce-binary-classification
```

The published paper describes **Calibrated Explanations v0.2.3**, and the reproduction
environment is therefore pinned to `calibrated-explanations==0.2.3`. Repository history
also shows that some experiments were completed immediately before the release while
the package identified itself as the development version `0.2.3a`. Version 0.2.3 is the
appropriate released version for reproducing the published study.

The state-of-the-art comparison uses `lime==0.2.0.1` and `shap==0.44.0`; these versions
are also pinned in `environment.yml`.

## Experiments

Run from the **repo root** so that `studies` is importable:

```bash
# State-of-the-art comparison (25 datasets, CE vs LIME vs SHAP)
python -m studies.binary-classification.experiments.Classification_Experiment_sota

# Ablation study
python -m studies.binary-classification.experiments.Classification_Experiment_Ablation

# Stability and robustness
python -m studies.binary-classification.experiments.Classification_Experiment_stab_rob

# SOTA comparison ablation
python -m studies.binary-classification.experiments.sota_comparison_ablation
```

## Analysis

Open the notebooks from the repo root with Jupyter:

| Notebook | Purpose |
|---|---|
| `analysis/Classification_Analysis_sota.ipynb` | State-of-the-art results |
| `analysis/Classification_Analysis_Ablation.ipynb` | Ablation results |
| `analysis/Classification_Analysis_stab_rob.ipynb` | Stability / robustness results |
| `analysis/Classification_plots.ipynb` | Paper figure generation |

## Results

Pre-computed result archives are in `results/` for comparison without re-running:

| File | Contents |
|---|---|
| `results_sota.pkl` | 25-dataset CE vs LIME vs SHAP results |
| `results_sota_xGB.pkl` | XGBoost variant results |
| `results_sota.zip` | Compressed archive of sota results |
| `results_ablation.pkl` | Ablation study results |
| `results_stab_rob.pkl` | Stability/robustness results |
| `sota_comparison_results.json` | Machine-readable sota comparison summary |
| `Calibrated_Explanations_Ablation.pdf` | Ablation study PDF report |

## Data

Datasets are loaded from `data/` at the repo root (`data/*.csv`).
