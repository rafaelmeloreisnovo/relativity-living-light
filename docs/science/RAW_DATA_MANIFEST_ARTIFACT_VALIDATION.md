# Raw Data Manifest Artifact Validation

Status: workflow artifact validated  
Claim level: `claim_allowed=false`

Uploaded artifact inspected:

```text
raw-data-manifest-status.zip
```

Expected files present:

```text
data/results/bootstrap/raw_data_manifest_status.json
data/results/bootstrap/raw_data_manifest_status.tsv
docs/science/RAW_DATA_MANIFEST_STATUS.md
```

Validated values:

```text
schema_version: 0.1
status: raw_data_manifest_status_generated
total_records: 6
raw_files_present: 0
raw_files_missing: 6
claim_allowed: false
```

Meaning:

```text
The custody scaffold is functioning. No raw data files are present yet, so every slot remains pending_raw_ingestion.
```

Safe conclusion:

```text
The raw-data layer is ready to receive files, calculate SHA256, and move selected routes toward v2 metrics. It does not yet support scientific claims.
```
