# Cross-Repo Relationship Registry

## Status

`beta_relationship_registry / evidence_gated / no_claim_promotion`

## Purpose

This registry preserves the useful part of the unified ecosystem map: it records possible relationships among repositories without treating them as validated integration.

Repositories in scope:

```text
instituto-Rafael/relativity-living-light
rafaelmeloreisnovo/ChipQuantum
rafaelmeloreisnovo/termux-app-rafacodephi
```

## State vocabulary

```text
VERIFIED             evidence located and checked in the owning repository
VERIFIED_LIMITED     evidence located for a narrow behavior, not full integration
DECLARED_BY_AUTHOR   declared but not independently verified here
HYPOTHESIS           plausible integration relationship needing test
TOKEN_VAZIO          required evidence not found yet
CLAIM_BLOCKED        cannot be promoted without evidence/test/artifact
```

## Relationship table

| ID | Relationship | State | Safe reading | Blocked claim | Next verification |
|---|---|---|---|---|---|
| RLL-CQ-001 | RLL may export numerical payloads to ChipQuantum | HYPOTHESIS | Candidate data-contract route | RLL already feeds a verified kernel | Verify actual consumer schema in ChipQuantum |
| RLL-CQ-002 | Q16.16 may be the required numeric bridge | HYPOTHESIS / CLAIM_BLOCKED | Possible fixed-point interface | Q16.16 conversion must be implemented now | Define exact scale/range/overflow policy after checking ChipQuantum code/tests |
| RLL-CQ-003 | Attractor count 42 may be shared conceptual invariant | DECLARED_BY_AUTHOR | Cross-repo invariant candidate | 42-attractor implementation is complete | Verify attractor table, tests and build logs in ChipQuantum |
| CQ-TX-001 | ChipQuantum binaries may run under Termux/mobile | HYPOTHESIS | Runtime integration candidate | Mobile execution is validated | Verify build artifact, ABI, loader path and runtime logs |
| TX-RLL-001 | Termux/mobile logs may feed back into RLL audit | HYPOTHESIS | Feedback/attestation route | Mobile result validates RLL | Define log schema, checksum and ingestion path |
| RLL-DATA-001 | `data/raw/data.json` absence blocks calc-data workflow | VERIFIED_LIMITED | Guarded input behavior; not necessarily a bug | Missing file proves data failure | Check workflow definition and intended input policy before adding data |
| RLL-DATA-002 | Synthetic fallback may help beta tests | CLAIM_BLOCKED | Only useful if explicitly synthetic | Synthetic fallback satisfies real-data validation | Keep synthetic output outside real-data claim paths |
| RLL-VEC-001 | RLL sqrt3_2 kernel documents the geometric/cosmological invariant; Vectras executes it as Q16.16 freestanding | HYPOTHESIS | Candidate architecture split; RLL owns science, Vectras owns runtime | Vectras integration is production-ready | Verify Vectras build, ARM freestanding tests and rollback paths before any merge |
| RLL-VEC-002 | Cosmology pivot (a_h, z_h) belongs to RLL; Vectras references the numeric constants only | HYPOTHESIS | Candidate responsibility boundary | Pivot is validated cosmological discovery | Define cross-reference link in Vectras pointing to docs/invariants/sqrt3_2_kernel.md |
| RLL-VEC-003 | PR Vectras #1032 removes cosmological/pivot material; equivalent coverage must stay in RLL | CLAIM_BLOCKED | Migration path candidate; no regressions | Tests removed without replacement are acceptable | Check that all removed tests have equivalent contracts in RLL before approving Vectras #1032 |
| RLL-VEC-004 | RLL PR #426 Real Data Contract CI failure blocks promotion of sqrt3_2 pivot as real-data result | CLAIM_BLOCKED | CI failure is a blocker, not a finding | Real Data Contract CI failure does not block the kernel | Check CI failure per docs/HOTFIX_REAL_VALIDATION_DATA_CONTRACT_2026-05-22.md before promoting any pivot result |

## Implantation policy

A relationship can become an issue, code change, workflow, or test only when it has:

```text
owner repo
source path
evidence state
reproduction or citation
safe next action
claim boundary
```

## Safe beta tester workflow

```text
1. Choose one relationship ID.
2. Verify the owning repository directly.
3. Record path, commit, test/log, or TOKEN_VAZIO.
4. Add a small issue or audit note.
5. Implement only the narrow verified fix.
6. Keep scientific/hardware claims blocked until reproducible artifacts exist.
```

## Do not do

```text
Do not treat this registry as proof of working integration.
Do not use it to claim production readiness.
Do not use RLL documentation alone to change ChipQuantum or Termux behavior.
Do not satisfy real-data gates with synthetic fixtures.
Do not convert hypotheses into bugs without verification.
```

## Good implantation summary

The good part to implant is not the entire master document as authority.

The good part is the method:

```text
relationship -> evidence state -> verification -> small fix -> test -> artifact -> claim gate
```

## Final boundary

This registry improves auditability and beta-test coordination. It does not validate RLL, ChipQuantum, Termux integration, hardware execution, or cosmological claims.
