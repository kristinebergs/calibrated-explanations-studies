# Calibrated Explanations — Studies and Reproducibility

Official reproducibility companion to [calibrated-explanations](https://github.com/Moffran/calibrated_explanations).

Each maintained study directory is named after the corresponding paper title. Historical material is preserved as faithfully as possible; when a study is only partially reproducible, its README states the missing material explicitly.

## Studies

| Paper / study | Directory | Public reproduction status |
|---|---|---|
| *Calibrated Explanations: with Uncertainty Information and Counterfactuals* | `studies/calibrated-explanations-with-uncertainty-information-and-counterfactuals` | Code, analysis and archived results |
| *Investigating the Impact of Calibration on the Quality of Explanations* | `studies/investigating-the-impact-of-calibration-on-the-quality-of-explanations` | Original experiment code, analysis and CSV results migrated |
| *Calibrated Explanations for Regression* | `studies/calibrated-explanations-for-regression` | Code, analysis and archived results |
| *Calibrated Explanations for Multi-class* | `studies/calibrated-explanations-for-multi-class` | Code and archived results |
| *Conditional Calibrated Explanations: Finding a Path Between Bias and Uncertainty* | `studies/conditional-calibrated-explanations-finding-a-path-between-bias-and-uncertainty` | Notebook-driven study and archived results |
| *Fast Calibrated Explanations: Efficient and Uncertainty-Aware Explanations for Machine Learning Models* | `studies/fast-calibrated-explanations-efficient-and-uncertainty-aware-explanations-for-machine-learning-models` | Code and archived evaluation material |
| *Ensured: Explanations for Decreasing the Epistemic Uncertainty in Predictions* | `studies/ensured-explanations-for-decreasing-the-epistemic-uncertainty-in-predictions` | Experiment code; results generated locally |
| *Calibrated Explanations for Within-Spec Risk Prediction: Uncertainty-Aware Decision Support* | `studies/calibrated-explanations-for-within-spec-risk-prediction-uncertainty-aware-decision-support` | Partial: recovered code/figures; raw result files still missing |
| *Guarded Explanations: Conformal Filtering for Distribution-Aware Rule Conditions* | `studies/guarded-explanations-conformal-filtering-for-distribution-aware-rule-conditions` | Partial: Oslo case data and case-specific code are not included |
| *Uncertainty-Aware Decision Support in Power-Grid Demand Forecasting* | `studies/uncertainty-aware-decision-support-in-power-grid-demand-forecasting` | README only; operational data are restricted |

## Usage

Clone the repository and open the README in the study directory for the paper you want to reproduce. Environment requirements, commands, available results and known gaps are study-specific. Do not assume that the latest Calibrated Explanations release exactly reproduces historical papers.

The top-level `data/` directory contains shared versioned datasets used by several studies. `legacy/` preserves the evaluation tree migrated from the main Calibrated Explanations repository and should be treated as provenance material rather than the maintained navigation structure.

## Citation

Please cite the paper corresponding to the study you use, together with the Calibrated Explanations software where appropriate. Machine-readable citation metadata is available in `CITATION.cff`.

## License

BSD 3-Clause — see `LICENSE`.
