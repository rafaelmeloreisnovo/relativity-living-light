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
| `python scripts/run_real_pantheon_validation.py` | `data/pantheon/*` + scipy/numpy runtime | Executes verify+preflight+real run and writes `data/results/model_comparison.json` | Infrastructure-ready; real-data conclusion pending metric interpretation. |
| `python scripts/bh_flux_calc.py --preset sgr-a-star` | In-repo script only; optional user-provided weights | JSON BH mass-flux diagnostic for Sgr A* benchmark preset | Implemented; benchmark-only |
| `python scripts/bh_flux_calc.py --preset m87-star-low` | In-repo script only; optional user-provided weights | JSON BH mass-flux diagnostic for M87* benchmark preset | Implemented; benchmark-only |
| `python scripts/bh_flux_calc.py --preset quasar-demo` | In-repo script only; optional user-provided weights | JSON BH mass-flux diagnostic for illustrative quasar-scale preset | Implemented; benchmark-only |
| `python scripts/bh_flux_calc.py --m-bh-solar <M> --mdot-solar-year <Mdot>` | User-supplied black-hole mass and accretion rate | JSON custom BH mass-flux diagnostic | Implemented; benchmark-only |
| `pytest -q` | Test dependencies + local source tree | Test report with pass/fail summary, including BH flux unit tests | Implemented |

## Status legend
- **Implemented**: command is present and invocable.
- **Data-dependent**: command behavior depends on external/locally provisioned real datasets.
- **Benchmark-only**: command is a diagnostic/reproducibility helper and does not establish a cosmological claim.

## Core/archive boundary recommendation
- Keep archival and historical content immutable for traceability.
- Treat `src/`, `tests/`, `scripts/`, and `data/` reproducibility docs as the **core execution boundary** for scientific validation.
- Treat broad narrative corpora (`newadd/`, `RMR/`, duplicate archives, exploratory notebooks) as **archive/reference boundary** unless promoted with reproducibility metadata.

## BH flux benchmark boundary

The BH flux layer adds a reproducible diagnostic for black-hole mass-flow bookkeeping:

```text
Mdot -> horizon area -> mass flux -> unit-equivalent count rate -> weighted RLL BH index
```

It is intentionally separate from the Pantheon+/LCDM cosmology validation pipeline. It may support benchmark comparison across Sgr A*, M87*, and quasar-scale examples, but it must not be interpreted as proof of RLL cosmology or as a replacement for GR/GRMHD.

> Note: `data/results/model_comparison.json` now includes conservative threshold-based delta interpretation fields (`interpretation_label`, `interpretation_reason`, `thresholds_used`, `claim_boundary`) and does **not** produce automatic cosmological conclusions.