# Calibrated Explanations — Evaluation Suite

[![License](https://img.shields.io/badge/License-BSD_3--Clause-blue.svg)](LICENSE)
[![calibrated-explanations](https://img.shields.io/badge/library-calibrated--explanations-orange)](https://github.com/Moffran/calibrated_explanations)

Reproducibility companion to [calibrated-explanations](https://github.com/Moffran/calibrated_explanations).
This repository contains all evaluation code, experiment runners, Jupyter notebooks, and result
artifacts for the published calibrated-explanations studies.
The evaluation suite is kept separate from the core library to keep the package lean while making
every published result fully reproducible.

---

## Overview

### Studies (one folder per paper)

| Study | Task types | Paper | README |
|---|---|---|---|
| `studies/binary-classification` | Classification | ESWA 2024 | [README](studies/binary-classification/README.md) |
| `studies/calibration-quality` | Classification | AMAI 2023 | [README](studies/calibration-quality/README.md) |
| `studies/regression` | Regression | ML 2025 | [README](studies/regression/README.md) |
| `studies/multiclass` | Multiclass | PMLR 2024 | [README](studies/multiclass/README.md) |
| `studies/conditional-fairness` | Classification | xAI 2024 | [README](studies/conditional-fairness/README.md) |
| `studies/fast-ce` | Classification · Multiclass · Regression | xAI 2025 | [README](studies/fast-ce/README.md) |
| `studies/ensured` | Classification · Multiclass · Regression | arXiv 2024 | [README](studies/ensured/README.md) |

> New studies go in `studies/` following the `studies/_template/` conventions.

### Legacy (migrated from main repo)

The `legacy/` folder contains the original evaluation code as it existed in
`calibrated_explanations/evaluation/`. See [README § Legacy](README.md#legacy) and
[legacy/README.md](legacy/README.md) for details.

---

## Prerequisites

- Python ≥ 3.8
- `calibrated-explanations` — **each study was produced with the library version current at
  time of publication.** The exact version is stated in the corresponding paper (typically as
  a tag or release number). Install the version referenced in the paper you are reproducing:
  ```
  pip install "calibrated-explanations==<version from paper>"
  ```
  Installing a different version may change outputs, since explanation behaviour and APIs
  have evolved across releases.

> **Note:** `calibrated-explanations` itself is not listed in `legacy/requirements.txt` or
> `legacy/environment.yml` — those files cover only the additional evaluation dependencies
> (LIME, SHAP, XGBoost, etc.). Install the library separately at the correct version first.

---

## Quick Start

### 1. Clone

```bash
git clone https://github.com/Moffran/calibrated-explanations-evaluations.git
cd calibrated-explanations-evaluations
```

### 2. Environment

**Conda (recommended):**

```bash
conda env create -f legacy/environment.yml
conda activate ce-evaluation
```

**pip:**

```bash
python -m venv .venv
# Windows:
.\.venv\Scripts\activate
# Linux / macOS:
source .venv/bin/activate

pip install "calibrated-explanations==<version from paper>"
pip install -r legacy/requirements.txt
```

For notebooks, also install:

```bash
pip install "calibrated-explanations[viz,notebooks]"
```

### 3. Verify data

Datasets live in `data/` at the repo root. Binary classification benchmarks read from
`data/*.csv`; multiclass from `data/Multiclass/multi/`; regression from `data/reg/`.
No additional download is required — all datasets are versioned in this repository.

### 4. Run an experiment

All scripts use module execution from the repo root so that `legacy` is importable:

```bash
# Binary classification — state-of-the-art comparison
python -m legacy.Classification_Experiment_sota

# Ensured explanations — quick sanity run
python -m legacy.ensure.experiment_ensure_binary --limit-datasets 2

# Reject integration — full core suite
python -m legacy.reject.run_all_guarded --full

# Fast filtering ablation
python -m legacy.fast_filtering.fast_feature_filtering_ablation_multi --tasks classification --limit 3
```

See each sub-README for the full parameter reference.

---

## Repository Structure

```
calibrated-explanations-evaluations/
│
├── README.md                   ← you are here
├── LICENSE                     ← BSD 3-Clause
├── CITATION.cff                ← machine-readable citation
├── CONTRIBUTING.md
├── CODE_OF_CONDUCT.md
├── CHANGELOG.md
│
├── data/                       ← benchmark datasets (versioned)
│   ├── *.csv                   ← binary classification datasets
│   ├── Multiclass/             ← multiclass datasets
│   └── reg/                    ← regression datasets
│
└── legacy/                     ← experiment code from calibrated_explanations (see Legacy below)
    ├── __init__.py
    ├── environment.yml          ← conda environment
    ├── requirements.txt         ← pip alternative
    │
    ├── Classification_Experiment_sota.py
    ├── Classification_Experiment_Ablation.py
    ├── Classification_Experiment_stab_rob.py
    ├── Classification_Analysis_*.ipynb
    ├── Classification_plots.ipynb
    ├── Conditional_Fairness_Experiment.ipynb
    ├── Conditional_Fairness_Plotting.ipynb
    │
    ├── ensure/                  ← ensured explanations study
    ├── fast_filtering/          ← performance & fast filtering study
    ├── fastCE/                  ← fast CE acceleration study
    ├── guarded/                 ← guarded explanations study
    ├── multiclass/              ← multiclass study
    ├── regression/              ← regression study
    ├── reject/                  ← reject integration study
    └── scripts/                 ← shared helper scripts
```

---

## Studies

### Binary classification

**Paper:** Löfström, H., Löfström, T., Johansson, U., and Sönströd, C. —
*Calibrated Explanations: with Uncertainty Information and Counterfactuals*,
Expert Systems with Applications, 2024.
DOI: [10.1016/j.eswa.2024.123154](https://doi.org/10.1016/j.eswa.2024.123154)

Scripts reproduce the 25-dataset binary study (`sota`), the ablation over design choices, and
the stability / robustness benchmarks.
Result archives (`results_sota.pkl`, `results_ablation.pkl`, `results_stab_rob.pkl`) are
included for comparison without re-running.

### Multiclass classification

**Paper:** Löfström, T., Löfström, H., and Johansson, U. —
*Calibrated Explanations for Multi-class*,
Proceedings of the Thirteenth Workshop on Conformal and Probabilistic Prediction and Applications,
PMLR 230:175–194, 2024.
PDF: [lofstrom24a.pdf](https://raw.githubusercontent.com/mlresearch/v230/main/assets/lofstrom24a/lofstrom24a.pdf)

See [legacy/multiclass/](legacy/multiclass/).

### Regression

**Paper:** Löfström, T., Löfström, H., Johansson, U., Sönströd, C., and Matela, R. —
*Calibrated Explanations for Regression*, Machine Learning 114, 100, 2025.
DOI: [10.1007/s10994-024-06642-8](https://doi.org/10.1007/s10994-024-06642-8)

See [legacy/regression/](legacy/regression/).

### Conditional fairness

**Paper:** Löfström, H. and Löfström, T. —
*Conditional Calibrated Explanations: Finding a Path Between Bias and Uncertainty*,
xAI 2024, Communications in Computer and Information Science, vol 2153. Springer, Cham.
DOI: [10.1007/978-3-031-63787-2_17](https://doi.org/10.1007/978-3-031-63787-2_17)

Notebooks in [legacy/](legacy/) (`Conditional_Fairness_*.ipynb`).

### Ensured explanations

**Preprint:** Löfström, H., Löfström, T., and Hallberg Szabadváry, J. —
*Ensured: Explanations for Decreasing the Epistemic Uncertainty in Predictions*,
arXiv:2410.05479, 2024.
URL: [arxiv.org/abs/2410.05479](https://arxiv.org/abs/2410.05479)

See [legacy/ensure/README.md](legacy/ensure/README.md) for prerequisites,
quick-run commands, and LaTeX export instructions.

### Guarded explanations

Scenarios A–E covering rule usefulness, OOD detection quality, and engineering invariants.
See [legacy/guarded/README.md](legacy/guarded/README.md) for the full scenario guide
and paper-use rules.

### Reject integration

**Paper:** Hallberg Szabadváry, J., Löfström, T., Johansson, U., Sönströd, C., Ahlberg, E., and Carlsson, L. —
*Classification with reject option: Distribution-free error guarantees via conformal prediction*,
Machine Learning with Applications 20, 100664, 2025.
DOI: [10.1016/j.mlwa.2025.100664](https://doi.org/10.1016/j.mlwa.2025.100664)

14 scenarios mapping to research questions RQ1–RQ6 and contributions C1–C4.
See [legacy/reject/README.md](legacy/reject/README.md).

### Performance & fast filtering

**Paper:** Löfström, T., Rabia Yapicioglu, F., Stramiglio, A., Löfström, H., and Vitali, F. —
*Fast Calibrated Explanations: Efficient and Uncertainty-Aware Explanations for Machine Learning Models*,
xAI 2025, Communications in Computer and Information Science, vol 2580. Springer, Cham.
DOI: [10.1007/978-3-032-08333-3_16](https://doi.org/10.1007/978-3-032-08333-3_16)

Multi-dataset ablation, feature-overlap fidelity, top-k sweep, and dimensionality scaling.
See [legacy/fast_filtering/README.md](legacy/fast_filtering/README.md).

---

## Legacy

The `legacy/` folder contains all evaluation code copied directly from the
`calibrated_explanations` main repository (from its `evaluation/` directory).
It is named **legacy** rather than `evaluation` to make clear that:

- This is the original, as-migrated content from the main repo — a faithful copy,
  not a redesigned evaluation framework.
- Future studies in this repository will live in their own top-level folders
  alongside `legacy/`, following a cleaner per-study layout.
- The `legacy/` module path (`python -m legacy.<module>`) signals to contributors
  that these scripts reflect how evaluation was done in the main repo and may not
  conform to any new conventions introduced here.

Scripts inside `legacy/` are fully functional; "legacy" describes provenance, not quality.

---

## Citation

If you use this evaluation suite or the calibrated-explanations library in your research,
please cite the relevant paper(s) below.

**Binary classification (primary):**

```bibtex
@article{lofstrom2024calibrated,
  title   = {Calibrated Explanations: with Uncertainty Information and Counterfactuals},
  author  = {L{\"o}fstr{\"o}m, Helena and L{\"o}fstr{\"o}m, Tuwe and Johansson, Ulf and S{\"o}nstr{\"o}d, Cecilia},
  journal = {Expert Systems with Applications},
  year    = {2024},
  doi     = {10.1016/j.eswa.2024.123154}
}
```

**Regression:**

```bibtex
@article{lofstrom2025regression,
  title   = {Calibrated Explanations for Regression},
  author  = {L{\"o}fstr{\"o}m, Tuwe and L{\"o}fstr{\"o}m, Helena and Johansson, Ulf and S{\"o}nstr{\"o}d, Cecilia and Matela, Rudy},
  journal = {Machine Learning},
  volume  = {114},
  number  = {100},
  year    = {2025},
  doi     = {10.1007/s10994-024-06642-8}
}
```

**Multiclass:**

```bibtex
@inproceedings{lofstrom2024multiclass,
  title     = {Calibrated Explanations for Multi-class},
  author    = {L{\"o}fstr{\"o}m, Tuwe and L{\"o}fstr{\"o}m, Helena and Johansson, Ulf},
  booktitle = {Proceedings of the Thirteenth Workshop on Conformal and Probabilistic Prediction and Applications},
  series    = {Proceedings of Machine Learning Research},
  volume    = {230},
  pages     = {175--194},
  year      = {2024},
  url       = {https://raw.githubusercontent.com/mlresearch/v230/main/assets/lofstrom24a/lofstrom24a.pdf}
}
```

**Conditional fairness:**

```bibtex
@inproceedings{lofstrom2024fairness,
  title     = {Conditional Calibrated Explanations: Finding a Path Between Bias and Uncertainty},
  author    = {L{\"o}fstr{\"o}m, Helena and L{\"o}fstr{\"o}m, Tuwe},
  booktitle = {Explainable Artificial Intelligence. xAI 2024},
  series    = {Communications in Computer and Information Science},
  volume    = {2153},
  publisher = {Springer, Cham},
  year      = {2024},
  doi       = {10.1007/978-3-031-63787-2_17}
}
```

**Fast Calibrated Explanations:**

```bibtex
@inproceedings{lofstrom2024fast,
  title     = {Fast Calibrated Explanations: Efficient and Uncertainty-Aware Explanations for Machine Learning Models},
  author    = {L{\"o}fstr{\"o}m, Tuwe and {Rabia Yapicioglu}, Fatima and Stramiglio, Andrea and L{\"o}fstr{\"o}m, Helena and Vitali, Fabio},
  booktitle = {Explainable Artificial Intelligence. xAI 2025},
  series    = {Communications in Computer and Information Science},
  volume    = {2580},
  publisher = {Springer, Cham},
  year      = {2024},
  doi       = {10.1007/978-3-032-08333-3_16}
}
```

**Reject integration:**

```bibtex
@article{hallberg2025reject,
  title   = {Classification with reject option: Distribution-free error guarantees via conformal prediction},
  author  = {Hallberg Szabadv{\'a}ry, Johan and L{\"o}fstr{\"o}m, Tuwe and Johansson, Ulf and S{\"o}nstr{\"o}d, Cecilia and Ahlberg, Ernst and Carlsson, Lars},
  journal = {Machine Learning with Applications},
  volume  = {20},
  pages   = {100664},
  year    = {2025},
  doi     = {10.1016/j.mlwa.2025.100664}
}
```

**Ensured explanations (preprint):**

```bibtex
@misc{lofstrom2024ensured,
  title         = {Ensured: Explanations for Decreasing the Epistemic Uncertainty in Predictions},
  author        = {L{\"o}fstr{\"o}m, Helena and L{\"o}fstr{\"o}m, Tuwe and Hallberg Szabadv{\'a}ry, Johan},
  year          = {2024},
  eprint        = {2410.05479},
  archivePrefix = {arXiv}
}
```

A machine-readable [CITATION.cff](CITATION.cff) is also provided.

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).

## Code of Conduct

See [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).

## License

BSD 3-Clause — see [LICENSE](LICENSE).
Copyright © 2023 Helena Löfström.
