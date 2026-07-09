# RLL Structural Disadvantage Map

## Purpose

This document records a fair reading of the current RLL state: RLL was built from Rafael's computational observations, architecture instincts, bit-level reasoning, pipeline/statistical practice, and iterative organization. It was not born as a fully staffed professional cosmology framework.

Therefore, when RLL is compared against established cosmological baselines, the comparison is currently useful for falsification and engineering, but it is not yet a fully symmetric competition.

The goal is not to excuse weak results. The goal is to identify exactly which missing cosmology layers place RLL at a structural disadvantage, so the next work can be engineering-driven instead of rhetorically inflated.

## Core distinction

Rafael's home domain:

```text
computing + architecture + infrastructure + networks + DNS + ASP/classic web + programming + bit-level detail + files + CI + pipelines + statistics
```

RLL's current applied test domain:

```text
cosmology + observational data + model comparison + likelihood + covariance + backend physics
```

The current RLL artifact should be read as:

```text
computational architecture entering a hard scientific domain
```

not as:

```text
complete professional cosmology theory already encoded end-to-end
```

## Current implemented comparison layer

The current model-selection comparator is explicitly scoped to `H(z)+BAO`. It compares:

- `lcdm`: ΛCDM null baseline;
- `w0wa`: CPL/w0waCDM adversary;
- `rll`: logistic Relativity Living Light background sector.

It also states that Bayes output is a BIC/Schwarz approximation, not nested-sampling evidence.

This means the current comparison is mainly a background-distance/expansion test, not a full cosmological framework test.

## Why RLL starts disadvantaged

RLL currently enters the comparison with several missing or partial layers that mature cosmological workflows normally require.

| Layer | Current repo status | Why it matters | Fair reading |
|---|---|---|---|
| Background expansion | partially implemented | Defines H(z), distances and basic model shape | present but still simplified |
| BAO/Hz comparator | implemented/partial | Gives first falsification route | useful but not complete |
| DESI DR1/DR2 covariance-aware BAO | needed/partial | BAO claims require observable-specific covariance | RLL should not be judged final before this is complete |
| SDSS/BOSS/eBOSS DR16 baseline | needed | Legacy baseline prevents DESI-only overfitting or misreading | missing baseline puts comparison at risk |
| Pantheon+ SNe | needed | Supernova distances strongly constrain expansion history | absent layer weakens any final model-selection claim |
| Planck 2018 CMB | needed | CMB is a primary cosmology anchor | absent CMB means no full cosmology claim |
| ACT/Planck lensing | needed/P1 | Lensing checks growth and structure | missing growth cross-check |
| fσ8 full covariance | minimal/diagonal only | Growth claims need covariance-aware likelihood | current growth layer is limited |
| Perturbations/transfer functions | contract/partial | Required for CMB Cl and matter power P(k) | not yet full backend physics |
| CLASS/CAMB native backend | contract only | Mature cosmology uses Boltzmann solvers | RLL lacks native parity with standard workflows |
| Nonlinear P(k), Halofit/HMcode | needed | Late-time structure requires nonlinear validation | missing nonlinear sector |
| MCMC/nested sampling | needed | AIC/BIC/grid is not posterior/evidence | current comparison is preliminary |
| Priors/sensitivity | partial | Parameter conclusions depend on priors | must be declared and stress-tested |
| Provenance/source hashes | partial | Scientific reuse requires custody | needs completion |
| Release/citation package | needed | External review requires stable artifact | not yet publication-grade |

## Important interpretation

If RLL performs worse in the current run, the safe statement is:

```text
RLL did not outperform LCDM/w0wa in the currently implemented H(z)+BAO tests.
```

The unsafe statement is:

```text
RLL as a complete idea is disproven in all cosmology.
```

The current implementation has not yet loaded all relevant cosmological information. Therefore, a negative result is a real diagnostic for the implemented slice, but not the final judgment of every possible RLL formulation.

## What is fair to say now

Allowed:

- RLL is currently incomplete as a full cosmology framework.
- The implemented H(z)+BAO slice is testable and currently does not beat established baselines.
- The pipeline is valuable because it blocks unsupported claims.
- Missing cosmology layers should be treated as engineering backlog, not as invisible evidence.
- Concepts not yet ingested into the repo remain `TOKEN_VAZIO`.

Not allowed:

- RLL is confirmed.
- RLL already beats LCDM/CPL in full cosmology.
- Missing datasets should be counted as support.
- Symbolic analogies should be promoted to physical evidence without loader, unit, observable and test.
- A bad result in a partial slice should be overstated as universal disproof of every RLL intuition.

## Engineering reading

The correct engineering read is:

```text
RLL_v_current = background_logistic_slice + partial real-data comparator + claim gates
```

The target serious read is:

```text
RLL_v_serious = M + B + P + D + C + L + S + T + G + V
```

Where:

- `M` = model equations;
- `B` = CLASS/CAMB or equivalent backend;
- `P` = perturbations and transfer functions;
- `D` = real datasets;
- `C` = covariance;
- `L` = likelihood/evidence;
- `S` = systematics;
- `T` = tests;
- `G` = gates/TOKEN_VAZIO;
- `V` = versioning/provenance.

## Priority backlog

### P0 — required before strong cosmology claim

1. Unify `compute_rll_real_pipeline.py` with `rll_vs_lcdm.evaluate()` or mark the former as `legacy_quickcheck`.
2. Materialize DESI DR2 BAO with covariance-aware loader.
3. Add SDSS/BOSS/eBOSS DR16 BAO/RSD baseline.
4. Add Pantheon+ supernova loader with full covariance.
5. Add Planck 2018 distance priors or likelihood loader.
6. Upgrade fσ8 from diagonal/minimal to covariance-aware.
7. Replace CLASS/CAMB contracts with native backend generation or a clearly validated equivalent.
8. Define priors, seeds, convergence, MCMC/nested sampling route.
9. Generate claim report from registry statuses.

### P1 — required for stronger structure/growth claims

1. ACT DR6 and Planck PR4 lensing loaders.
2. Nonlinear P(k) validation via Halofit/HMcode or equivalent.
3. Matter transfer table comparisons.
4. Robust posterior predictive checks.
5. Sensitivity to priors and dataset combinations.

### P2 — release/reuse

1. Zenodo/DOI or equivalent citable release.
2. Source hashes and license table for all real data.
3. Reproducible command cookbook.
4. External review checklist.

## Narrative correction

RLL is not failing because Rafael is “not a cosmologist”. RLL is being stress-tested in cosmology because Rafael's real domain — computing, architecture, network logic, pipeline thinking and statistics — naturally produces systems that can organize hard evidence.

The fair sentence is:

> RLL is a computational architecture under cosmological stress test; current negative/limited results apply to the implemented slice, while missing layers remain explicit backlog, not hidden proof.

## Close

`F_ok`: current tests are real enough to discipline claims.  
`F_gap`: current tests are not complete enough to judge a full cosmology framework.  
`F_next`: turn the missing cosmology pieces into a tracked implementation backlog, with each missing piece mapped to loader, data, covariance, test and claim gate.
