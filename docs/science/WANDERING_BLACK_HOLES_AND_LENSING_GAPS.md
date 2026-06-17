# Wandering Black Holes and Lensing Gaps

Status: hypothesis boundary / observational gap model  
Scope: wandering black holes, silent compact masses, gravitational lensing, historical impulse, slingshot/recoil  
Claim level: conservative; no replacement claim for GR, LCDM, black-hole astrophysics, or lensing theory

---

## 1. Purpose

This document records an RLL-compatible hypothesis boundary for objects or systems that may be gravitationally important but weakly visible or electromagnetically silent.

The motivating idea is:

> A black hole, compact remnant, binary remnant, or orphan mass concentration may have interacted strongly with surrounding matter in the past, ejected or consumed nearby material, and later remain difficult to observe because it has little or no nearby luminous matter.

This is not treated as proof of a new gravitational law. It is treated as a testable observational gap.

---

## 2. Core distinction

RLL must distinguish three different cases:

```text
current gravitational field
historical gravitational impulse
observational invisibility due to low accretion / low luminosity
```

A black hole can be difficult to observe if it is not accreting gas or interacting with nearby matter. However, it can still be detectable indirectly through:

- gravitational lensing;
- microlensing;
- astrometric lensing;
- perturbation of stellar orbits;
- displaced or recoiling AGN signatures;
- hypervelocity stars;
- stellar streams;
- gravitational-wave merger history;
- compact star clusters bound to a recoiling black hole.

---

## 3. Wandering / rogue / recoiling black hole layer

A black hole may become spatially displaced from its original galactic center through several known or candidate channels:

| Channel | Description | Expected observable |
|---|---|---|
| gravitational-wave recoil | asymmetric GW emission after BH merger gives the remnant a kick | displaced AGN, offset BH, compact bound star cluster |
| three-body slingshot | interaction among multiple compact objects ejects one body | high-velocity BH or star, binary hardening |
| galaxy merger remnant | SMBH not yet settled into new galactic center | off-nuclear AGN / dynamical offset |
| stripped galaxy nucleus | galaxy loses stellar envelope, leaving compact nucleus/BH | compact remnant, unusual velocity dispersion |
| isolated stellar-mass BH | no luminous companion or accretion | microlensing / astrometric lensing |
| consumed local matter | nearby matter depleted, low accretion state | silent compact mass detectable only dynamically |

All of these require external validation before any RLL claim is allowed.

---

## 4. Silent black-hole condition

A black hole may be present but hard to observe when:

```text
accretion_rate ≈ low
nearby_gas_density ≈ low
stellar_companion = absent
jet_activity = absent
AGN_activity = absent
thermal_emission = weak
```

Therefore:

```text
not luminous ≠ not massive
not accreting ≠ not gravitationally active
no visible galaxy ≠ no compact mass
```

But also:

```text
no light ≠ proof of black hole
```

The required evidence must be dynamical, lensing-based, or gravitational-wave based.

---

## 5. Lensing / curvature-of-light channel

If a silent or wandering compact mass lies along or near a background light path, it may reveal itself by curving light.

Possible signatures:

| Signature | Meaning |
|---|---|
| strong lensing | multiple images/arcs from high mass concentration |
| weak lensing | statistical distortion of background galaxies |
| microlensing | temporary brightening of a background star/source |
| astrometric microlensing | apparent position shift of background source |
| time-delay lensing | delayed multiple images due to gravitational potential |
| dark lens candidate | lensing mass without obvious luminous counterpart |

RLL may classify these as `light_curvature_observable`, not as direct visible detection.

---

## 6. Historical impulse / slingshot boundary

A compact object or star can be accelerated by a past gravitational encounter and later appear far away from the original potential.

Conservative interpretation:

> The field acted during the encounter; energy and angular momentum were transferred; the escaped object now carries a kinematic memory of that past interaction.

Not allowed:

> A disappeared field keeps pulling without mass-energy carrier.

Candidate channels:

- Hills mechanism;
- binary disruption near SMBH;
- three-body scattering;
- black-hole binary hardening;
- gravitational-wave recoil;
- tidal stripping during galaxy mergers.

---

## 7. Candidate variables

