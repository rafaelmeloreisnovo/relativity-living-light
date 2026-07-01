# Root Artifact Classification

Status: `governance_record / operational_control_layer`

Purpose: classify loose root-level artifacts without moving, deleting, renaming, or changing their scientific content. This document is an operational index only; it does not validate RLL, alter equations, or promote any artifact to real-data evidence.

## Allowed classes

| Class | Meaning |
|---|---|
| `canonical_entrypoint` | A root file that intentionally guides users toward repository navigation or primary context. |
| `validation_artifact` | A validation plan, status, protocol, or evidence-routing artifact. |
| `governance_record` | A repository organization, migration, audit, or decision record. |
| `legacy_mirror` | A preserved copy or mirror retained for continuity or historical traceability. |
| `raw_authorial` | Author-originated conceptual, mathematical, multilingual, or exploratory material preserved as source expression. |
| `operational_config` | A root-level configuration file used by automation or validation routing. |
| `audit_pending` | A root artifact whose final purpose, provenance, or canonical destination remains unresolved. |

## Classification table

| Root artifact | Class | Operational handling |
|---|---|---|
| `CAMINHOS_VALIDACAO_NOVOS.yml` | `operational_config` | Keep at root until validation routing is consolidated; treat as automation/config input, not as scientific proof. |
| `COMPREHENSIVE_REPOSITORY_ANALYSIS.md` | `governance_record` | Preserve as repository-level analysis and migration context. |
| `FALSIFIABILITY_PROTOCOL.md` | `validation_artifact` | Treat as a falsifiability/claim-boundary protocol; do not use it to declare validation without real-data metrics. |
| `GOVERNANCE_REORG_DRAFT.md` | `governance_record` | Treat as a draft governance/reorganization record until superseded by a canonical governance index. |
| `VALIDATION_STATUS.md` | `validation_artifact` | Treat as validation-status routing; status language must remain bounded by current evidence. |
| `NEXT_RLL_VALIDATION_STEP.md` | `validation_artifact` | Treat as next-action guidance for validation, not as completed validation. |
| `Matemática.md` | `raw_authorial` | Preserve as authorial mathematical material; do not normalize or relocate in this control PR. |
| `MathRaf.md` | `raw_authorial` | Preserve as authorial mathematical/conceptual material under future provenance review. |
| `Numprimod.md` | `raw_authorial` | Preserve as authorial numerical/prime-number material under future provenance review. |

## Control rules

- Do not move or delete classified root artifacts as part of this document.
- Do not change scientific equations when classifying artifacts.
- Do not infer that a classified artifact is validated real-data evidence.
- Use this table as a lightweight routing layer for future cleanup, inventory, and governance PRs.
