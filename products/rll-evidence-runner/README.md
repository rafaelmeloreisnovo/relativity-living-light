# RLL Evidence Runner V1

A fail-closed product surface for executing or replaying scientific experiments while preserving evidence boundaries.

```text
experiment YAML
→ schema and policy validation
→ input identity and sidecar verification
→ argv execution without shell=True
→ output hashing
→ model metric extraction
→ baseline comparison
→ semantic receipt
→ verification
```

## Non-authorizations

```text
claim_allowed=false
publication_effect=NONE
CI PASS != scientific truth
replay != fresh fit
readiness != likelihood
negative delta != confirmation
TOKEN_VAZIO != PASS
```

## Install

From the repository root:

```bash
python -m pip install -e products/rll-evidence-runner
```

## Commands

```bash
rll-evidence validate products/rll-evidence-runner/experiments/joint_real_lcdm_rll_v1.yml
rll-evidence run products/rll-evidence-runner/experiments/joint_real_lcdm_rll_v1.yml
rll-evidence verify artifacts/evidence/RLL-EVIDENCE-JOINT-REAL-001/receipt.json
rll-evidence compare artifacts/evidence/RLL-EVIDENCE-JOINT-REAL-001/receipt.json \
  --baseline LCDM_joint_real --candidate RLL_joint_real
```

Pantheon+ full-covariance readiness:

```bash
python scripts/fetch_pantheon_covariance.py
rll-evidence run products/rll-evidence-runner/experiments/pantheon_full_covariance_readiness_v1.yml
```

The large covariance matrix remains outside Git. The experiment requires its sidecar digest and the repository verifier.

## Receipt model

Each receipt contains:

- experiment and commit identity;
- Python/platform context;
- input and output hashes;
- exact argv and exit state;
- bounded stdout/stderr;
- extracted model metrics;
- candidate-minus-baseline deltas;
- `F_ok`, `F_gap`, `F_next`;
- a semantic digest excluding wall-clock duration;
- a full receipt digest;
- invariant `claim_allowed=false`.

## Scope of the two V1 profiles

| Profile | What it proves | What it does not prove |
|---|---|---|
| Joint-real replay | Existing result artifact is readable, hashed and compared consistently | Fresh optimization, independent replication or Pantheon integration |
| Pantheon readiness | Catalog and covariance satisfy strict presence/integrity gates | Cosmological preference or scientific confirmation |

The next scientific adapter is intentionally left explicit rather than simulated: full-covariance Pantheon likelihood with LCDM/RLL under the same frozen inputs, bounds, seeds and uncertainty policy.
