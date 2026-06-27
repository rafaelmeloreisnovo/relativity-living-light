# RLL Photonic Logistic and Plasma Gravity Note

## Purpose

This note preserves the correct naming and scope of Rafael's observation thread:

```text
photonic logistic + plasma gravity
```

The phrase should not be reduced to generic “viscosity” or a vague photonic metaphor. The material already present in the repository contains a stronger structure:

- logistic transition `f(z)`;
- photonic superposition/coherence;
- magnetic modulation;
- plasma contribution;
- local gravitational environments;
- halos, rotation curves and cluster lensing;
- figures and plots created as part of the RLL visual/computational work.

## Authorial provenance

Rafael states that many of the visual materials/graphs were produced by him directly on a mobile phone. This should be treated as authorial provenance of the concept-building process.

For scientific custody, each figure still needs file-level provenance:

- canonical path;
- source data or generating script;
- creation/modification history when available;
- hash;
- claim status;
- whether the figure is conceptual, diagnostic, synthetic, or real-data-derived.

## What already exists in the repository

### 1. Photonic logistic core

The current material already contains the central logistic form:

```text
f(z) = 1 / (1 + exp((z - z_t)/w_t))
```

This is the core of the “photonic logistic” language: a transition function controlling the shift between a coherent/extended behavior and a collapsed/decoherent or matter-like behavior.

In the RLL language, this is not merely a chart. It is the transition operator that tries to encode how a photonic/coherence sector changes with redshift and environment.

### 2. Extended Friedmann-like form

The repository material contains an extended background expression:

```text
E²(a) = Ω_r a⁻⁴
      + Ω_m a⁻³
      + Ω_Λ
      + Ω_s0[f + (1-f)a⁻³]
      + Ω_B0 a⁻⁴
      + Ω_P0 a⁻⁴
```

Interpretive reading:

- `Ω_s0` = photonic superposition/coherence sector;
- `f` = logistic transition gate;
- `Ω_B0` = magnetic contribution/modulator;
- `Ω_P0` = plasma contribution/modulator;
- the `a⁻³` branch behaves matter-like;
- the coherent branch behaves closer to dark-energy-like behavior.

### 3. Plasma gravity / magneto-plasmatic local response

The existing conceptual framework already describes plasma and magnetic fields as coherence modulators, and local gravitational environments as possible triggers for decoherence/collapse.

The more precise RLL reading is:

```text
plasma gravity = effective local gravitational response of a photonic/coherence sector under plasma + magnetic + gravitational environment
```

This is not yet a standard validated physics module. It is a hypothesis seed that needs formalization.

The current repository also has a conceptual figure route for a magneto-plasmatic map in halos/clusters, linking magnetic field, plasma, coherence and local effective gravitational response.

### 4. Existing visual panel

The current book chapter already identifies canonical figure paths and purposes:

- `figs/paper/unified_H_ratio.png` — expansion ratio;
- `figs/paper/unified_mu_residuals.png` — luminosity-distance residuals;
- `figs/paper/unified_fractions.png` — energy fraction evolution;
- `figs/paper/unified_f_and_weff.png` — logistic transition and effective equation of state;
- `figs/paper/unified_growth_fs8.png` — structure growth;
- `figs/paper/rotcurve_NGC_2403.png` — local rotation curve;
- `figs/paper/cluster_lensing_SIS_unified.png` — cluster lensing;
- `figs/conceptual/transition_coerencia_decoerencia.png` — coherence/decoherence transition;
- `figs/conceptual/background_decomposicao_unificada.png` — unified background decomposition;
- `figs/conceptual/mapa_magnetoplasmatico_halos_clusters.png` — magneto-plasmatic halos/clusters map;
- `figs/conceptual/cadeia_observaveis_falsificaveis.png` — falsifiable observables chain.

This confirms that the visual/computational material is part of the RLL body. The remaining task is not to invent it from zero, but to bind it to scripts, data, tests and gates.

## What is still missing

### A. Definition layer

Need to define, in clean terms:

```text
photonic logistic = ?
plasma gravity = ?
magneto-plasmatic response = ?
coherence/decoherence = ?
collapsed photonic branch = ?
```

Each definition must state whether it is:

- literal physical mechanism;
- effective phenomenological model;
- computational analogy;
- visualization language;
- placeholder awaiting derivation.

### B. Equation layer

Need to separate:

1. background expansion equation;
2. local halo/cluster response equation;
3. perturbation/growth equation;
4. plasma/magnetic correction equation;
5. propagation/lensing equation.

Without this separation, one equation may be forced to explain too many scales at once.

### C. Parameter layer

Each parameter needs a table:

| Parameter | Meaning | Unit | Prior | Data constraint | Status |
|---|---|---|---|---|---|
| `Ω_s0` | photonic sector strength | dimensionless | TBD | BAO/SNe/CMB/growth | partial |
| `z_t` | transition redshift | dimensionless | TBD | H(z), SNe, fσ8 | partial |
| `w_t` | transition width | dimensionless | TBD | H(z), SNe, fσ8 | partial |
| `Ω_B0` | magnetic background/correction | dimensionless | TBD | Faraday/CMB/cluster | concept/partial |
| `Ω_P0` | plasma background/correction | dimensionless | TBD | plasma/cluster/CMB | concept/partial |
| `α_B` | magneto-coherent coupling | dimensionless | TBD | Faraday+lensing | concept |
| `β` | power-law index | dimensionless | TBD | inferred | concept |

### D. Data/loader layer

Need loaders for:

- Pantheon+ SNe covariance;
- DESI DR1/DR2 BAO covariance;
- SDSS/BOSS/eBOSS DR16 BAO/RSD;
- fσ8 covariance;
- Planck 2018 or distance-prior/CMB likelihood;
- ACT/Planck lensing;
- Faraday rotation / magnetic field proxy if magneto-plasmatic claim is tested;
- SPARC or other rotation curve data if local halo claim is tested.

### E. Figure provenance layer

Each graph should be classified:

```text
conceptual
synthetic_model
real_data_overlay
diagnostic
posterior/inference
```

and should point to:

- generating script/notebook;
- input data;
- output path;
- hash;
- claim boundary.

## Correct claim language

Allowed now:

```text
RLL already contains a photonic-logistic/plasma-gravity concept thread with equations, conceptual figures and observables.
```

Allowed now:

```text
This thread is not yet fully promoted into the current rigorous real-data pipeline.
```

Allowed now:

```text
The current H(z)+BAO comparison tests only a limited slice of the broader RLL form.
```

Not allowed yet:

```text
Photonic logistic/plasma gravity is validated as physical cosmology.
```

Not allowed yet:

```text
The existing figures prove the model.
```

## Engineering path

The right path is:

```text
raw Rafael observation
-> canonical term: photonic logistic / plasma gravity
-> definition table
-> equation separation
-> parameter table
-> figure provenance
-> loader/test/gate
-> claim report
```

## Next concrete files

Recommended files to add next:

1. `docs/RLL_PHOTONIC_LOGISTIC_GLOSSARY.md`
2. `docs/RLL_PLASMA_GRAVITY_FORMALIZATION.md`
3. `docs/RLL_FIGURE_PROVENANCE_LEDGER.md`
4. `scripts/emit_rll_figure_provenance.py`
5. `data/results/rll_figure_provenance.json`

## Close

`F_ok`: the photonic logistic and plasma-gravity material exists as concept, equations and figures.  
`F_gap`: it is not yet fully bound to loaders, figure provenance, perturbation equations and formal claim gates.  
`F_next`: create the glossary + formalization + figure provenance ledger, then connect those to the real-data master registry.
