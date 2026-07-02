# Coherent Update Protocol

## Status

`audit_note / governance_record / claim_boundary`

## Purpose

This file records the repository rule for **coherent updates**.

A coherent update is small, auditable, non-destructive and claim-bounded. It improves traceability, documentation, validation plumbing or repository hygiene without promoting a scientific conclusion beyond the evidence.

## Operating rule

Every coherent update must preserve four boundaries:

1. **No deletion first** — classify, register and trace before moving or removing artifacts.
2. **No claim inflation** — infrastructure, metadata, CI success or documentation do not validate RLL by themselves.
3. **No synthetic promotion** — mock, sample, demo and generated placeholders remain blocked from `REAL_VALIDATED` unless source, hash, execution, metric, baseline and claim boundary exist.
4. **No regime mixing** — scientific core, validation, governance, symbolic material, authorial legacy, data and results must stay distinguishable.

## Allowed update classes

| Class | Allowed action | Claim boundary |
|---|---|---|
| `docs/audits` | record audit status, gaps, decisions and compatibility notes | does not prove scientific validity |
| `docs/governance` | define policy, workflow and repository regimes | does not change model output |
| `docs/validation` | describe tests, falsifiers and required evidence | does not imply the test passed |
| `tools/validators` | check structure, fields, paths, schemas and contracts | structural pass is not scientific validation |
| `.github/workflows` | run bounded CI checks with explicit permissions and timeouts | CI success is execution evidence only |
| `data/real` | register real sources with signatures, checksums and variance policy | source registration is not model confirmation |
| `results` | materialize outputs with manifest/checksum/report | output exists does not mean model wins |

## Required minimum record

A coherent update should answer:

```text
what changed?
why was it needed?
which artifact class is touched?
what claim is allowed?
what claim remains blocked?
what should be checked next?
```

## Claim boundary

This file does not validate RLL, does not refute RLL, does not select a cosmological model, and does not change any scientific result.

It only defines a safer update discipline for future repository work.

## Next coherent updates

Recommended next updates, in safe order:

1. Create or update a dated audit note for the current repository state.
2. Ensure each new data/validation artifact has a manifest or registry entry.
3. Keep symbolic/epistemic analogies separated from scientific validation documents.
4. Prefer small commits with one responsibility each.
5. Re-run inventory and contract checks after structural changes.

## Final rule

```text
coherence first;
traceability second;
claim last;
proof only after evidence.
```
