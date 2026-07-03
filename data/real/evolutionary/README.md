# Real Evolutionary Data Artifact Root

Status: `artifact_root / claim_bounded`

This directory is reserved for small, provenance-safe sequence artifacts generated from public or local FASTA inputs.

Generated files should follow this pattern:

```text
<dataset>.raw.fasta
<dataset>.records.csv
<dataset>.pairwise.csv
<dataset>.metrics.json
<dataset>.MANIFEST.json
```

## Boundary

This directory stores real-data artifacts and calculated descriptive metrics. It does not validate RLL, infer a tree, prove selection, or establish a scientific claim by itself.

## Recommended command

```bash
python scripts/calculate_sequence_metrics.py \
  --input path/to/input.fasta \
  --dataset-id example_sequence_dataset \
  --output-dir data/real/evolutionary
```

For public sources, fetch or export the FASTA file first using an official provider, keep the source URL/access date in a note or manifest, then run the calculator. Network fetching code was intentionally not added here until the source allowlist and CI policy are reviewed.
