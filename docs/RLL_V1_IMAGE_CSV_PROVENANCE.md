# RLL V1 Image and CSV Provenance

**Status:** `TAG_SIDE_OPERATIONAL / DOI_SIDE_TOKEN_VAZIO / CLAIM_BLOCKED`  
**Scope:** immutable inventory of images and CSV files stored in Git tag `v1.0.0`.

## Claim boundary

This document and its workflow establish repository provenance only.

```text
tag path + Git object id + SHA-256
!= DOI custody
!= scientific validation
!= physical confirmation
```

`claim_allowed=false` remains mandatory.

## Operational route

```text
Git tag v1.0.0
→ resolve immutable commit and tree
→ enumerate image/CSV blobs with git ls-tree
→ read blobs with git cat-file
→ calculate SHA-256
→ emit inventory, receipt, manifest and checksums
→ preserve DOI comparison as TOKEN_VAZIO
```

Canonical implementation:

- workflow: `.github/workflows/rll-v1-tag-provenance.yml`
- builder: `tools/audit_v1_tag_media_provenance.py`
- tests: `tests/test_v1_tag_media_provenance.py`
- artifact name: `rll-v1-tag-provenance-${RUN_ID}`

## Artifact contract

```text
V1_IMAGE_CSV_INVENTORY.csv
TAG_RECEIPT.json
RLL_V1_IMAGE_CSV_PROVENANCE.md
MANIFEST.json
CHECKSUMS.sha256
BUILD.log
```

The inventory records:

- category (`image` or `csv`);
- path inside the immutable tag;
- Git mode and object type;
- Git object identifier;
- blob size;
- SHA-256 of exact blob bytes.

## What this closes

The Git-tag side of the earlier provenance uncertainty becomes operationally testable and reproducible. A reviewer can verify which image and CSV bytes existed in `v1.0.0` without trusting the current working tree.

## What remains open

The DOI/Zenodo package has not yet been materialized through an official snapshot and compared file by file.

Therefore:

```text
TV-RLL-V1-IMAGE-CSV-PROVENANCE.state = PARTIALLY_RESOLVED
```

Required final closure:

1. obtain the official DOI/Zenodo snapshot;
2. inventory its files and hashes;
3. compare path, content hash, role and timestamp against the tag artifact;
4. classify every mismatch as expected divergence, `TOKEN_VAZIO` or `CONTRADICTION`;
5. preserve a signed or independently reproducible comparison receipt.

## F_ok

- immutable Git commit and tree can be resolved;
- image and CSV blobs are read directly from Git objects;
- SHA-256 and checksums are produced;
- the audit fails closed when the requested tag does not exist;
- CI does not push, merge or promote claims.

## F_gap

- DOI/Zenodo snapshot and custody comparison;
- independent review of the final tag↔DOI relationship;
- interpretation of unmatched artifacts.

## F_next

Materialize the official DOI/Zenodo package and generate the second side of the comparison without changing the tag-derived inventory.
