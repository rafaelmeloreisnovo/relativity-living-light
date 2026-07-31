# RLL — real project-source seed v1

This directory contains the **deterministic initial corpus** required to run the project-source index without an external download.

## Included now

- 13 public-safe source bodies, byte-exact, stored in `corpus.public.v1.jsonl.gz.b64`;
- 123,646 source bytes and 4,483 source lines;
- per-source SHA-256, size, line count, temporal state, authority relation and claim boundary in `configs/project_sources_seed.v1.json`;
- one personal/psychometric source represented only by its real digest, size and line count.

The private source body is intentionally absent because this repository is public. `PRIVATE_POINTER_ONLY` is real data about the source and its custody boundary; it is not a placeholder and cannot produce chunks.

## Execute

```bash
PYTHONPATH=src python -m rll.project_source_seed verify
PYTHONPATH=src python -m rll.project_source_seed bootstrap \
  --db artifacts/orcid_rll/project_sources_seed.sqlite3
PYTHONPATH=src python -m rll.project_source_seed search \
  "ORCID vetores proveniência" \
  --db artifacts/orcid_rll/project_sources_seed.sqlite3
```

Expected bootstrap state:

```text
documents=14
verified=13
pointer_only=1
chunks=202
missing=0
mismatch=0
claim_allowed=false
```

## Boundary

`source present` is not `scientific claim validated`. Every indexed chunk remains `claim_allowed=false` and must pass the RLL source-specific hypothesis, dimensional, dataset, uncertainty, falsifier and independent-reproduction gates.
