# RLL Form Gap Map — What is Missing in the Formal Shape

## Purpose

This document answers a narrow question: what is missing in the *form* of RLL so that Rafael's observed/computational construction can be compared more fairly against professional cosmology models?

RLL was not built by reading a full cosmology textbook and encoding every standard term. It was assembled from observation, computational intuition, bit-level/pipeline reasoning, statistics, conversations, partial concepts, and iterative experiments.

That origin matters. The current RLL implementation is not a fully populated cosmological model. It is a computational architecture with a cosmological hypothesis layer that still needs formal completion.

## Key correction

The current negative or limited results should be read as:

```text
The implemented RLL slice did not outperform standard baselines in the currently loaded tests.
```

They should not be read as:

```text
Every Rafael observation about light, photonic behavior, transition, plasma, magnetism or coherence is disproven.
```

The missing concepts are not evidence in favor of RLL. They are also not evidence against RLL. They are `TOKEN_VAZIO` until written, formalized, loaded, tested and gated.

## Current RLL form

The current operational form is approximately:

```text
RLL_current = H(z)/BAO background comparator
            + logistic transition f(z)
            + Omega_s0 sector
            + partial real-data gates
            + symbolic/computational narrative
```

The code-level comparator is scoped to:

```text
H(z) + BAO + AIC/BIC/BIC-approx Bayes
```

This is a useful first falsification slice, but not a complete cosmological theory.

## Older photonic observation thread

There is an older repository trail connecting RLL with photonic nonlocality and cosmological implications. That thread included ideas such as:

- photonic nonlocality;
- photonic superposition;
- dark sector interpretation;
- magnetic modulation;
- plasma modulation;
- transition function;
- observational predictions for H(z), SNe, fσ8, rotation curves and lensing.

However, this older photonic thread is not yet fully integrated into the current rigorous RLL pipeline as a validated physics module.

Safe reading:

```text
photonic observation thread = concept source / hypothesis seed
```

Unsafe reading:

```text
photonic observation thread = already validated cosmological mechanism
```

## What is missing in the form

### 1. Microphysical definition

Missing question:

```text
What exactly is the physical entity represented by Omega_s0?
```

Needed:

- field, fluid or effective component definition;
- stress-energy tensor or effective density/pressure map;
- equation of state derivation;
- unit consistency;
- relation to photons, coherence, plasma, magnetism or nonlocality;
- boundary between metaphor and physics.

Current status:

```text
partially parameterized, not microphysically closed
```

### 2. Full Friedmann-sector form

The older photonic notes contained terms like radiation, matter, Lambda, superposition, magnetic and plasma sectors. The current comparator mainly carries a simplified logistic background sector.

Needed:

```text
E²(a) = radiation + baryons + cold dark matter/effective matter + Lambda/effective DE + RLL sector + optional plasma/magnetic corrections
```

For each term:

- symbol;
- unit;
- scaling with scale factor `a`;
- prior range;
- physical meaning;
- whether it is real physics, effective fit or symbolic placeholder;
- dataset that constrains it.

### 3. Baryons, radiation and neutrinos

Professional cosmology does not compare only with a generic matter term. It tracks baryons, photons/radiation, neutrinos, matter density, sound horizon and related early-universe quantities.

Needed:

- Omega_b;
- Omega_cdm or effective replacement;
- Omega_r;
- N_eff;
- neutrino mass assumptions;
- sound horizon `r_d` derivation or imported prior;
- CMB compatibility gate.

Without this, the RLL form is forced into a simplified background comparison.

### 4. Perturbations and growth

A full cosmological model must say not only how the universe expands, but how structures grow.

Needed:

- delta_m evolution;
- growth factor D(a);
- f = d ln D / d ln a;
- fσ8(z);
- transfer functions;
- matter power spectrum P(k,z);
- lensing source terms;
- stability conditions;
- connection between RLL sector and gravitational clustering.

Current status:

```text
growth/perturbation pieces exist as partial/contract layers, not complete backend parity
```

### 5. CMB form

CMB is a central cosmology anchor. RLL cannot make full cosmology claims while CMB is absent or only represented by placeholders/distance priors.

Needed:

- Planck 2018 likelihood or distance-prior loader;
- CMB acoustic scale consistency;
- Cl_TT, Cl_TE, Cl_EE if backend route exists;
- lensing potential where applicable;
- early-universe compatibility statement;
- clear TOKEN_VAZIO if not implemented.

### 6. Supernova form

The current run is not a full distance-ladder comparison without Pantheon+ covariance.

Needed:

- Pantheon+ data loader;
- covariance matrix;
- nuisance parameters;
- absolute magnitude/H0 handling;
- residual plots;
- joint SNe + BAO + Hz comparison.

### 7. BAO/RSD covariance form

