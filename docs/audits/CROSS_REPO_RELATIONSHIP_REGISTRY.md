# Cross-Repo Relationship Registry

## Status

`beta_relationship_registry / evidence_gated / no_claim_promotion`

## Purpose

This registry preserves the useful part of the unified ecosystem map: it records possible relationships among repositories without treating them as validated integration.

The machine-readable articulation contract is `knowledge_ecosystem/session_operating_system.yml`. It organizes the complete-session groups, public/private boundaries, microcommit plan and traceability chain. It does not replace direct verification in the owning repositories.

Repositories in scope:

```text
instituto-Rafael/relativity-living-light
rafaelmeloreisnovo/papers
rafaelmeloreisnovo/ChipQuantum
rafaelmeloreisnovo/termux-app-rafacodephi
rafaelmeloreisnovo/Cosmos
rafaelmeloreisnovo/TeoremasTesesTeorias
rafaelmeloreisnovo/GAIA_phi
rafaelmeloreisnovo/RafPolimata
rafaelmeloreisnovo/Rafaelia_Private
rafaelmeloreisnovo/RafCoder
rafaelmeloreisnovo/Vectras-VM-Android
```

Names beyond files read directly in this audit remain `DECLARED_BY_AUTHOR` or `TOKEN_VAZIO` until the owning repository and path are verified.

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
| RLL-VEC-001 | RLL sqrt3_2 kernel documents the geometric/cosmological invariant; Vectras executes it as Q16.16 freestanding | HYPOTHESIS | Candidate architecture split; RLL owns science, Vectras owns runtime | Vectras freestanding build and ARM tests not yet confirmed in this registry | Verify Vectras build, ARM freestanding tests and rollback paths before any merge |
| RLL-VEC-002 | Cosmology pivot (a_h, z_h) belongs to RLL; Vectras references the numeric constants only | HYPOTHESIS | Candidate responsibility boundary | Pivot is validated cosmological discovery | Define cross-reference link in Vectras pointing to docs/invariants/sqrt3_2_kernel.md |
| RLL-VEC-003 | PR Vectras #1032 removes cosmological/pivot material; equivalent coverage must stay in RLL | CLAIM_BLOCKED | Migration path candidate; no regressions | Tests removed without replacement are acceptable | Check that all removed tests have equivalent contracts in RLL before approving Vectras #1032 |
| RLL-VEC-004 | RLL PR #426 Real Data Contract CI failure blocks promotion of sqrt3_2 pivot as real-data result | CLAIM_BLOCKED | CI failure is a blocker, not a finding | Real Data Contract CI failure does not block the kernel | Check CI failure per docs/HOTFIX_REAL_VALIDATION_DATA_CONTRACT_2026-05-22.md before promoting any pivot result |
| SES-RLL-001 | Cosmology opens the session and RLL provides the first scientific body, while the complete session crosses additional domains | DECLARED_BY_AUTHOR / CLAIM_BLOCKED | Reading order and scope declared by Rafael | All session domains are already scientifically unified by RLL | Verify every cross-domain relation against its owning source, units, material and falsifier |
| RLL-PAP-001 | Public RLL may point to the private `papers` research engine without copying its private formulas or sessions | VERIFIED_LIMITED | Public pointer and private-content boundary are structurally represented | Public RLL contains the full private research corpus | Verify private paths and commits inside `papers`; keep public content pointer-only |
| PAP-ML-001 | `papers` contains Exacordex/Raefaelos, T7, ARM32/NEON and mathematical research documents | VERIFIED_LIMITED | Repository README and selected private paths were read through authorized access | Every listed engine is tested, correct or scientifically validated | Verify builds, tests, binaries, ABI and formula-to-code links in the owning repository |
| RLL-PHO-001 | Photonic, magnetic, acoustic, plasma and jet mechanisms may be organized through field, gradient and energy-momentum transfer relations | HYPOTHESIS / CLAIM_BLOCKED | Cross-scale mathematical and operational comparison candidate | These mechanisms are one physical phenomenon or validate RLL | Define carrier, medium, scale, units, dataset, safety boundary and falsifier for each mechanism |
| SES-GPT-001 | GPT session groups may be indexed as one evolving interaction with corrections, sources and evidence states | HYPOTHESIS / CLAIM_BLOCKED | Candidate contextual organization method | Hidden GPT weights, tokens or private metadata were read or reconstructed | Verify only user-provided/exported session pointers; keep inaccessible metadata TOKEN_VAZIO |
| RLL-KOS-001 | `session_operating_system.yml` links session groups to sources, concepts, operations, artifacts, states and destinations | VERIFIED_LIMITED | Machine-readable organizational contract with schema, validator, tests and rollback plan | The contract proves cross-repo integration or scientific truth | Check generated audit artifact and select one narrow relationship for owning-repo verification |
| PRIV-001 | Private repositories must be represented in public RLL through pointers and evidence states only | VERIFIED_LIMITED | Enforced structural disclosure boundary | Public registry may copy private formulas, raw prompts or unsafe protocols | Keep validator fail-closed and Verify private content only inside the authorized owning repository |

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
Do not use RLL documentation alone to change another repository's behavior.
Do not satisfy real-data gates with synthetic fixtures.
Do not convert hypotheses into bugs without verification.
Do not copy private session text or formulas into the public registry.
Do not create a second orchestration workflow when the existing validator can be extended.
```

## Good implantation summary

The good part to implant is not the entire master document as authority.

The good part is the method:

```text
relationship -> evidence state -> verification -> small fix -> test -> artifact -> claim gate
```

The complete-session articulation adds:

```text
session group -> source -> concept -> formula/model -> operation -> material -> artifact -> test/log -> state -> boundary -> destination -> next action
```

## Final boundary

This registry improves auditability and beta-test coordination. It does not validate RLL, private papers, ChipQuantum, Termux, Vectras, hardware execution, GPT internals, photonic/plasma mechanisms or cosmological claims.
