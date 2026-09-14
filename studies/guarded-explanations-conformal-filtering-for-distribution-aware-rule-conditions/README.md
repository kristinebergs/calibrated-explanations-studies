# Guarded Explanations: Conformal Filtering for Distribution-Aware Rule Conditions

## Reproducibility status

This study covers the publicly recoverable Guarded Explanations implementation and evaluation material.

**Important limitation:** the Oslo real-estate case study is not fully reproducible from this repository. The proprietary Oslo data are not included, and the case-specific experiment code/material used to produce that part of the paper is also not currently available here.

Accordingly, the material in this study should be interpreted as covering the generic/synthetic/benchmark evaluation of Guarded Explanations, not the complete Oslo case study.

## Implementation provenance

The Guarded Explanations implementation entered the Calibrated Explanations codebase in the historical development line that introduced the KNN guard and guarded factual/alternative explanation paths. The study package preserves/references the recoverable public experiment material; the library implementation itself remains versioned in the main `calibrated_explanations` repository.

## Missing Oslo material

- proprietary Oslo real-estate data;
- case-specific runner/preprocessing material not present in the public/recoverable repositories;
- case-specific raw results where not publicly available.

This README makes that boundary explicit so that the existence of a study folder is not mistaken for a claim of full-paper reproducibility.
