# Changelog

All notable changes to this repository are recorded here.
Entries are organized by study area and date.

---

## 2026-06-19 — Initial migration

Migrated all evaluation content from `calibrated_explanations/evaluation/` into this
standalone reproducibility repository as `legacy/`.
See [README.md § Legacy](README.md#legacy) for the rationale behind the folder name.

### Added

**Binary classification**
- `legacy/Classification_Experiment_sota.py` — 25-dataset binary state-of-the-art study
- `legacy/Classification_Experiment_Ablation.py` — ablation over design choices
- `legacy/Classification_Experiment_stab_rob.py` — stability and robustness benchmarks
- `legacy/Classification_Analysis_*.ipynb` — analysis notebooks
- `legacy/Classification_plots.ipynb` — figure generation
- Result archives: `results_sota.pkl`, `results_sota_xGB.pkl`, `results_ablation.pkl`, `results_stab_rob.pkl`

**Multiclass classification**
- `legacy/multiclass/` — multiclass experiment scripts and COPA 2024 result tables

**Regression**
- `legacy/regression/` — regression experiment scripts, notebooks, and result archives

**Ensured explanations**
- `legacy/ensure/` — binary, multiclass, and regression ensured-explanation runners
- LaTeX export utilities

**Guarded explanations**
- `legacy/guarded/` — scenarios A–E: rule usefulness, OOD detection, regression invariants,
  real-data usability, edge-case hardening
- Scenario C LaTeX artifacts

**Reject integration**
- `legacy/reject/` — 14-scenario reject evaluation suite (core + supplementary)
- Scenario artifacts (CSV, JSON, Markdown) for scenarios 1–14

**Conditional fairness**
- `legacy/Conditional_Fairness_Experiment.ipynb`
- `legacy/Conditional_Fairness_Plotting.ipynb`

**Performance & fast filtering**
- `legacy/fast_filtering/` — ablation, feature-overlap, top-k sweep, synthetic sweep
- `legacy/fastCE/` — acceleration timing and regression analysis
- Various ablation result JSON archives (`caching_ablation_results.json`, etc.)

**Datasets**
- `data/` — all benchmark datasets (binary, multiclass, regression)

**Repository infrastructure**
- `README.md`, `LICENSE`, `CITATION.cff`, `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`
- `.github/ISSUE_TEMPLATE/` — bug report and new-scenario templates
- `.gitignore`
