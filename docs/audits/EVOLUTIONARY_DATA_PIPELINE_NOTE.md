# Sequence Data Pipeline Note

Status: `partially_implemented / claim_bounded`

Implemented files:

```text
scripts/calculate_sequence_metrics.py
tests/test_calculate_sequence_metrics.py
data/real/evolutionary/README.md
.github/workflows/validate-sequence-metrics.yml
```

Implemented flow:

```text
local FASTA input
-> raw FASTA artifact
-> records CSV
-> pairwise CSV
-> metrics JSON
-> manifest JSON
-> targeted pytest check
-> lightweight GitHub Actions workflow
```

Calculated fields:

```text
sequence_count
total_bases
length_min / length_max / length_mean
A/C/G/T/N/OTHER counts
GC fraction
pairwise p-distance for equal-length comparable sequences
mismatch count
```

Boundary:

```text
This is structural data infrastructure. It does not validate RLL or promote scientific claims.
```

Network retrieval is not included in this commit. The safe next step is to add a reviewed source allowlist and connect it to the calculator.
