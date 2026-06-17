# Gravitational Residual Memory and Compact Gaps

Status: hypothesis boundary / model-gap ledger  
Scope: RLL structure formation, disrupted galaxies, compact remnants, gravitational residuals  
Claim level: conservative; no replacement claim for GR, LCDM, stellar evolution, or compact-object theory

---

## 1. Purpose

This document records two related modeling gaps that should be treated explicitly in the RLL repository:

1. **Residual gravitational structures**: cases where the visible morphology of a galaxy or bound system is destroyed, but a gravitational signature remains through residual mass, dark matter halo structure, compact remnants, stellar streams, lensing, or orbital memory.
2. **Compact-remnant transition gaps**: cases where the boundary between neutron stars, mass-gap objects, and black holes is not a single sharp number, but a transition region dependent on mass, equation of state, fallback, metallicity, rotation, binarity, and formation channel.

These gaps are useful to RLL only if treated as **scale-indexed astrophysical modules**, not as direct replacements for the cosmological background equation.

---

## 2. Core boundary

RLL must separate:

```text
cosmological background
→ structure formation
→ bound systems
→ disrupted or residual structures
→ compact-remnant formation
→ observable catalogs
```

The background equation should not be overloaded to explain every local phenomenon directly.

Correct claim:

> RLL may define a scale-indexed transition/memory layer for residual gravitational structures and compact-remnant boundaries, requiring external validation.

Incorrect claim:

> RLL already explains black holes, disrupted galaxies, or replaces GR/LCDM using these gaps.

---

## 3. Gap A — Residual gravitational structures

A visible galaxy can be morphologically destroyed while part of its gravitational signature remains encoded in:

- residual stellar mass;
- dark-matter halo structure;
- compact central remnants;
- stellar streams;
- orbital anisotropy;
- weak/strong lensing;
- velocity dispersion;
- gas distribution;
- tidal debris;
- relaxation history.

Important distinction:

```text
visible form disappeared ≠ gravitational effect disappeared
```

A gravitational signature requires remaining mass-energy, or an observable delayed signal. RLL must not claim memory without a physical carrier.

---

## 4. Candidate variables for residual structures

| Symbol | Meaning | Status | Required observable |
|---|---|---|---|
| `Phi_res` | residual gravitational potential | hypothesis | lensing / kinematics / mass model |
| `M_res` | residual bound mass | hypothesis | stellar mass + gas + dark matter inference |
| `C_orb` | orbital coherence after disruption | hypothesis | stellar streams / phase-space maps |
| `tau_relax` | relaxation time of disrupted system | hypothesis | simulations + kinematic age |
| `M_dyn` | dynamic memory proxy | hypothesis | velocity dispersion / orbit reconstruction |
| `H_orphan` | orphan halo indicator | hypothesis | lensing or kinematic mass without luminous galaxy |

Provisional relation, not yet an operational equation:

```text
Memory_residual(scale, t) = F(Phi_res, M_res, C_orb, tau_relax, environment)
```

This must remain marked as `HYPOTHESIS` until measured against data.

---

## 5. Required observables for residual gravitational memory

To test this module, at least one observable set is required:

| Observable | Why it matters |
|---|---|
| stellar velocities | reveals gravitational potential and disrupted orbits |
| stellar streams | traces past tidal disruption |
| weak lensing | detects mass distribution independent of light |
| strong lensing | constrains compact mass concentration |
| gas / X-ray maps | traces hot gas and potential wells |
| proper motions | reconstructs phase-space memory |
| dark-matter halo inference | separates luminous loss from mass loss |
| numerical merger simulation | tests whether observed structure can arise dynamically |

If none of these exist for a given case, status must be:

```text
TOKEN_VAZIO / LACUNA_OBSERVACIONAL
```

---

## 6. Gap B — Compact-remnant transition boundary

The transition from neutron star to black hole is not a single fixed stellar-mass threshold.

RLL must separate:

```text
initial stellar mass
final pre-supernova mass
core mass
helium-core mass
metallicity
rotation
binarity
fallback
explosion energy
final remnant mass
```

The mass that matters observationally is the compact remnant mass, not only the initial stellar mass.

---

## 7. Compact object boundary table

Approximate conservative ranges for documentation and pipeline tagging:

| Regime | Approximate mass range | Interpretation | Claim status |
|---|---:|---|---|
| white dwarf | below Chandrasekhar-scale limit | low/intermediate-mass endpoint | reference |
| neutron star | about 1.2–2.3 solar masses | EOS-dependent compact remnant | reference / active constraint |
| lower mass gap | about 2.5–5 solar masses | massive NS or light BH candidates | active boundary |
| stellar black hole | about 5–50 solar masses | collapse/fallback/fusion products | reference / catalog-tested |
| pair-instability gap | roughly tens to ~100+ solar masses, model-dependent | direct stellar-collapse suppression region | model-dependent |
| intermediate-mass black hole | ~10^2–10^5 solar masses | mergers, dense clusters, direct collapse, seeds | active research |
| supermassive black hole | ~10^6–10^10 solar masses | galactic nuclei / early-universe seeds | cosmology/galaxy evolution |

