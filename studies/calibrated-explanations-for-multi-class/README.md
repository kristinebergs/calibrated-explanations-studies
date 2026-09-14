# Multiclass Classification Study

## Paper

Löfström, T., Löfström, H., and Johansson, U. (2024).
**Calibrated Explanations for Multi-class.**
*Proceedings of the Thirteenth Workshop on Conformal and Probabilistic Prediction and Applications,*
PMLR 230:175–194.
PDF: [lofstrom24a.pdf](https://raw.githubusercontent.com/mlresearch/v230/main/assets/lofstrom24a/lofstrom24a.pdf)

## Overview

Reproduces the multiclass calibrated explanations study, including the main multiclass
experiment and Venn-Abers normalization experiments on real-world multiclass datasets.

## Environment

```bash
conda env create -f environment.yml
conda activate ce-multiclass
```

> **Pin `calibrated-explanations` to the version stated in the paper** before running.
> Replace `<VERSION>` in `environment.yml` with that version number.

## Experiments

Run from the **repo root**:

```bash
# Main multiclass experiment
python -m studies.multiclass.experiments.Experiment_Multiclass

# Real-data multiclass experiment
python -m studies.multiclass.experiments.experiment_real_multiclass

# Venn-Abers normalization study
python -m studies.multiclass.experiments.experiment_va_normalization
```

Generate plots after running experiments:

```bash
python -m studies.multiclass.experiments.Plots_Multiclass
```

## Results

| File | Contents |
|---|---|
| `results_COPA_2024.csv` | Full COPA 2024 result table |
| `results_COPA_2024.xlsx` | Formatted COPA 2024 result table |

## Data

Multiclass datasets are loaded from `data/Multiclass/multi/` at the repo root.