| Symbol | Meaning | Required observable |
|---|---|---|
| `M_dark` | inferred compact/dark mass | lensing or dynamics |
| `Phi_lens` | lensing potential | lens model / image distortion |
| `theta_E` | Einstein radius or lensing scale | lensing geometry |
| `mu_lens` | magnification | flux/time-domain measurement |
| `alpha_deflect` | deflection angle | astrometry / lens model |
| `v_kick` | recoil/slingshot velocity | proper motion / radial velocity |
| `Delta_v` | velocity gained in encounter | trajectory reconstruction |
| `E_transfer` | transferred orbital energy | dynamical model |
| `J_transfer` | transferred angular momentum | orbital solution |
| `t_enc` | estimated encounter time | traceback / simulation |
| `origin_trace` | reconstructed origin | phase-space data |
| `accretion_rate` | activity level | X-ray/radio/IR/optical constraints |
| `field_present_now` | whether mass/potential is still present | lensing/dynamics |
| `silent_flag` | low-luminosity compact mass candidate | multiwavelength non-detection + mass evidence |

---

## 8. Suggested YAML schema fragment

```yaml
wandering_black_hole_candidate:
  object_id: TOKEN_VAZIO
  candidate_type: wandering_bh | recoiling_bh | silent_bh | dark_lens | orphan_compact_mass
  evidence_channels:
    lensing: TOKEN_VAZIO
    microlensing: TOKEN_VAZIO
    astrometric_lensing: TOKEN_VAZIO
    stellar_kinematics: TOKEN_VAZIO
    hypervelocity_traceback: TOKEN_VAZIO
    gravitational_wave_history: TOKEN_VAZIO
    multiwavelength_accretion: TOKEN_VAZIO
  physical_parameters:
    M_dark_msun: null
    theta_E_arcsec: null
    alpha_deflect_mas: null
    v_kick_km_s: null
    Delta_v_km_s: null
    t_enc_myr: null
    accretion_rate_state: low | active | unknown
  claim_boundary:
    black_hole_confirmed: false
    mass_carrier_required: true
    lensing_or_dynamics_required: true
    no_luminosity_is_not_proof: true
    claim_allowed: false
  status: TOKEN_VAZIO
```

---

## 9. Model-gap ledger

| Gap | Current status | Risk if ignored | Next action |
|---|---|---|---|
| wandering black hole with little accretion | hypothesis / observed class candidate | assuming absence of light means absence of mass | require lensing/dynamics/multiwavelength constraints |
| dark lens candidate | active observational boundary | overclaiming black hole from lensing alone | require mass model and luminous-counterpart search |
| historical slingshot origin | hypothesis | confusing current field with past impulse | reconstruct trajectory and encounter time |
| recoiling SMBH after merger | active astrophysical channel | treating offset as proof without alternatives | require velocity offset, spatial offset, host modeling |
| consumed/depleted local matter | hypothesis | claiming invisibility as proof | require accretion upper limits and environment model |
| isolated stellar-mass BH | active microlensing/astrometry channel | misclassifying neutron star/dark remnant | require mass constraints and compact-remnant boundary |

---

## 10. Required observations before claim

Minimum evidence set for any candidate:

```text
position
proper_motion_or_velocity
mass_estimate
lensing_or_dynamical_signature
luminous_counterpart_search
multiwavelength_non_detection_or_accretion_state
baseline_alternatives
error_model
claim_allowed
```

If the source is only a conceptual possibility, status remains:

```text
TOKEN_VAZIO / LACUNA / HYPOTHESIS
```

---

## 11. Claim boundary

Allowed statements:

- A black hole can be dynamically important while electromagnetically quiet.
- A compact mass can reveal itself through lensing or stellar kinematics even without nearby luminous matter.
- A past gravitational encounter can leave a kinematic memory in an ejected object.
- RLL can model this as a scale-indexed astrophysical gap requiring external validation.

Not allowed statements:

- Lack of visible matter proves a black hole.
- A vanished gravitational field keeps acting without a mass-energy carrier.
- RLL has already discovered or proven a wandering black hole.
- Light curvature alone uniquely identifies a black hole without ruling out other compact/dark-mass models.

---

## 12. Safe conclusion

The relevant RLL insight is:

```text
mass may remain when light disappears;
trajectory may preserve past gravitational impulse;
lensing may reveal compact mass without emission;
absence of accretion is not absence of gravity.
```

This creates a valid model-gap layer:

```text
silent compact mass
→ lensing/dynamics
→ historical impulse
→ trajectory memory
→ claim-boundary ledger
```

The layer becomes scientific only when connected to real lensing, microlensing, astrometric, kinematic, or gravitational-wave datasets.

---

## Retrofeedback

F_ok: wandering/silent black holes, lensing gaps, and historical slingshot memory are now separated as a testable hypothesis layer.  
F_gap: no candidate catalog is wired into the pipeline yet.  
F_next: add source ledgers for microlensing, Gaia astrometry, gravitational-wave recoil candidates, hypervelocity stars, and dark-lens candidates.
