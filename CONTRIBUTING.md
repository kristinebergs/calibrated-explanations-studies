# Contributing

Thank you for your interest in the Calibrated Explanations studies repository.
This repository is primarily a reproducibility archive; contributions are most valuable
in the form of bug reports, dataset corrections, and new evaluation scenarios tied
to published or under-review work.

---

## Reporting a bug

Use the [Bug Report](ISSUE_TEMPLATE/bug_report.md) issue template.
Please include:

- The scenario or script name (for example
  `legacy.reject.scenario_1_binary_coverage`)
- Operating system and Python version
- The exact command you ran (from the repo root)
- Full error output or unexpected result

---

## Proposing a new evaluation scenario

Use the [New Scenario](ISSUE_TEMPLATE/new_scenario.md) issue template.
A scenario proposal should state:

- The research question or paper it supports
- Which study area it belongs to (or that it is a new one)
- The primary metric and acceptance criterion
- Whether result artifacts should be versioned

---

## Submitting a fix or new scenario

1. Fork the repository and create a branch from `main`.
2. Follow the selected study README. For a legacy script, run from the
   repository root so `legacy` is importable:
   ```bash
   python -m legacy.<module> --quick   # for legacy/ scripts
   ```
3. Verify that existing artifacts are not changed by your fix unless that is the intent.
4. Open a pull request with a clear description of what changed and why.

---

## Code style

- Evaluation scripts are research code; strict formatting is not enforced.
- Keep new scripts runnable using the entry-point command documented by their
  study README.
- Record new study dependencies in that study's environment definition and
  update its README in the same change.

---

## Dataset additions

- Place new datasets under `data/` following the existing layout conventions
  (`data/*.csv` for binary, `data/Multiclass/multi/` for multiclass, `data/reg/` for regression).
- All datasets in this repository are small enough to version directly.
  Do not add files larger than ~30 MB without discussion.

---

## Questions

Open a [GitHub Discussion](https://github.com/kristinebergs/calibrated-explanations-studies/discussions)
or contact the maintainers via the email addresses in [CITATION.cff](CITATION.cff).
