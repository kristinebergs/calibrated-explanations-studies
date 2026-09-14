# Investigating the Impact of Calibration on the Quality of Explanations

## Paper

Löfström, H., Löfström, T., Johansson, U., and Sönströd, C. (2023).
**Investigating the impact of calibration on the quality of explanations.**
*Annals of Mathematics and Artificial Intelligence.*
DOI: https://doi.org/10.1007/s10472-023-09837-2

## Provenance

This study has been migrated from the original repository `tuvelofstrom/calibrating-explanations` into the Calibrated Explanations studies repository.

The migrated material includes the original experiment scripts, statistical analysis notebook, and archived CSV results. The original study predates the `calibrated-explanations` package and therefore has no CE package dependency.

## Experiments

The original scripts are under `experiments/`:

- `experiment_1.py`
- `experiment_2.py`
- `experiment_utils.py`

Run them from the repository root so that the shared `data/` directory is available.

## Analysis

`analysis/significance.ipynb` contains the Wilcoxon significance analysis used with the archived result table.

## Results

The archived result files include:

- `results/experiment_1.csv`
- `results/experiments.csv`

The original repository also contains an Excel rendering of the results. CSV files are preserved here as the canonical machine-readable outputs.

## Data

The original scripts use the same binary benchmark datasets that are already versioned in this repository's top-level `data/` directory. They are therefore not duplicated inside this study folder.
