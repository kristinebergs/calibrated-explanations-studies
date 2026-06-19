# Calibration Quality Study

## Paper

Löfström, H., Löfström, T., Johansson, U., and Sönströd, C. (2023).
**Investigating the impact of calibration on the quality of explanations.**
*Annals of Mathematics and Artificial Intelligence.*
DOI: [10.1007/s10472-023-09837-2](https://doi.org/10.1007/s10472-023-09837-2)

This is the originating paper for the calibrated-explanations idea.

## Code and data

The code and data for this paper are hosted in a separate repository:

**[https://github.com/tuvelofstrom/calibrating-explanations](https://github.com/tuvelofstrom/calibrating-explanations)**

This study folder exists as a placeholder to keep the CITATION.cff reference anchored
within this repository's study structure. If code is later migrated here, populate
`experiments/`, `analysis/`, and `results/` following the `_template/` conventions.

## Environment

```bash
conda env create -f environment.yml
conda activate ce-calibration-quality
```

> **Pin `calibrated-explanations` to the version stated in the paper** before running.
> Replace `<VERSION>` in `environment.yml` with that version number.
