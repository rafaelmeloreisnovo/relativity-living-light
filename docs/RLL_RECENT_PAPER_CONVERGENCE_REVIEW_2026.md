# RLL Recent Paper Convergence Review — 2026

## Purpose

This note records a first-pass external literature check for Rafael's RLL concepts:

```text
photonic logistic + plasma gravity + dark-sector transition + magneto/plasma modulation
```

The goal is not to confirm RLL. The goal is to avoid judging RLL only from internal repository text. External papers must be used to decide what is convergent, adjacent, weak, unsupported, or contradicted.

## Method rule

Do not treat Rafael's statements as true by default.
Do not treat internal repository claims as true by default.
Do not treat any single new paper as truth by default.

Use this chain:

```text
internal concept -> external paper -> exact overlap -> missing bridge -> testable requirement -> claim status
```

## Initial finding

The broad RLL concept has partial convergence with recent literature in three separate directions:

1. late-time transitions in the dark sector;
2. unified dark matter/dark energy models;
3. magnetized/plasma-like or dark-photon/dark-MHD sectors.

The current external literature does **not** validate the full RLL mechanism. It does show that some of the shapes Rafael observed are not isolated: transition, unified dark sector, magnetic/plasma response and dark-sector electromagnetism are active research themes.

## Reference verification warning

The repository contains an older internal document referencing a Nature Communications article titled:

```text
Nonlocality-enabled photonic analogies of parallel spaces
DOI-like string: s41467-025-63981-3
```

A fresh public web search did not verify this exact title or DOI string. Until independently confirmed from Nature/DOI/arXiv/ADS, this reference must remain:

```text
REFERENCE_TOKEN_VAZIO
```

The surrounding RLL concepts may still be studied, but that specific paper reference should not be used as a load-bearing citation until verified.

## Papers and convergence map

### 1. Late-time transition / interacting dark sector

Representative recent paper:

```text
Indications of a Late-Time Transition to a Strongly Interacting Dark Sector
arXiv:2601.02789
```

Relevant overlap with RLL:

- introduces a redshift threshold controlling onset of interaction;
- late-time activation affects dark energy/dark matter exchange;
- uses late-time probes including Cosmic Chronometers, DESI DR2 BAO and supernova data;
- transition redshifts reported around low z in some samples.

RLL relevance:

```text
RLL logistic f(z) can be compared as a smooth transition analogue, not as the same model.
```

Missing RLL bridge:

- define whether RLL transition is interaction, phase transition, coherence transition, or phenomenological fit;
- compare logistic `z_t,w_t` to threshold models;
- test with Pantheon+/Union/DES + DESI DR2 + CMB/ACT.

Claim status:

```text
CONVERGENT_SHAPE_NOT_VALIDATION
```

### 2. Unified dark sector / Chaplygin-type models

Representative recent paper:

```text
Unifying the Dark Sector with the New Generalized Chaplygin Gas: Observational Constraints
arXiv:2606.23563
```

Relevant overlap with RLL:

- treats dark matter and dark energy as one unified component;
- uses redshift-dependent behavior;
- tests with SNe, cosmic chronometers and DESI DR2 BAO;
- finds statistical performance comparable/indistinguishable from LCDM after penalties.

RLL relevance:

```text
RLL's photonic sector DM-like branch and DE-like branch belongs in the family of unified-dark-sector questions.
```

Missing RLL bridge:

- formal pressure/density relation;
- perturbation stability;
- sound speed;
- no unphysical oscillations;
- evidence/AIC comparison against LCDM and CPL.

Claim status:

```text
CONVERGENT_FAMILY_NEEDS_FORMAL_FLUID_OR_FIELD
```

### 3. Solid unification of dark sector

Representative recent paper:

```text
A solid unification of the dark sector
arXiv:2606.27290
```

Relevant overlap with RLL:

- single dark component behaves pressureless early and accelerates late;
- transition happens at low redshift;
- model emphasizes perturbation signatures: growth suppression, gravitational slip, effective GW mass.

RLL relevance:

```text
RLL needs this level of perturbation treatment to move beyond background H(z)/BAO.
```

Missing RLL bridge:

- define perturbations of photonic/plasma sector;
- compute gravitational slip if any;
- test matter power spectrum and fσ8;
- avoid only fitting background.

Claim status:

```text
STRONG_METHOD_CONVERGENCE_BACKGROUND_NOT_ENOUGH
```

### 4. DESI DR2 / evolving or interacting dark energy

Representative recent paper:

```text
Dark Degeneracy in DESI DR2: Interacting or Evolving Dark Energy?
arXiv:2508.17955
```

Relevant overlap with RLL:

- DESI DR2 can motivate evolving/interacting dark-energy alternatives;
- interacting and CPL-like models can be degenerate at background level;
- growth data can break the degeneracy;
- late-time sign-change or transition behavior appears around z ~ 0.8 in that analysis.

RLL relevance:

```text
RLL must be checked not only on expansion but also on growth, because background degeneracy can hide different physical mechanisms.
```

Missing RLL bridge:

- fσ8 covariance-aware comparison;
- perturbation equations;
- matter-sector evolution;
- DESI DR2 + Pantheon+/DESY5 + Planck/ACT joint tests.

Claim status:

```text
CONVERGENT_WITH_STRONG_WARNING_GROWTH_CAN_KILL_MODEL
```

