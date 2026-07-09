# Relational Validation Results

## Status

`relational_validation_regime / evidence_convergence / claim_boundary`

## Purpose

This directory stores evolving logs, artifacts and ledgers for relational validation.

Relational validation means that a claim may be strengthened only when independent artifacts converge coherently across:

```text
source data
execution log
result artifact
metric
baseline/adversary
uncertainty or covariance when applicable
claim boundary
negative ledger / contradiction check
reproducible command or workflow
```

## Claim boundary

```text
claim_allowed=false_by_default
relational_validation_directory=true
automatic_proof=false
scientific_validation=false_until_convergence_gates_pass
```

This directory allows future proof-state promotion **if** evidence is true, coherent, tested and convergent. It does not automatically prove RLL, RAFAELIA, cosmology, physics, neuroscience or any derived claim.

## Directory layout

```text
results/relational_validation/
  README.md
  RELATIONAL_VALIDATION_LEDGER.yml
  logs/
    README.md
  artifacts/
    README.md
```

## Promotion states

| State | Meaning |
|---|---|
| `RELATIONAL_PENDING` | Claim has a proposed relation graph but lacks tested convergence. |
| `RELATIONAL_TESTED` | At least one test/log/artifact exists, but convergence is incomplete. |
| `RELATIONAL_CONVERGENCE_CANDIDATE` | Multiple independent artifacts agree under declared metrics and baselines. |
| `RELATIONAL_CONVERGENCE_BLOCKED` | Evidence is incomplete, contradictory, synthetic-only or lacks baseline/error. |
| `RELATIONAL_VALIDATED_REVIEW_READY` | Convergence package is complete enough for external review. |
| `RELATIONAL_REFUTED` | Tested evidence contradicts the claim. |

## Rule

```text
Convergence may promote a proof-state.
Convergence cannot skip evidence.
Self-reference is allowed only as traceability, not as circular proof.
```

## Self-reference policy

Every new relational validation package should reference:

```text
1. this README;
2. RELATIONAL_VALIDATION_LEDGER.yml;
3. the exact log path;
4. the exact artifact path;
5. the command or workflow that generated it;
6. the claim boundary it respects;
7. the next gate that could promote, block or refute it.
```

## Minimal package checklist

```text
[ ] claim_id
[ ] relation_graph_id
[ ] source_paths
[ ] log_paths
[ ] artifact_paths
[ ] metric_names
[ ] baseline_or_adversary
[ ] uncertainty_or_covariance_status
[ ] contradiction_check
[ ] reproducibility_command
[ ] claim_allowed
[ ] claim_blocked
[ ] next_gate
```
