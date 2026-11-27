# Source inventory (integration)

Primary source: user-supplied `ENSURED-explanations-main.zip`, SHA-256
`53f9e38f49cc19f33485370ebf82205ef5c0ddf82a10152a7a0f361fff542f70`.
The ZIP has five Python files and seven Markdown files; it has no datasets,
dataset loader, notebook, environment definition, or tests. All five Python
files were compared with the 2024 study before copying. The attached
Markdown files were read as source documentation, not repository instructions;
some contain old paths or unverified empirical claims and were not copied.

| File | ZIP vs 2024 study | Integration action |
| --- | --- | --- |
| `common_ensure.py` | Expanded ranking, disagreement and policy Pareto logic | Copy ZIP; implement article score directly to avoid CE helper's negative-weight offset |
| `experiment_ensure_binary.py` | Nearly identical runner, changed local imports | Copy ZIP; remove obsolete path bootstrap; add dataset selector |
| `experiment_ensure_multiclass.py` | Nearly identical runner, changed local imports | Same |
| `experiment_ensure_regression.py` | Nearly identical runner, changed local imports | Same |
| `export_ensure_tables_latex.py` | New policy table and many added collection calls | Copy ZIP; retain known aggregation defect for reviewer-evidence step |
| `datasets_ensure.py` | Absent from ZIP | Copy 2024 loader and registry; its `parents[2]` root calculation works at this study-root location |
| `analysis_ensure.ipynb` | Absent from ZIP | Leave 2024 notebook in historical study; no current-analysis notebook created |
| `experiment_ensure.py` | Absent from ZIP | Leave 2024 original experiment in historical study |
| Study README and environment | Absent from ZIP | Write article-specific instructions and environment |

The 2024 study and `legacy/ensure` are preserved without edits. The new
directory is the only maintained implementation for the current article.
