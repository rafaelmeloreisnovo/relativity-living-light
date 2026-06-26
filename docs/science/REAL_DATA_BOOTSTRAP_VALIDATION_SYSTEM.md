# Real Data Bootstrap Validation System

Status: operational bootstrap specification  
Scope: real data ingestion, source ledgers, validation readiness, claim boundary, reproducible calculation proof  
Claim level: conservative; no claim is allowed without real data, checksum, executable metric, baseline, and validation output

---

## 1. Purpose

This document defines the initial real-data body required to turn RLL hypothesis modules into calculable, auditable, and falsifiable validation pathways.

The goal is not only to collect data. The goal is to connect every required real dataset to:

```text
module → observable → source → local path → checksum → validation script → metric → baseline → claim boundary
```

Without this full chain, the status remains:

```text
TOKEN_VAZIO / LACUNA / BLOQUEADO
```

---

## 2. Absolute operating rule

No conceptual structure becomes a scientific result by itself.

A claim is allowed only when all of the following exist:

1. real source identified;
2. source reference or URL recorded;
3. local data path or explicit external-only status recorded;
4. checksum when local data exists;
5. observables mapped;
6. validation script mapped;
7. metric defined;
8. baseline model defined;
9. error model or uncertainty treatment defined;
10. machine-readable output generated;
11. claim boundary explicitly checked.

If any item is missing:

```text
claim_allowed = false
```

---

## 3. Initial real-data body

The initial system must include ledgers for these domains:

| Domain | Ledger path | Purpose | Status |
|---|---|---|---|
| cosmology background | `data/real/bootstrap/real_data_requirements_bootstrap.yml` | global requirement map | scaffold |
| compact objects | `data/real/compact_objects/wandering_black_hole_sources.yml` | wandering/silent/recoiling BH candidates | TOKEN_VAZIO |
| residual structures | `data/real/structure/residual_gravity_sources.yml` | orphan halos, disrupted galaxies, historical impulse | TOKEN_VAZIO |
| compact-remnant boundary | `data/real/compact_objects/remnant_boundary_sources.yml` | NS/BH mass gap and remnant classes | to be added |
| lensing | `data/real/lensing/dark_lens_sources.yml` | dark lens / microlensing / astrometric lensing | to be added |
| kinematics | `data/real/kinematics/hypervelocity_sources.yml` | slingshot and traceback candidates | to be added |
| high-z SMBH | `data/real/high_z_smbh/high_z_seed_sources.yml` | early black-hole seed constraints | to be added |

---

## 4. Required validation modules

Each module must have a validation target, even if still empty.

| Module | Required calculation | Required baseline | Output expected |
|---|---|---|---|
| RLL vs LCDM/CPL | chi2, AIC, AICc, BIC, covariance-aware comparison | LCDM, wCDM, CPL/w0waCDM | `data/results/cosmology/model_comparison.json` |
| compact remnant boundary | mass-class consistency, mass-gap classification | NS EOS / BH catalog baseline | `data/results/compact_objects/remnant_boundary_validation.json` |
| wandering BH / dark lens | mass-lensing/dynamics consistency | non-BH lens alternatives | `data/results/compact_objects/wandering_bh_validation.json` |
| residual gravity | mass carrier + kinematic/lensing consistency | tidal/disruption baseline | `data/results/structure/residual_gravity_validation.json` |
| historical impulse | trajectory traceback + Delta_v consistency | standard slingshot/recoil model | `data/results/kinematics/historical_impulse_validation.json` |
| high-z SMBH seeds | mass-redshift-growth feasibility | Eddington/accretion/seed models | `data/results/high_z_smbh/seed_validation.json` |

---

## 5. Minimum data columns by module

### 5.1 Cosmology

```text
z
observable_type
observable_value
uncertainty
covariance_reference
source_id
model_prediction_LDCM_or_LCDM
model_prediction_RLL
residual
pull
```

### 5.2 Compact remnant boundary

```text
object_id
candidate_class
mass_msun
mass_uncertainty_low
mass_uncertainty_high
radius_km_if_available
spin_if_available
source_catalog
measurement_method
classification_baseline
claim_allowed
```

### 5.3 Wandering / silent black holes

```text
candidate_id
candidate_type
ra
dec
redshift_or_distance
mass_estimate_msun
mass_method
lensing_signature
kinematic_signature
accretion_state
multiwavelength_counterpart
alternative_models
claim_allowed
```

### 5.4 Residual gravitational structures

```text
object_id
structure_type
stellar_mass_estimate
dark_mass_estimate
velocity_dispersion
stream_or_tidal_feature
lensing_evidence
mass_carrier_evidence
environment
baseline_model
claim_allowed
```

### 5.5 Historical impulse / slingshot

```text
object_id
object_type
position
proper_motion
radial_velocity
origin_trace
v_in
v_out
Delta_v
t_enc
encounter_model
current_field_status
claim_allowed
```

---

## 6. Bootstrap scan behavior

The validation bootstrap must:

1. scan all source ledgers under `data/real/`;
2. detect `TOKEN_VAZIO`, `null`, missing local paths, and missing checksums;
3. classify each source as `ready`, `blocked`, `external_only`, `token_vazio`, or `schema_error`;
4. build a machine-readable summary;
5. refuse to set `claim_allowed=true` unless every required condition is satisfied;
6. write summary outputs under `data/results/bootstrap/`.

Expected outputs:

```text
data/results/bootstrap/real_data_bootstrap_summary.json
data/results/bootstrap/real_data_bootstrap_ledger.tsv
docs/science/REAL_DATA_BOOTSTRAP_SCAN_REPORT.md
```

---

## 7. Required claim boundary language

Every generated validation report must include:

```text
This artifact is a validation-readiness artifact unless all required real data, checksums, metrics, baselines, and uncertainty treatments are present.
```

And:

```text
No scientific superiority claim is allowed from incomplete source ledgers or TOKEN_VAZIO entries.
```

---

## 8. Initial execution order

Recommended order:

1. create bootstrap requirement YAML;
2. create scan script;
3. run scan against existing ledgers;
4. generate summary JSON/TSV/report;
5. add one real dataset source per module;
6. add validation script for one module at a time;
7. only then calculate metrics.

---

## 9. Safe conclusion

The system starts as a body of structured absence:

```text
absence is mapped
lacuna is protected
TOKEN_VAZIO is explicit
claim is blocked
next data requirement is visible
```

This is the correct starting point for real validation.

---

## Retrofeedback

F_ok: real-data bootstrap requirements are now defined as a reproducible validation system.  
F_gap: real datasets still need to be ingested and hashed.  
F_next: run the bootstrap scan and then add one real catalog per module.
