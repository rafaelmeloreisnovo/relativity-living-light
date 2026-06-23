# RLL - w0wa implementation ledger

Data: 2026-06-23
Repo: `instituto-Rafael/relativity-living-light`

## Implemented

- `rll_vs_lcdm.py` now evaluates three separated models: `lcdm`, `w0wa`, and `rll`.
- `rll` uses the logistic background sector:

```text
E2(z) = Omega_m(1+z)^3 + Omega_Lambda + Omega_s0[f(z)+(1-f(z))(1+z)^3]
f(z) = 1/(1+exp((z-z_t)/w_t))
Omega_Lambda = 1 - Omega_m - Omega_s0
```

- `src/rll/cli.py` now forwards the real-data command to the model-selection comparator.
- `NEXT_RLL_VALIDATION_STEP.md` now documents the w0wa command path.
- `tests/test_rll_model_selection.py` covers the logistic midpoint, model separation, and BIC helper.

## Commands

```bash
python rll_vs_lcdm.py --adversary both --with-bayes --with-growth
rll run --data real --model rll --adversary w0waCDM --with-bayes --with-growth
```

## Boundary

This is a minimum executable comparison layer. It does not replace robust parameter optimization, full covariance treatment, full Bayesian evidence, or the future growth-structure module.

Fields intentionally left for later work are marked in outputs as `TOKEN_VAZIO`.
