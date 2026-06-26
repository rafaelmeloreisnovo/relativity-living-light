# Claim Boundary Quality Gates

Status: active quality gate  
Claim level: `claim_allowed=false`

---

## Purpose

This gate prevents seed-stage validation artifacts from accidentally becoming scientific claims.

It protects the repository rule:

```text
No claim_allowed=true before raw data, checksum, metric, baseline, uncertainty/error model, and review evidence exist.
```

---

## Files added

```text
scripts/validation/check_claim_boundary.py
scripts/validation/check_seed_artifact_contracts.py
tests/test_real_seed_utils.py
tests/test_orbital_outputs.py
data/schemas/real_seed_ingestion_plan.schema.json
data/schemas/orbital_shape_angular_momentum.schema.json
.github/workflows/claim-boundary-quality-gates.yml
```

---

## What the CI checks

```text
1. validation scripts compile
2. seed-stage artifacts keep claim_allowed=false
3. canonical JSON artifacts keep required contract fields
4. parser regression tests pass
5. orbital output regression tests pass
```

---

## Why this matters

A previous parser issue converted positive ranges and uncertainties into signed values. The new tests prevent that class of regression.

The claim gate also makes sure future edits do not silently change the scientific state from seed-level to claim-level.

---

## Safe conclusion

The project now has a first formal quality layer above the seed artifacts. This does not prove the science; it protects the path toward proof.
