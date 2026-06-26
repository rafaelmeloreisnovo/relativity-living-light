# Real Observational Seed v1 Map

Status: mapped real-data supplement  
Claim level: external seed only; no final scientific claim  
Extends: `data/real/bootstrap/real_observational_seed_v0.yml`

---

## 1. Purpose

This document maps additional real observational seed records to the RLL validation structure.

The goal is to increase real-data coverage without pretending that raw catalogs, posterior samples, checksums, or final baselines have already been ingested.

Main files:

```text
data/real/bootstrap/real_observational_seed_v1.yml
data/real/bootstrap/real_observational_seed_v1.csv
```

---

## 2. New seed records

| Seed | Module | Main observable | Why it maps |
|---|---|---|---|
| `REAL_SEED_GW190814` | compact remnant boundary | secondary mass 2.50–2.67 M_sun | lower mass-gap / NS-BH boundary |
| `REAL_SEED_PSR_J0952_0607` | compact remnant boundary | neutron-star mass 2.35 ± 0.17 M_sun | high-mass neutron-star / EOS constraint |
| `REAL_SEED_GAIA_BH1` | wandering black holes | dormant BH mass 9.62 ± 0.18 M_sun | dark mass via astrometry + RV |
| `REAL_SEED_GAIA_BH2` | wandering black holes | dormant BH mass 8.9 ± 0.3 M_sun | wide dormant BH binary |
| `REAL_SEED_GAIA_BH3` | residual gravity structures | ~33 M_sun BH; ED-2 stream context | massive dormant BH linked to residual stream / low metallicity |
| `REAL_SEED_S5_HVS1` | historical impulse slingshot | 1755 ± 50 km/s; GC traceback | direct historical impulse / Hills mechanism seed |
| `REAL_SEED_CEERS_1019` | high-z SMBH seeds | z=8.679; log M_BH=6.95 ± 0.37 | early AGN growth / seed model constraint |

---

## 3. Data-to-structure map

```text
observational seed
→ target ledger
→ expected result artifact
→ future metric
→ baseline model
→ claim boundary
```

### 3.1 Compact remnant boundary

Seeds:

```text
GW190814
PSR J0952-0607
```

Target ledger:

```text
data/real/compact_objects/remnant_boundary_sources.yml
```

Expected result:

```text
data/results/compact_objects/remnant_boundary_validation.json
```

Future metrics:

```text
mass_gap_overlap_probability
EOS_minimum_maximum_mass_constraint
uncertainty_overlap
posterior_classification
```

### 3.2 Wandering / dormant black holes

Seeds:

```text
Gaia BH1
Gaia BH2
```

Target ledger:

```text
data/real/compact_objects/wandering_black_hole_sources.yml
```

Expected result:

```text
data/results/compact_objects/wandering_bh_validation.json
```

Future metrics:

```text
astrometric_binary_dark_mass_consistency
wide_binary_dark_mass_consistency
luminous_companion_exclusion_score
```

### 3.3 Residual gravitational structures

Seed:

```text
Gaia BH3 / ED-2 stream context
```

Target ledger:

```text
data/real/structure/residual_gravity_sources.yml
```

Expected result:

```text
data/results/structure/residual_gravity_validation.json
```

Future metrics:

```text
stream_membership_probability
compact_mass_stream_context_consistency
low_metallicity_origin_consistency
```

### 3.4 Historical impulse / slingshot

Seed:

```text
S5-HVS1
```

Target ledger:

```text
data/real/kinematics/hypervelocity_sources.yml
```

Expected result:

```text
data/results/kinematics/historical_impulse_validation.json
```

Future metrics:

```text
traceback_probability
escape_velocity_consistency
Hills_mechanism_energy_consistency
```

### 3.5 High-redshift SMBH seeds

Seed:

```text
CEERS 1019
```

Target ledger:

```text
data/real/high_z_smbh/high_z_seed_sources.yml
```

Expected result:

```text
data/results/high_z_smbh/seed_validation.json
```

Future metrics:

```text
Eddington_growth_feasibility_grid
seed_mass_requirement
light_seed_vs_heavy_seed_comparison
super_Eddington_requirement
```

---

## 4. Claim boundary

Allowed now:

```text
The repository contains a broader real observational seed map for future validation.
```

Not allowed now:

```text
RLL has validated new compact-remnant, dormant-black-hole, residual-structure, slingshot, or high-z SMBH claims.
```

Reason:

```text
raw catalogs, checksums, posterior samples, model grids, baseline comparisons, and error propagation remain required.
```

---

## 5. Safe conclusion

```text
v0 = first real seed validation artifacts
v1 = more real data mapped into the validation graph
v1 ≠ final validation
v1 = next ingestion queue
```

The next operational step is to choose one branch and ingest its raw source table or posterior data.
