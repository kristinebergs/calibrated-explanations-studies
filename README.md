# Calibrated Explanations — Studies and Reproducibility

[![License](https://img.shields.io/badge/License-BSD_3--Clause-blue.svg)](LICENSE)
[![calibrated-explanations](https://img.shields.io/badge/library-calibrated--explanations-orange)](https://github.com/Moffran/calibrated_explanations)

Official reproducibility companion to
[calibrated-explanations](https://github.com/Moffran/calibrated_explanations).
This repository is authoritative for evaluation code, datasets, notebooks,
environment definitions, result archives, and study-specific reproduction
instructions for published Calibrated Explanations research.

Keeping studies separate makes the core package lean while allowing historical
work to preserve its original environment and CE version requirements.

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

---

## Prerequisites

Prerequisites are study-specific. Use the selected study README for its Python
version, CE version-selection rule, environment definition, and any additional
dependencies. Installing a different CE version may change results because APIs
and explanation behaviour have evolved across releases.

---

## Quick Start

### 1. Clone

```bash
git clone https://github.com/kristinebergs/calibrated-explanations-studies.git
cd calibrated-explanations-studies
```

### 2. Select a study

Open the README for the paper or result you want to reproduce in
[`studies/`](studies/). Each study owns its CE version-selection rule,
environment, datasets, random seeds, entry-point commands, and expected
artefacts.

### 3. Follow the study README

Create the documented environment, install the specified historical CE version,
run the study-specific scripts or notebooks, and compare the outputs with that
study's bundled artefacts. Do not assume the latest CE release reproduces an
older paper exactly.

---

## Repository Structure

```
calibrated-explanations-studies/
|-- README.md
|-- data/                  # versioned study datasets
|-- studies/               # one maintained navigation unit per paper
|   |-- binary-classification/
|   |-- calibration-quality/
|   |-- conditional-fairness/
|   |-- ensured/
|   |-- fast-ce/
|   |-- multiclass/
|   `-- regression/
`-- legacy/                # provenance-preserving migrated evaluation tree
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

See the [multiclass study README](studies/multiclass/README.md).

### Regression

**Paper:** Löfström, T., Löfström, H., Johansson, U., Sönströd, C., and Matela, R. —
*Calibrated Explanations for Regression*, Machine Learning 114, 100, 2025.
DOI: [10.1007/s10994-024-06642-8](https://doi.org/10.1007/s10994-024-06642-8)

See the [regression study README](studies/regression/README.md).

### Conditional fairness

**Paper:** Löfström, H. and Löfström, T. —
*Conditional Calibrated Explanations: Finding a Path Between Bias and Uncertainty*,
xAI 2024, Communications in Computer and Information Science, vol 2153. Springer, Cham.
DOI: [10.1007/978-3-031-63787-2_17](https://doi.org/10.1007/978-3-031-63787-2_17)

See the
[conditional-fairness study README](studies/conditional-fairness/README.md).

### Ensured explanations

**Preprint:** Löfström, H., Löfström, T., and Hallberg Szabadváry, J. —
*Ensured: Explanations for Decreasing the Epistemic Uncertainty in Predictions*,
arXiv:2410.05479, 2024.
URL: [arxiv.org/abs/2410.05479](https://arxiv.org/abs/2410.05479)

See the [ensured study README](studies/ensured/README.md).

### Fast CE

**Paper:** Löfström, T., Rabia Yapicioglu, F., Stramiglio, A., Löfström, H., and Vitali, F. —
*Fast Calibrated Explanations: Efficient and Uncertainty-Aware Explanations for Machine Learning Models*,
xAI 2025, Communications in Computer and Information Science, vol 2580. Springer, Cham.
DOI: [10.1007/978-3-032-08333-3_16](https://doi.org/10.1007/978-3-032-08333-3_16)

See the [Fast CE study README](studies/fast-ce/README.md).

---

## Legacy

The `legacy/` folder contains all evaluation code copied directly from the
`calibrated_explanations` main repository (from its `evaluation/` directory).
It is named **legacy** rather than `evaluation` to make clear that:

- This is the original, as-migrated content from the main repo — a faithful copy,
  not a redesigned evaluation framework.
- Maintained study navigation lives under `studies/`, following the per-study
  layout shown above.
- The `legacy/` module path (`python -m legacy.<module>`) signals to contributors
  that these scripts reflect how evaluation was done in the main repo and may not
  conform to any new conventions introduced here.

Use the corresponding study README for current reproduction instructions;
`legacy` describes provenance and preserves the original migrated layout.

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
