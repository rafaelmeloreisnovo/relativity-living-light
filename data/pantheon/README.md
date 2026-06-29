# Pantheon+ Required Inputs

This directory is for user-supplied Pantheon+ files required by the repository's real-data preflight and likelihood flows.

## Required files

1. `Pantheon+SH0ES.dat` (required; official distance/redshift table)
2. `Pantheon+SH0ES_STAT+SYS.cov` (optional heavy covariance; required only for full covariance likelihoods)
3. `Pantheon+SH0ES_STATONLY.cov` (optional heavy covariance; required only for stat-only covariance likelihoods)

> Without the required table, Pantheon+ preflight must fail with exit code `2`. Heavy covariance files are intentionally optional for lightweight source-custody checks.

## Provenance fields (record for each file)

For each file, record the following in your lab log or run manifest:
- `filename`
- `source_url`
- `source_project` (e.g., Pantheon+SH0ES DataRelease)
- `source_version_or_tag`
- `downloaded_at_utc`
- `downloaded_by`
- `license_or_terms`
- `sha256`
- `size_bytes`

## SHA256 requirements

- SHA256 must be computed immediately after download and before first run.
- SHA256 must be rechecked when files are moved, copied, or re-downloaded.
- Automation path:

```bash
python scripts/verify_pantheon_inputs.py --json
```

This script reports `sha256`, `size_bytes`, `required`, and missing-file status for required and optional-heavy inputs.

## Minimal validation commands

```bash
python -m rll.cli preflight-real
python -m rll.cli preflight-real --json
python scripts/verify_pantheon_inputs.py --json
```

## Note on scientific claims

Presence and checksum validation of Pantheon+ files establishes ingestion readiness only. It does **not** establish model preference claims by itself.
