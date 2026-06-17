# Canonical Route Artifacts Validation

Status: uploaded combined artifact inspected  
Claim level: `claim_allowed=false`

Artifact inspected:

```text
canonical-route-artifacts.zip
```

Expected package contents were present:

```text
data/real/bootstrap/canonical_route_checklist.yml
docs/science/CANONICAL_ROUTE_CHECKLIST.md
docs/science/TACTICAL_ROUTE_ORCHESTRATOR.md
docs/science/ROUTE_DEFIBRILLATION_POLICY.md
docs/science/PEER_REVIEW_READINESS_STATUS.md
docs/science/ROADMAP_NEXT_ACTIONS.md
data/raw/RAW_DATA_MANIFEST.yml
data/results/bootstrap/raw_data_manifest_status.json
data/results/bootstrap/raw_data_manifest_status.tsv
docs/science/RAW_DATA_MANIFEST_STATUS.md
data/real/orbital_dynamics/orbital_shape_angular_momentum_seed_v1.csv
data/raw/orbital_dynamics/ephemerides/jpl_horizons_mars_vectors_2006_sample.csv
data/raw/orbital_dynamics/ephemerides/jpl_horizons_mars_vectors_2006_sample.meta.yml
data/results/orbital_dynamics/orbital_state_vector_v2_validation.json
docs/science/ORBITAL_STATE_VECTOR_V2_REPORT.md
```

Validation findings:

```text
total_files: 15
raw_status_total_records: 8
raw_status_files_present: 2
raw_status_files_missing: 6
orbital_v2_items: 2
claim_allowed: false
```

Correction applied:

```text
The Mars vector CSV in the combined artifact is LF-normalized.
Its canonical repository checksum is:
32406d83e4fa91fdf3d0f4359a849503c4b33bfa8fef1b71fdf496231ba15c86
bytes: 359
```

The manifest, metadata and raw status files were aligned to this canonical LF-normalized checksum.

Safe conclusion:

```text
The combined artifact is structurally complete. It remains pre-review and claim-blocked. The next step is to add schema/tests for canonical artifact validation in CI.
```
