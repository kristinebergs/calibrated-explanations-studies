# <Study Name>

## Paper

<Author Last>, <First>., et al. (<Year>).
**<Full Paper Title>.**
*<Journal or Proceedings>.*
DOI: [<doi>](https://doi.org/<doi>)

## Overview

<!-- One paragraph: what does this study evaluate, what is the key claim or metric? -->

## Environment

```bash
conda env create -f environment.yml
conda activate ce-<study-name>
```

> **Pin `calibrated-explanations` to the version stated in the paper** before running.
> Replace `<VERSION>` in `environment.yml` with that version number.

## Experiments

Run from the **repo root** so that `studies` is importable:

```bash
python -m studies.<study-name>.experiments.<script-name>
```

<!-- List all runnable entry points with a brief description of each. -->

## Analysis

<!-- List notebooks and their purpose, or note that analysis is script-driven. -->

| Notebook | Purpose |
|---|---|
| `analysis/<notebook>.ipynb` | <description> |

## Results

<!-- Describe what is written to results/ and how to interpret the main output files. -->

| File | Contents |
|---|---|
| `results/<file>` | <description> |

## Data

<!-- State which subfolder(s) under data/ this study reads from. -->

Datasets are loaded from `data/` at the repo root.