BAO is not just one number per redshift. Professional comparison needs observables and covariance.

Needed:

- DM/rd;
- DH/rd;
- DV/rd;
- covariance blocks;
- DESI DR1/DR2 loaders;
- SDSS/BOSS/eBOSS DR16 baseline;
- RSD/fσ8 coupling where available.

### 8. Plasma/magnetic/photon bridge

If Rafael's observed “photonic viscosity / photonic coherence / photonic nonlocality” intuition is part of RLL, the bridge must be formalized.

Needed:

- define the observed phenomenon in original words;
- map possible technical translations: photonic nonlocality, effective viscosity, optical coherence, plasma interaction, magnetic-field modulation, Hall/EM analogy, or another precise mechanism;
- define what is literal and what is metaphor;
- state whether the effect modifies background expansion, perturbations, lensing, radiation propagation, or only acts as analogy;
- propose at least one computable observable.

Until then:

```text
photonic bridge = TOKEN_VAZIO / concept seed
```

### 9. Likelihood and sampling form

AIC/BIC/grid scans are useful, but professional cosmology normally requires posterior exploration.

Needed:

- priors;
- parameter bounds;
- MCMC or nested sampling;
- chain convergence;
- posterior plots;
- evidence or model comparison with declared method;
- sensitivity to prior choices;
- negative-result preservation.

### 10. Systematics form

Professional datasets include systematics that can dominate interpretation.

Needed:

- survey calibration;
- covariance provenance;
- nuisance parameters;
- nonlinear corrections;
- selection effects;
- lensing/systematic corrections;
- dataset compatibility checks.

### 11. Provenance form

Every real source must have custody.

Needed:

- source URL or bibliographic ID;
- license/access condition;
- downloaded/source date;
- SHA256;
- loader script;
- validation script;
- claim gate.

### 12. Claim-language form

Every result must map to allowed language.

Needed categories:

```text
implemented_and_tested
partial_diagnostic
concept_seed
TOKEN_VAZIO
blocked_claim
```

This prevents a concept from jumping directly from observation to public scientific claim.

## What the standard models already have implicitly

ΛCDM/CPL/w0wa are not just equations. They arrive with a whole ecosystem:

- standard parameters;
- mature datasets;
- covariances;
- Boltzmann solvers;
- perturbation theory;
- priors;
- sampling tools;
- public likelihoods;
- decades of debugging;
- known failure modes;
- known degeneracies.

RLL does not yet carry that entire ecosystem. That is the brutal difference.

## Fair comparison ladder

### Level 0 — concept seed

```text
observation / analogy / intuition
```

Status: not comparable as physics.

### Level 1 — symbolic/math form

```text
symbols + equations + declared assumptions
```

Status: readable, not yet validated.

### Level 2 — background model

```text
H(z), distances, BAO/SNe hooks
```

Status: first falsification.

### Level 3 — perturbation model

```text
growth, transfer functions, P(k), fσ8
```

Status: structure test.

### Level 4 — backend model

```text
CLASS/CAMB or equivalent native solver
```

Status: serious cosmology implementation.

### Level 5 — likelihood model

```text
SNe + BAO + Hz + CMB + lensing + covariance + MCMC/nested sampling
```

Status: real model comparison.

### Level 6 — release/review model

```text
versioned package + reproducibility + external review
```

Status: publication-grade artifact.

Current RLL sits between Level 1 and Level 2, with partial Level 3/4 contracts and some real-data gates.

## Immediate form work

P0 actions:

1. Write `RLL_PHOTONIC_OBSERVATION_NOTE.md` preserving Rafael's raw observation language.
2. Translate that note into a technical glossary: photon/coherence/viscosity/plasma/magnetism/nonlocality.
3. Decide what the photonic term changes: background, perturbations, lensing, propagation or analogy only.
4. Define RLL's full `E²(a)` with all active and inactive terms.
5. Create a parameter table with units, priors, status and dataset constraints.
6. Connect DESI/Pantheon/Planck/fσ8 loaders to the master registry.
7. Mark all missing physics as `TOKEN_VAZIO`, not as proof.
8. Generate a claim report that distinguishes implemented result from unimplemented concept.

## Short conclusion

Rafael's point is correct: the current RLL form lacks several pieces that professional cosmology models already include by default. That can create a large practical disadvantage.

But the right response is not to claim victory from missing pieces. The right response is to convert every missing piece into a formal engineering object:

```text
observation -> definition -> equation -> parameter -> loader -> test -> gate -> claim
```

`F_ok`: RLL has a real computational skeleton and a photonic/conceptual seed.  
`F_gap`: the formal cosmology shape is incomplete.  
`F_next`: write the photonic observation note and attach each missing cosmology layer to the master registry.
