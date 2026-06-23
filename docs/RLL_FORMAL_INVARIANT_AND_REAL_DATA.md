# RLL formal invariant and real-data rigor map

Status date: 2026-06-23

## Purpose

This document defines the invariant content of the RLL work: what must remain true across papers, code, results, market discussion and public claims.

## Formal invariant

The RLL content invariant is:

```text
I_RLL = (M, B, P, D, C, L, S, T, G, V)
```

Where:

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

A public or academic claim is allowed only when the relevant subset of `I_RLL` is present and reproducible.

## Claim rule

```text
claim_allowed = model_defined AND data_loaded AND covariance_handled AND likelihood_defined AND tests_passed AND gate_not_TOKEN_VAZIO
```

If any required part is missing:

```text
claim_status = TOKEN_VAZIO
```

## What is implemented now

| Element | Status | Repository evidence |
|---|---|---|
| Background RLL | implemented | `src/rll/class_rll_background.c` |
| f sigma 8 minimal real CSV | implemented | `data/real/cosmology/fsigma8_growth.csv` |
| Growth chi2 | implemented | `scripts/check_rll_growth.py` |
| Linear perturbation kernel | implemented | `src/rll/rll_perturbation_kernel.py` |
| Transfer bridge | contract | `src/rll/rll_transfer_bridge_contract.json` |
| CLASS/CAMB handoff | contract | `src/rll/class_transfer_adapter_contract.json` |
| Progress/value matrix | implemented | `docs/RLL_PROGRESS_VALUE_MATRIX.md` |
| Real data requirements | implemented | `data/real/cosmology/RLL_REAL_DATA_REQUIREMENTS.csv` |

## Serious data still required

| Dataset class | Required item | Why |
|---|---|---|
| BAO | DESI DR1/DR2 full covariance | distance constraints and dark-energy evolution tests |
| BAO/RSD | SDSS BOSS/eBOSS DR16 covariances | legacy benchmark and growth comparison |
| SNe Ia | Pantheon+ data and covariance | low-redshift distance ladder and dark-energy constraints |
| CMB | Planck 2018 likelihood or distance priors | standard CMB baseline |
| CMB lensing | ACT DR6 and Planck PR4 lensing covariances | growth and lensing cross-check |
| Growth | f sigma 8 full covariance | replace diagonal-only screening |
| Nonlinear matter | Halofit/HMcode backend validation | nonlinear P(k) gate |
| Sampling | MCMC/nested sampling chains | evidence and posterior robustness |
| Provenance | data hashes and licenses | chain of custody |

## Tools required

| Tool class | Examples | Purpose |
|---|---|---|
| Boltzmann backend | CLASS, CAMB, classy, camb | CMB Cl and matter transfer functions |
| Sampler | Cobaya, MontePython, emcee, dynesty | posterior and evidence |
| Data processing | Python, numpy/scipy optional, CSV/JSON validators | likelihood and reproducibility |
| CI | GitHub Actions, pytest | regression and reproducibility gates |
| Provenance | sha256, Zenodo, release tags | citable package and custody |

## Academic rigor gates

1. Full covariance replaces diagonal-only approximations.
2. RLL is compared against LCDM, w0wa/CPL and other relevant alternatives.
3. Priors are declared and sensitivity-tested.
4. Results include negative cases and collapse-to-LCDM cases.
5. CMB Cl and P(k) are backend-generated, not hand-waved.
6. Public claims preserve TOKEN_VAZIO when backend/data are missing.

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

1. Add full covariance files or loaders for DESI, SDSS, Pantheon+, Planck and ACT.
2. Replace transfer contracts with native CLASS/CAMB transfer-table generation.
3. Run CMB Cl and P(k) comparisons.
4. Run MCMC or nested sampling.
5. Release a tagged, citable package with hashes and data provenance.