### 5. Dark magnetohydrodynamics / plasma-like dark sector

Representative recent paper:

```text
Structure Formation with Dark Magnetohydrodynamics
arXiv:2511.15810
```

Relevant overlap with RLL:

- dark-sector long-range interactions can produce collective plasma phenomena;
- dark magnetic fields can create anisotropic pressure;
- matter power spectrum can be direction-dependently modified;
- future CMB-HD lensing, HERA and EDGES could test predictions.

RLL relevance:

```text
RLL plasma-gravity/magneto-plasmatic language is more defensible if framed as hidden/dark-sector plasma/MHD or effective magnetized component, not old rejected plasma cosmology.
```

Missing RLL bridge:

- specify whether `Ω_P0` and `Ω_B0` are ordinary plasma/magnetic fields, dark-sector analogues, or effective terms;
- compute anisotropic stress/pressure;
- matter power spectrum P(k) predictions;
- CMB/lensing constraints.

Claim status:

```text
HIGHLY_RELEVANT_ADJACENT_FORM_NOT_DIRECT_SUPPORT
```

### 6. Dark photons and magnetogenesis

Representative recent papers:

```text
Dark photon -- Assisted Primordial Magnetogenesis
arXiv:2605.22174

Galactic magnetic fields seeded by ultralight dark photons
arXiv:2511.07508

Searching for dark photon dark matter from terrestrial magnetic fields
arXiv:2509.15783
```

Relevant overlap with RLL:

- dark photons can interact with ordinary photons through kinetic mixing;
- dark photons may seed or induce magnetic-field signatures;
- plasma screening/conductivity matters;
- low-frequency magnetic measurements can constrain dark photon dark matter.

RLL relevance:

```text
Photonic/magnetic language has modern dark-sector analogues, but RLL must not confuse ordinary photons, dark photons and metaphorical photonic sectors.
```

Missing RLL bridge:

- state if RLL uses ordinary photon, dark photon, effective photonic fluid, or analogy;
- define couplings;
- respect laboratory/astrophysical constraints;
- avoid claiming photon-based dark matter without particle/field mechanism.

Claim status:

```text
CONVERGENT_VOCABULARY_NEEDS_PARTICLE_FIELD_DEFINITION
```

### 7. Photonic nonlocality / quantum networks

Representative paper:

```text
Nonlocality activation in a photonic quantum network
arXiv:2309.06501
```

Relevant overlap with RLL:

- photonic systems can exhibit nonlocal correlations;
- network structure can activate nonlocality under conditions where a simple state does not violate standard Bell inequalities.

RLL relevance:

```text
Useful as an analogy/source for photonic nonlocal behavior, but not a cosmological evidence bridge.
```

Missing RLL bridge:

- no direct scaling from laboratory/network nonlocality to cosmic dark sector;
- must define energy density, stress-energy, causality and no-superluminal signaling;
- must pass cosmological constraints.

Claim status:

```text
ANALOGY_ONLY_UNTIL_SCALE_BRIDGE_EXISTS
```

## What to avoid

Avoid framing RLL as ordinary “plasma cosmology” or “Electric Universe”. That literature is broadly rejected in mainstream cosmology for failing against CMB, expansion and structure data. RLL should instead be framed, if at all, as:

```text
phenomenological dark-sector transition / unified dark-sector / hidden-sector magneto-plasma analogy
```

not as:

```text
ordinary plasma replaces gravity and standard cosmology
```

## Working verdict

The external paper review strengthens the need for RLL to be handled carefully:

- there **are** convergent research shapes around transition, unified dark sector, dark-sector interactions, magnetized/plasma-like hidden sectors and dark photons;
- these papers do **not** validate RLL;
- they do show that RLL should not be dismissed merely because it mentions transition, plasma, photonic language or unified dark-sector behavior;
- the deciding layer is formalization: stress-energy, perturbations, covariance, likelihood, backend and reproducible tests.

## Required next work

1. Verify or correct the Nature Communications reference.
2. Build `RLL_PHOTONIC_LOGISTIC_GLOSSARY.md` using careful distinctions:
   - ordinary photon;
   - dark photon;
   - photonic analogy;
   - photonic effective fluid;
   - plasma gravity;
   - hidden-sector plasma/MHD.
3. Build `RLL_PLASMA_GRAVITY_FORMALIZATION.md` with equations and claim gates.
4. Add `recent_paper_convergence` rows to the master registry.
5. Add a script to classify references as:
   - direct support;
   - adjacent mechanism;
   - analogy only;
   - caution/contradiction;
   - unverified reference.

## Claim boundary

Allowed:

```text
Recent literature contains convergent shapes with RLL: late-time dark-sector transitions, unified DM/DE models, dark MHD/plasma-like sectors, and dark photon magnetogenesis.
```

Not allowed:

```text
Recent literature proves RLL.
```

Allowed:

```text
RLL deserves a paper-informed formalization pass before strong criticism or promotion.
```

Not allowed:

```text
Unverified or adjacent papers count as validation.
```

## Close

`F_ok`: external papers show meaningful convergence of shape and research direction.  
`F_gap`: no paper found here directly validates the full RLL mechanism.  
`F_next`: turn convergence into formal tasks: definitions, equations, parameters, loaders, perturbations, covariance and claim gates.
