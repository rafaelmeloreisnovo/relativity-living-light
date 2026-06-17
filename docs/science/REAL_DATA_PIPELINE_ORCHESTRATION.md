# Real Data Pipeline Orchestration

Status: operational orchestration guide  
Scope: real observational seeds, ingestion planning, target ledgers, validators, outputs, raw-data paths  
Claim level: orchestration only; no final scientific claim

---

## 1. Purpose

This document defines the operational path for including real observational data into the RLL validation system.

It turns the current seed catalogs into a structured queue:

```text
seed record
→ route
→ target ledger
→ validator
→ expected result artifact
→ future raw-data path
→ metric
→ baseline
→ claim boundary
```

---

## 2. Core files

### Inputs

```text
data/real/bootstrap/real_observational_seed_v0.csv
data/real/bootstrap/real_observational_seed_v1.csv
data/real/bootstrap/real_seed_pipeline_orchestration.yml
```

### Orchestration script

```text
scripts/data_scan/build_real_seed_ingestion_plan.py
```

### Workflow

```text
.github/workflows/real-seed-ingestion-plan.yml
```

### Generated outputs

```text
data/results/bootstrap/real_seed_ingestion_plan.json
data/results/bootstrap/real_seed_ingestion_plan.tsv
docs/science/REAL_SEED_INGESTION_PLAN.md
```

---

## 3. Routes

### 3.1 Compact remnant boundary

Seeds:

```text
GW230529
GW190814
PSR J0740+6620
PSR J0952-0607
```

Route:

```text
data/real/compact_objects/remnant_boundary_sources.yml
→ scripts/validation/validate_compact_remnant_boundary.py
→ data/results/compact_objects/remnant_boundary_validation.json
```

Future raw paths:

```text
data/raw/compact_objects/gw/posteriors/
data/raw/compact_objects/pulsars/
data/raw/compact_objects/eos_baselines/
```

Future metrics:

```text
mass_gap_overlap_probability
posterior_classification_probability
EOS_minimum_maximum_mass_constraint
uncertainty_overlap
```

---

### 3.2 Wandering / dark compact mass

Seeds:

```text
OGLE-2011-BLG-0462
Gaia BH1
Gaia BH2
```

Route:

```text
data/real/compact_objects/wandering_black_hole_sources.yml
data/real/lensing/dark_lens_sources.yml
→ scripts/validation/validate_dark_lens_candidates.py
→ data/results/compact_objects/wandering_bh_validation.json
```

Future raw paths:

```text
data/raw/lensing/microlensing/
data/raw/astrometry/gaia_bh/
data/raw/spectroscopy/radial_velocity/
```

Future metrics:

```text
astrometric_binary_dark_mass_consistency
microlensing_mass_consistency
luminous_counterpart_exclusion_score
alternative_model_comparison
```

---

### 3.3 Residual gravitational structures

Seeds:

```text
Gaia BH3
ED-2 stream context
```

Route:

```text
data/real/structure/residual_gravity_sources.yml
→ scripts/validation/validate_residual_gravity_structures.py
→ data/results/structure/residual_gravity_validation.json
```

Future raw paths:

```text
data/raw/structure/stellar_streams/
data/raw/astrometry/gaia_bh3/
data/raw/metallicity/low_metallicity_stars/
```

Future metrics:

```text
stream_membership_probability
compact_mass_stream_context_consistency
low_metallicity_origin_consistency
residual_mass_carrier_check
```

---

### 3.4 Historical impulse / slingshot

Seeds:

```text
S5-HVS1
LMC hypervelocity-star seed
```

Route:

```text
data/real/kinematics/hypervelocity_sources.yml
→ scripts/validation/validate_historical_impulse_candidates.py
→ data/results/kinematics/historical_impulse_validation.json
```

Future raw paths:

```text
data/raw/kinematics/hypervelocity_stars/
data/raw/astrometry/gaia_hvs/
data/raw/models/galactic_potential/
```

Future metrics:

```text
traceback_probability
escape_velocity_consistency
Hills_mechanism_energy_consistency
origin_model_comparison
```

---

### 3.5 High-z SMBH seeds

Seeds:

```text
UHZ1
CEERS 1019
```

Route:

```text
data/real/high_z_smbh/high_z_seed_sources.yml
→ scripts/validation/validate_high_z_smbh_seeds.py
→ data/results/high_z_smbh/seed_validation.json
```

Future raw paths:

```text
data/raw/high_z_smbh/jwst/
data/raw/high_z_smbh/chandra/
data/raw/high_z_smbh/photometry_spectroscopy/
```

Future metrics:

```text
Eddington_growth_feasibility_grid
seed_mass_requirement
light_seed_vs_heavy_seed_comparison
magnification_and_selection_context_check
```

---

## 4. Operational command

Run locally or in CI:

```bash
python scripts/data_scan/build_real_seed_ingestion_plan.py
```

Or use GitHub Actions:

```text
Real Seed Ingestion Plan
```

---

## 5. Claim boundary

Allowed now:

```text
The repository contains a real-data ingestion orchestration map and planned pipeline routes.
```

Not allowed now:

```text
The repository has completed raw-data validation for all seed records.
```

Reason:

```text
Seed records are external anchors. Raw data, checksums, posterior samples, full metrics, baselines, and uncertainty propagation are still required.
```

---

## 6. Safe conclusion

```text
v0 = real seed validation artifacts
v1 = expanded real seed map
orchestration = routes and ingestion queue
next = raw catalog ingestion and checksum verification
```

This is a pipeline of possibility made auditable, not a final claim.
