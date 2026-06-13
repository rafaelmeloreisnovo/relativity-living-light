# Raw Data Manifest CI Artifact Note

Status: uploaded workflow artifact validated in ChatGPT session.  
Claim level: `claim_allowed=false`

Artifact inspected:

```text
raw-data-manifest-status.zip
```

Expected files were present:

```text
data/results/bootstrap/raw_data_manifest_status.json
data/results/bootstrap/raw_data_manifest_status.tsv
docs/science/RAW_DATA_MANIFEST_STATUS.md
```

Validated state:

```text
status: raw_data_manifest_status_generated
total_records: 6
raw_files_present: 0
raw_files_missing: 6
claim_allowed: false
```

Safe conclusion:

```text
The raw-data custody scaffold is working. No raw files are present yet, so all records remain pending_raw_ingestion and cannot support scientific claims.
```
