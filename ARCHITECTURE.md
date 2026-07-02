# ARCHITECTURE.md — Relativity Living Light

## Operational Architecture Schema

**Status:** `architecture_schema / metadata_ready / claim_boundary`  
**Version:** 2.0  
**Updated UTC:** 2026-07-02  
**Audience:** researchers, maintainers, reviewers, contributors, auditors, educators and non-specialist readers.

---

## 1. Claim boundary

This file describes repository architecture. It does not validate RLL as a physical or cosmological theory.

```text
architecture_document=true
scientific_validation=false
claim_promotion=false
external_endorsement=false
```

Correct framing:

```text
architecture improves navigation and auditability
architecture does not prove scientific claims
professional presentation does not replace evidence
passing CI does not mean a model is true
```

---

## 2. Why this revision exists

A proposed `ARCHITECTURE_OPERATIONAL_SCHEMA.md` was reviewed. The coherent parts were kept:

```text
layered architecture
audience-aware explanations
canonical directory roles
operational procedures
governance states
onboarding and review paths
plain-language accessibility
```

The following were downgraded or removed unless independently evidenced elsewhere:

```text
no gaps
fixed FAIR score
Big Tech compliant as a completed status
post-PhD quality as proof
peer-ready as acceptance
ROI or valuation claims
final validation against DESI/Pantheon/Planck/CMB
```

---

## 3. Current scientific boundary

The current canonical result is a real-data smoke/sanity comparison, not a final cosmological fit.

Allowed:

```text
The repository can compare LCDM, wCDM, CPL/w0waCDM and RLL in a shared artifact.
The current smoke run keeps claims blocked.
```

Blocked:

```text
RLL is confirmed.
RLL beats LCDM.
RLL beats CPL.
RLL resolves dark energy, H0 or S8.
This architecture file proves the theory.
```

---

## 4. Layered architecture

```text
[Public entry]
README.md, ARCHITECTURE.md, professionalization docs
        ↓
[Governance and claim boundaries]
docs/governance/, docs/professionalization/, docs/yml/
        ↓
[Audits and registries]
docs/audits/, migration ledgers, placement registries
        ↓
[Scientific and methodological documents]
docs/, current result tables, falsifiability matrices
        ↓
[Data contracts and inputs]
data/real/, data/inputs/, manifests, checksums
        ↓
[Pipelines and validation tools]
scripts/, tools/, tests/, .github/workflows/
        ↓
[Results and generated artifacts]
results/, data/results/
        ↓
[Historical intake]
to_Add/, legacy notes, historical drafts
```

Each layer has a different authority level. File existence does not automatically authorize a claim.

---

## 5. Canonical roots

| Root | Role | Boundary |
|---|---|---|
| `README.md` | public orientation | Must not overclaim validation. |
| `ARCHITECTURE.md` | operational schema | Structure, not proof. |
| `docs/governance/` | policy and integrity | Governance is not scientific validation. |
| `docs/professionalization/` | review packaging | Readiness is not acceptance. |
| `docs/yml/` | onto-epistemic registries | Metadata is not validation. |
| `docs/audits/` | audit notes | Audit note needs evidence to become proof. |
| `data/real/` | materialized real inputs | Data still need metric, baseline and uncertainty. |
| `data/inputs/` | canonical inputs | Input is not result. |
| `scripts/` | runners | Execution must avoid silent overwrite. |
| `tools/` | validators and normalizers | Structural validation is not model truth. |
| `.github/workflows/` | CI gates | Passing CI is not cosmological proof. |
| `to_Add/` | historical intake | Provenance only; not canonical execution root. |

---

## 6. Evidence flow

```text
source or historical input
  → registration / manifest / checksum when applicable
  → contract or schema validation
  → pipeline execution or structural validation
  → result artifact
  → model or baseline comparison
  → claim boundary
  → audit or review note
  → promotion, rejection or TOKEN_VAZIO
```

Promotion requires evidence. A cleaner document does not make a claim true.

---

## 7. Epistemic states

| State | Meaning |
|---|---|
| `VERIFIED` | Evidence is located and traceable. |
| `DECLARED_BY_AUTHOR` | Declared, but not independently established. |
| `TOKEN_VAZIO` | Needed evidence is missing or intentionally blank. |
| `CONTRADICTION` | Evidence contradicts the claim. |
| `METADATA_READY` | Organized/parseable, but not scientifically validated. |
| `CLAIM_BLOCKED` | Claim cannot be promoted under current evidence. |
| `SYNTHETIC_ONLY` | Mock/demo/toy material only. |
| `AUDIT_PENDING` | Requires inspection. |
| `REAL_VALIDATED_BLOCKED` | Real validation blocked pending source, execution, metric, baseline, uncertainty and boundary. |

---

## 8. Operational rules

### Documentation

```text
identify artifact kind
state purpose and audience
state claim_allowed and claim_blocked
link canonical paths
avoid unsupported quality scores
commit narrow changes
```

### Data and results

```text
record source and provenance
add checksum or manifest when possible
separate real, synthetic, toy, example and historical material
block claims until metric, baseline and uncertainty exist
```

### to_Add migration

```text
classify before moving
preserve original intake
promote only through registry and audit
mark historical reports as historical
never use to_Add/ as current scientific evidence
```

---

## 9. Accessibility policy

Good architecture should serve expert and non-expert readers. It may use diagrams, glossary-style explanations and simple language. Accessibility must reduce ambiguity, not reduce rigor.

---

## 10. Maintainer checklist

```text
[ ] No final scientific claim is introduced by architecture wording.
[ ] No score or maturity label appears without source and method.
[ ] Synthetic/toy artifacts remain labeled.
[ ] Historical intake remains historical.
[ ] Current result limitations remain visible.
[ ] Next action is narrow and non-destructive.
```

---

## 11. Next coherent evolution

```text
Link this file from a documentation index if needed.
Recheck root-level public files for architecture or validation overclaims.
Keep current scientific result boundaries near public-facing docs.
```

---

## Final rule

```text
Architecture organizes the path to evidence.
Architecture is not evidence by itself.
Coherence first; traceability second; claim last.
```
