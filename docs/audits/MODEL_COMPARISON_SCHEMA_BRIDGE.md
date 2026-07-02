# Model Comparison Schema Bridge

## Status

`hotfix / structural_compatibility`

## Problem

The real-data pipeline may materialize `tables/model_comparison.csv` with uppercase information-criterion columns:

```text
AIC
BIC
```

Some downstream audit/EFT consumers expect lowercase aliases:

```text
aic
bic
```

Without a schema bridge, a valid materialized model-comparison table can look incomplete to downstream readers and produce an artificial `TOKEN_VAZIO`.

## Hotfix

Use:

```bash
python3 tools/normalize_model_comparison_csv.py artifacts/real-data-contract/tables/model_comparison.csv
```

The tool preserves existing values and adds missing compatibility aliases:

| Source column | Compatibility alias |
|---|---|
| `AIC` | `aic` |
| `BIC` | `bic` |
| `chi2` | `chi2_total` |

## Claim boundary

This bridge is structural only.

It does not:

- validate RLL;
- select a winning cosmological model;
- modify scientific results;
- promote mock/synthetic artifacts;
- change the EFT decision logic.

It only prevents a capitalization mismatch from becoming a false `TOKEN_VAZIO`.
