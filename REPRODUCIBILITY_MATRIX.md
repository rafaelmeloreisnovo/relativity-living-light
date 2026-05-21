# REPRODUCIBILITY_MATRIX

## Command inventory (supported flows)

| Command | Expected inputs | Outputs | Current status |
|---|---|---|---|
| `python -m rll.cli run --data synthetic --model rll` | Python env + in-repo synthetic pipeline files | Synthetic run logs and generated artifacts from Structure D flow | Implemented and exercised by tests |
| `python -m rll.cli run --data real --model rll` | Real-data scripts and required datasets according to chosen flow | Real-flow execution logs and downstream artifacts | Implemented; data-dependent |
| `python -m rll.cli run --data real --with-bayes` | Pantheon+/real inputs required by `docs/panteon_likelihood.py` | Comparative/AIC-BIC style output from selected script | Implemented; data-dependent |
| `python -m rll.cli run --data real --with-covariance` | Pantheon+ covariance + dependencies | Covariance-aware run via selected script | Implemented; data-dependent |
| `python -m rll.cli preflight-real` | `data/pantheon/lcparam_full_long_zhel.txt`, `data/pantheon/Pantheon+SH0ES_STAT+SYS.cov` | Human-readable pass/fail listing; exit `0` or `2` | Implemented |
| `python -m rll.cli preflight-real --json` | Same as above | JSON payload with `passed/missing/required`; exit `0` or `2` | Implemented (added in this hardening pass) |
| `python scripts/verify_pantheon_inputs.py` | Same required Pantheon+ files | Human-readable file status + SHA256 for existing files; exit `0` or `2` | Implemented (added in this hardening pass) |
| `python scripts/verify_pantheon_inputs.py --json` | Same required Pantheon+ files | JSON verification report including SHA256 and size; exit `0` or `2` | Implemented (added in this hardening pass) |
| `pytest -q` | Test dependencies + local source tree | Test report with pass/fail summary | Executed in this hardening pass |

## Status legend
- **Implemented**: command is present and invocable.
- **Data-dependent**: command behavior depends on external/locally provisioned real datasets.

## Core/archive boundary recommendation
- Keep archival and historical content immutable for traceability.
- Treat `src/`, `tests/`, `scripts/`, and `data/` reproducibility docs as the **core execution boundary** for scientific validation.
- Treat broad narrative corpora (`newadd/`, `RMR/`, duplicate archives, exploratory notebooks) as **archive/reference boundary** unless promoted with reproducibility metadata.
