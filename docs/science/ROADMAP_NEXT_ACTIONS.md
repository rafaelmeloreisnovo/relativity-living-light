# Roadmap — Next Actions

Status: operational roadmap  
Claim level: `claim_allowed=false`

This roadmap starts from the current seed-stage validation scaffold and moves toward raw-data validated scientific workflows.

---

## Current state

```text
seed_items: 19
active_routes: 6
cosmology_background: blocked
claim_allowed_true_routes: 0
raw_data_complete_routes: 0
strongest_current_route: compact_remnant_boundary
strongest_transdisciplinary_route: orbital_shape_angular_momentum
highest_productization_asset: claim governance + dense feature matrix + validation dashboard
```

---

## P0 — Freeze governance and canonical artifacts

Goal: make the existing seed-stage system stable, reproducible, and hard to overclaim.

Tasks:

```text
Run Claim Boundary Quality Gates workflow
Run Dense Feature Matrix workflow
Confirm no artifact contains unsupported claim_allowed=true
Confirm canonical JSON, TSV, and MD artifacts match latest CI outputs
Add or update contract checks if CI output format changes
```

Done when:

```text
claim boundary gate passes
dense feature matrix artifact is generated
canonical artifacts are committed
claim_allowed remains false everywhere
```

Value unlocked:

```text
trust, governance, reproducibility, readiness for external review
```

---

## P1 — Raw data manifest and checksum layer

Goal: convert external-only seed references into auditable local raw-data records.

Tasks:

```text
Create data/raw/RAW_DATA_MANIFEST.yml
Add fields: source_url, access_date_utc, license_or_terms, sha256, local_path, source_version
Define data/raw/compact_objects/gw/posteriors/
Define data/raw/orbital_dynamics/ephemerides/
Define data/raw/astrometry/gaia_bh/
Define data/raw/high_z_smbh/
Add script to calculate sha256 for local raw files
```

Done when:

```text
at least one raw dataset is represented with sha256
manifest validates locally
claim_allowed still false until baseline and error model exist
```

Value unlocked:

```text
moves project from seed references toward real reproducible data custody
```

---

## P2 — Compact remnant v2

Goal: turn the strongest immediate route into a falsifiable metric using real posterior or catalog tables.

Tasks:

```text
Ingest one GW posterior sample or compact-object catalog table
Compute mass_gap_overlap_probability
Add EOS and low-mass black-hole baseline placeholders with clear provenance
Write data/results/compact_objects/remnant_boundary_validation_v2.json
Write docs/science/COMPACT_REMNANT_BOUNDARY_V2_REPORT.md
Add CI workflow or extend existing compact-object workflow
```

Done when:

```text
mass_gap_overlap_probability exists
input data has sha256 or explicit external-only boundary
baseline comparison is represented
negative result ledger is updated if RLL does not improve anything
```

Value unlocked:

```text
highest near-term academic value and strongest falsifiable scientific route
```

---

## P3 — Orbital state-vector v2

Goal: move orbital route from reference constants to vector residual tests.

Tasks:

```text
Ingest one state-vector table for Earth or Mars
Compute h_vector = |r x v|
Compare h_vector against seed formula h = sqrt(mu*a*(1-e^2))
Compute state_vector_vs_reference_h_residual
Add baseline note: Kepler/Newton/J2/SPICE or Horizons source
Write orbital_shape_angular_momentum_v2.json and report
```

Done when:

```text
state-vector residual exists
source/version/access metadata exists
uncertainty or precision note exists
no new-gravity claim is made
```

Value unlocked:

```text
strongest transdisciplinary math bridge: vectors, shape, spin, angular momentum
```

---

## P4 — Schemas, tests, and artifact contracts v2

Goal: make every central JSON artifact machine-checkable.

Tasks:

```text
Extend schemas to dense_behavior_features and dense_item_value_map
Add test for total_items=19 until item set changes intentionally
Add test for raw_data_local=false in seed-stage matrix
Add test that negative_results_ledger contains all active routes
Add workflow step for schema/contract checks
```

Done when:

```text
CI fails on malformed artifact
CI fails on missing claim_allowed
CI fails on unsupported change in route count or item count
```

Value unlocked:

```text
software quality and external collaborator confidence
```

---

## P5 — Residual, high-z, and slingshot maturation

Goal: move lateral high-potential routes from seed to first measurable metric.

Tasks:

```text
Residual route: add stream_membership_probability scaffold
High-z route: add Eddington growth grid with uncertainty columns
Slingshot route: add traceback_probability scaffold
Update negative results ledger after each measurable result
Update dense item value map after each v2 result
```

Done when:

```text
each route has one route-specific v2 metric artifact
each route has baseline and limitation notes
all remain claim_allowed=false unless full proof conditions exist
```

Value unlocked:

```text
broader academic portfolio and richer product demo
```

---

## P6 — Paper and product packaging

Goal: package the system as a scientific claim-governance engine and research workflow artifact.

Tasks:

```text
Write docs/science/PAPER_OUTLINE_VALIDATION_GOVERNANCE.md
Write docs/science/PRODUCT_NOTE_CLAIM_GOVERNANCE_ENGINE.md
Add one-page executive summary
Prepare reproducibility matrix for external reviewer
Prepare examples: compact remnant and orbital v2
```

Done when:

```text
paper outline exists
product note exists
two reproducible examples exist
claims are conservative and auditable
```

Value unlocked:

```text
academic communication, partnership readiness, SaaS/prototype framing
```

---

## Recommended next single action

```text
P1: create RAW_DATA_MANIFEST.yml and sha256 helper, then choose compact_remnant_boundary v2 as first raw-data route.
```

---

## Safe conclusion

The roadmap prioritizes trust and raw data before stronger scientific claims. The system remains `claim_allowed=false` until the full evidence chain is present.
