# RLL formal invariant and real-data rigor map

Status date: 2026-06-23

## Master registry

The authoritative real-data registry is now:

```text
data/real/cosmology/RLL_ALL_REAL_DATA_MASTER.csv
```

The detailed explanation is:

```text
docs/RLL_ALL_REAL_DATA_MASTER.md
```

Older requirement files are secondary. If there is disagreement, the master registry wins.

## Purpose

This document defines the invariant content of the RLL work: what must remain true across papers, code, results, market discussion and public claims.

## Formal invariant

```text
I_RLL = (M, B, P, D, C, L, S, T, G, V)
```

| Symbol | Meaning | Required content |
|---|---|---|
| M | model equations | exact background equations, parameters, priors |
| B | backend | CLASS/CAMB or equivalent Boltzmann integration path |
| P | perturbations | growth equation, transfer functions, CMB sources |
| D | real data | Hz, BAO, SNe, f sigma 8, CMB, lensing |
| C | covariance | full covariance or explicit diagonal-only disclaimer |
| L | likelihood | chi2/loglike, AIC/BIC/evidence when applicable |
| S | systematics | survey systematics, calibration, nonlinear corrections |
| T | tests | unit tests, regression tests, reproducibility commands |
| G | gates | claim gates, TOKEN_VAZIO, negative-result handling |
| V | versioning | commits, data hashes, source dates, release tags |

## Claim rule

```text
claim_allowed = model_defined AND data_loaded AND covariance_handled AND likelihood_defined AND tests_passed AND gate_not_TOKEN_VAZIO
```

If any required part is missing:

```text
claim_status = TOKEN_VAZIO
```

## Current implemented stack

| Element | Status | Repository evidence |
|---|---|---|
| Background RLL | implemented | `src/rll/class_rll_background.c` |
| f sigma 8 minimal real CSV | implemented | `data/real/cosmology/fsigma8_growth.csv` |
| Growth chi2 | implemented | `scripts/check_rll_growth.py` |
| Linear perturbation kernel | implemented | `src/rll/rll_perturbation_kernel.py` |
| Transfer bridge | contract | `src/rll/rll_transfer_bridge_contract.json` |
| CLASS/CAMB handoff | contract | `src/rll/class_transfer_adapter_contract.json` |
| Progress/value matrix | implemented | `docs/RLL_PROGRESS_VALUE_MATRIX.md` |
| All real data master | implemented | `data/real/cosmology/RLL_ALL_REAL_DATA_MASTER.csv` |

## Serious data still required

Do not maintain this list manually here. Use the master registry:

```text
data/real/cosmology/RLL_ALL_REAL_DATA_MASTER.csv
```

That file includes existing assets, PR #385, DESI DR1/DR2, SDSS/eBOSS DR16, Pantheon+, Planck 2018, ACT DR6, Planck PR4, f sigma 8 covariance, CLASS/CAMB native backend, nonlinear validation, sampling, provenance and release gates.

## Academic rigor gates

1. Full covariance replaces diagonal-only approximations.
2. RLL is compared against LCDM, w0wa/CPL and other relevant alternatives.
3. Priors are declared and sensitivity-tested.
4. Results include negative cases and collapse-to-LCDM cases.
5. CMB Cl and P(k) are backend-generated, not hand-waved.
6. Public claims preserve TOKEN_VAZIO when backend/data are missing.
7. Every dataset/backend mentioned in chat or docs must exist in the master registry.

## Market rigor gates

1. No financial valuation without users, revenue, adoption or independent benchmark.
2. Market value may be discussed only as route/potential until validation.
3. Software value requires installable package, docs, tests and examples.
4. Consulting/IP value requires reproducible performance and clear ownership/provenance.
5. Education value can be packaged earlier because the TOKEN_VAZIO method is already useful.

## Current invariant reading

```text
RLL is currently a reproducible research artifact with real-data falsification gates and growing backend structure.
RLL is not yet a confirmed cosmological theory.
RLL is not yet a market-valued product.
```

## Next required actions

1. Resolve or extract PR #385.
2. Materialize DESI DR2 BAO and Cobaya files.
3. Add DESI DR1, SDSS/eBOSS DR16, Pantheon+, Planck and ACT loaders with covariance.
4. Upgrade f sigma 8 from diagonal-only to covariance-aware.
5. Replace transfer contracts with native CLASS/CAMB transfer-table generation.
6. Run MCMC or nested sampling.
7. Release a tagged, citable package with hashes and data provenance.
