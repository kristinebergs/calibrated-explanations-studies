# Conditional Fairness Study

## Paper

Löfström, H. and Löfström, T. (2024).
**Conditional Calibrated Explanations: Finding a Path Between Bias and Uncertainty.**
In: Longo, L., Lapuschkin, S., Seifert, C. (eds) *Explainable Artificial Intelligence. xAI 2024.*
Communications in Computer and Information Science, vol 2153. Springer, Cham.
DOI: [10.1007/978-3-031-63787-2_17](https://doi.org/10.1007/978-3-031-63787-2_17)

## Overview

Evaluates Mondrian (conditional) calibration for fairness-aware explanations across
several real-world datasets, examining how conditioning on subgroups affects explanation
quality and bias.

## Environment

```bash
conda env create -f environment.yml
conda activate ce-conditional-fairness
```

> **Pin `calibrated-explanations` to the version stated in the paper** before running.
> Replace `<VERSION>` in `environment.yml` with that version number.

## Analysis

The study is notebook-driven. Open from the repo root with Jupyter:

| Notebook | Purpose |
|---|---|
| `analysis/Conditional_Fairness_Experiment.ipynb` | Full conditional fairness experiments |
| `analysis/Conditional_Fairness_Plotting.ipynb` | Paper figure generation |

## Results

Pre-computed Mondrian calibration result archives:

| File | Dataset |
|---|---|
| `results_mondrian_1.pkl` | Baseline dataset |
| `results_mondrian_Adult_1.pkl` | Adult income dataset |
| `results_mondrian_CaC_1.pkl` | Credit at Chance dataset |
| `results_mondrian_COMPAS_1.pkl` | COMPAS recidivism dataset |
| `results_mondrian_German_1.pkl` | German credit dataset |
| `results_mondrian_Housing_1.pkl` | Housing dataset |

## Data

Datasets are loaded from `data/` at the repo root.
