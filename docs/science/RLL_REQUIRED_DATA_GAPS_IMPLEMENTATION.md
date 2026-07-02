# RLL Required Data Gaps Implementation

**Status:** operational gap registry  
**Claim level:** `claim_allowed=false`  
**Registry:** `data/real_sources/rll_required_data_gap_registry.yml`

---

## 1. Purpose

This document records the implementation of a machine-readable gap layer for RLL validation routes.

The goal is not to add new observational data and not to approve any claim. The goal is to state, route by route, what is still absent and what evidence is required before a route can move toward a test-ready state.

---

## 2. Implemented gap layer

| Artifact | Role |
|---|---|
| `data/real_sources/rll_required_data_gap_registry.yml` | route-level registry of missing required data/artifacts |
| `tools/validate_required_data_gap_registry.py` | validator for required fields, states and claim gate |
| `tests/test_required_data_gap_registry.py` | CI coverage for the gap registry |
| `docs/science/VALIDATION_DASHBOARD.md` | dashboard link to the new layer |

---

## 3. Gaps registered

| Gap | Route | Priority | Required next artifact |
|---|---|---:|---|
| `GAP-COSMO-ROBUST-FIT` | `cosmology_background` | P0 | robust multi-seed joint runs |
| `GAP-COSMO-SUPERNOVA` | `cosmology_background` | P0 | covariance-aware supernova input |
| `GAP-COSMO-GROWTH` | `cosmology_growth` | P0 | external growth benchmark |
| `GAP-COSMO-CMB` | `cosmology_background` | P1 | CMB covariance or likelihood interface |
| `GAP-SIREN-DISTANCE` | `late_universe_sirens` | P2 | standard-siren distance catalog/likelihood |
| `GAP-REMNANT-POSTERIORS` | `compact_remnant_boundary` | P0 | public posterior samples with checksum |
| `GAP-SMBH-SEEDS` | `high_z_smbh_seeds` | P2 | high-z SMBH table and seed baselines |
| `GAP-ASTROMETRY-CANDIDATES` | `wandering_dark_compact_mass` | P2 | astrometric candidate manifest |

---

## 4. Promotion rule

A route remains blocked until the registry can point to:

```text
materialized data or primary reference
checksum or source signature
baseline/adversary
metric
uncertainty or error policy
executable command or artifact
falsifier
```

This converts vague absence into actionable work.

---

## 5. Immediate priority

The highest-priority practical route remains:

```text
GAP-REMNANT-POSTERIORS
```

Reason: the validation dashboard already marks `compact_remnant_boundary` as the recommended next route because it has a clearer raw-data path, metric and baseline.

The highest-priority cosmology route is:

```text
GAP-COSMO-ROBUST-FIT
```

Reason: the current cosmology artifact is still a smoke/sanity result and cannot support strong claims.

---

## 6. Safe language

Allowed:

```text
The repository now has an explicit data-gap registry for blocked validation routes.
```

Blocked:

```text
A listed gap is already solved.
The presence of a target path means the data exist.
The registry validates RLL.
The registry proves model superiority.
```

---

## 7. R3

```text
F_ok   = data gaps are now route-indexed and machine-readable.
F_gap  = required raw inputs, checksums, baselines and metrics still need execution.
F_next = implement the P0 gap with the most accessible public-data path.
```