All ranges must be treated as model-dependent and dataset-dependent, not as fixed universal constants.

---

## 8. Candidate variables for compact-remnant module

| Symbol | Meaning | Status |
|---|---|---|
| `M_ZAMS` | initial stellar mass | required input |
| `M_preSN` | pre-supernova mass | required input when available |
| `M_core` | core mass | required input when available |
| `M_He` | helium-core mass | required input for pair-instability checks |
| `Z` | metallicity | required environment parameter |
| `Omega_spin` | rotation | optional / required for detailed models |
| `binary_flag` | binary interaction channel | required classification |
| `E_SN` | explosion energy | model-dependent |
| `f_fallback` | fallback fraction | model-dependent |
| `M_remnant` | final compact-object mass | measured/model output |
| `remnant_type` | WD / NS / MASS_GAP / BH / IMBH / SMBH | classification |

---

## 9. Suggested YAML schema fragment

A future data file may use:

```yaml
compact_object_transition_zone:
  neutron_star_max_msun_range: [2.0, 2.3]
  lower_mass_gap_msun: [2.5, 5.0]
  common_stellar_bh_msun: [5.0, 50.0]
  pair_instability_gap_status: model_dependent
  claim_boundary:
    sharp_threshold: false
    requires_eos: true
    requires_formation_channel: true
    requires_observational_catalog: true
  observables_required:
    - gravitational_wave_catalog
    - pulsar_mass_measurement
    - xray_binary_mass
    - stellar_evolution_model
    - metallicity_or_environment
```

---

## 10. How this connects to RLL

This module should connect to RLL through structure and population history, not by directly changing the background expansion equation.

Allowed architecture:

```text
RLL background / expansion layer
→ structure formation layer
→ galaxy / halo evolution layer
→ stellar population layer
→ compact-remnant formation layer
→ gravitational-wave / EM catalog comparison
```

Not allowed:

```text
E²(a) directly explains a specific black hole without local astrophysical modeling.
```

---

## 11. Model-gap ledger

| Gap | Current status | Risk if ignored | Next action |
|---|---|---|---|
| residual potential after galaxy disruption | hypothesis | confusing lost morphology with lost gravity | define `Phi_res`, `M_res`, observables |
| orphan halo / dark residual structure | hypothesis | claiming invisible center without mass evidence | require lensing or kinematic proof |
| compact NS/BH boundary | active research boundary | using a fake fixed threshold | add mass-gap ledger |
| lower mass gap | active observational boundary | misclassifying massive NS/light BH | connect to GW catalog |
| pair-instability mass gap | model-dependent | overstating stellar-collapse limits | add metallicity and He-core dependence |
| early SMBH seeds | active cosmology/galaxy-evolution problem | mixing local BH physics with background cosmology | separate seed/accretion/merger channels |
| pre-motion / stored dynamic state | hypothesis | turning intuition into unvalidated parameter | require scale, units, observable, falsifier |

---

## 12. Claim boundary

Allowed statements:

- RLL can represent these as hypothesis modules.
- Residual gravitational structures may preserve observable signatures after visible morphology is lost.
- Compact-remnant formation requires transition zones rather than a single universal threshold.
- These modules require external datasets before validation.

Not allowed statements:

- RLL has proven a new black-hole formation law.
- RLL replaces GR, LCDM, or stellar-evolution models.
- A galaxy can keep gravitational influence without any mass-energy carrier.
- A single stellar mass threshold determines neutron star versus black hole in all cases.

---

## 13. Required future datasets

Future validation should connect this module to:

- gravitational-wave compact-object catalogs;
- neutron-star mass and radius constraints;
- pulsar mass catalogs;
- X-ray binary black-hole masses;
- Gaia astrometric compact-object candidates;
- stellar streams and disrupted-galaxy catalogs;
- weak/strong lensing mass maps;
- galaxy merger simulations;
- high-redshift AGN / SMBH seed observations.

Until these are wired into the pipeline, this document remains a hypothesis boundary, not a validation result.

---

## 14. Minimal falsifiability rule

For every future claim derived from this module, require:

```text
object_or_population
observable
units
dataset
baseline_model
RLL_prediction_or_interpretation
error_model
failure_condition
claim_allowed
```

If any item is missing, claim status must remain:

```text
blocked / TOKEN_VAZIO / LACUNA
```

---

## 15. Safe conclusion

RLL may add value here by organizing transition gaps that are often conceptually mixed:

```text
visible galaxy loss ≠ gravitational history loss
compact-remnant boundary ≠ one fixed mass threshold
local astrophysical transition ≠ direct cosmological-background proof
```

The scientific strength of this module will depend on whether it can be tied to real observables and falsifiable comparisons.

---

## Retrofeedback

F_ok: residual gravitational structures and compact-remnant gaps are now separated as modelable hypothesis modules.  
F_gap: no direct validation dataset is wired in this document yet.  
F_next: add YAML source ledgers for gravitational-wave catalogs, compact-object masses, lensing maps, and disrupted-galaxy observables.
