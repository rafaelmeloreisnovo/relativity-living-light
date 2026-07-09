# Architecture Operational Schema — RLL

## Status

`operational_schema / metadata_ready / claim_boundary`

**Version:** 2.0  
**Updated UTC:** 2026-07-02  
**Audience:** researchers, developers, maintainers, reviewers, educators and general readers.

---

## 1. Relation to root architecture

This document is an operational companion to:

```text
ARCHITECTURE.md
```

`ARCHITECTURE.md` is the root architecture boundary. This file may explain operational navigation, reader paths, diagrams and procedures, but it must not override the root claim boundary.

---

## 2. Claim boundary

```text
claim_allowed=false
architecture_document=true
scientific_validation=false
market_valuation=false
external_endorsement=false
peer_review_acceptance=false
```

This file does not prove RLL, does not validate a cosmological model, does not establish superiority over LCDM/wCDM/CPL, and does not certify FAIR, TRL, ROI or Big-Tech compliance as completed external facts.

Professional formatting improves reviewability. It is not evidence by itself.

---

## 3. Corrected executive view

Relativity Living Light is a multidisciplinary, claim-gated research repository. Its current defensible value is architectural and methodological:

```text
hypothesis organization
traceability
claim boundaries
real-data and synthetic-data separation
pipeline and validator discipline
auditability
external-review readiness as a route, not endorsement
```

Allowed statement:

```text
RLL is organized as a falsifiable research program with documentation, data contracts, scripts, registries, audits and claim gates.
```

Blocked statement:

```text
RLL is already scientifically validated against DESI, Pantheon+, Planck/CMB or other data as a final cosmological result.
```

---

## 4. Reader paths

| Reader | Entry | Purpose | Boundary |
|---|---|---|---|
| General reader | `README.md` | understand scope | no final proof implied |
| Researcher | `docs/INDICE_MESTRE.md`, current result docs | evaluate evidence | current results remain bounded |
| Developer | `scripts/`, `tools/`, `tests/` | reproduce checks | passing tests is not model truth |
| Auditor | `docs/audits/`, `docs/yml/`, `docs/governance/` | verify provenance | audit note is not automatic proof |
| Educator | `docs/canonicos/`, glossary/FAQ docs when present | explain concepts | metaphor is not validation |
| Historical reviewer | `to_Add/` and migration ledgers | preserve provenance | historical intake is not current science root |

---

## 5. Operational layers

```text
[Public orientation]
README.md, ARCHITECTURE.md, professionalization docs
        ↓
[Navigation and traceability]
docs/INDICE_MESTRE.md, docs/RLL_TRACEABILITY_MAP.md, inventories
        ↓
[Governance and claim boundaries]
docs/governance/, docs/yml/, docs/professionalization/
        ↓
[Audits and migration records]
docs/audits/, to_Add migration ledgers, placement registries
        ↓
[Scientific and methodological layer]
current result tables, falsifiability matrices, model notes
        ↓
[Data and evidence layer]
data/real/, data/inputs/, data/results/, manifests, checksums
        ↓
[Execution layer]
scripts/, tools/, tests/, .github/workflows/
        ↓
[Historical intake]
to_Add/, legacy notes, drafts and original bundles
```

Every layer has a different authority level. A document at a higher presentation layer cannot promote a claim that is blocked by the evidence layer.

---

## 6. Evidence flow

```text
claim or input
  → source/provenance registration
  → contract/schema validation when applicable
  → execution or structural check
  → output artifact
  → baseline/model comparison
  → uncertainty/covariance when applicable
  → claim boundary
  → audit/review state
  → VERIFIED, VERIFIED_LIMITED, DECLARED_BY_AUTHOR, TOKEN_VAZIO, CONTRADICTION or CLAIM_BLOCKED
```

---

## 7. Epistemic states

| State | Meaning |
|---|---|
| `VERIFIED` | Evidence is located and traceable. |
| `VERIFIED_LIMITED` | Evidence is located for a narrow behavior, but does not validate the whole relationship, integration or model. |
| `DECLARED_BY_AUTHOR` | Declared, but not independently established in current evidence. |
| `TOKEN_VAZIO` | Required evidence is missing or intentionally blank. |
| `CONTRADICTION` | Evidence contradicts the claim. |
| `METADATA_READY` | Organized or parseable, but not scientific validation. |
| `SYNTHETIC_ONLY` | Mock, toy, example or synthetic material only. |
| `CLAIM_BLOCKED` | Claim cannot be promoted under current evidence. |
| `AUDIT_PENDING` | Needs recheck. |
| `REAL_VALIDATED_BLOCKED` | Real validation requires source, execution, metric, baseline, uncertainty/covariance and boundary. |

---

## 8. Operational rules

### 8.1 Documentation changes

```text
state purpose and audience
state claim_allowed and claim_blocked
link canonical files
avoid unsupported scores or maturity labels
preserve historical context when relevant
commit narrow changes
```

### 8.2 Data and result changes

```text
separate real, synthetic, toy, example and historical data
record source and provenance
add checksum/manifest when possible
avoid silent overwrite of canonical outputs
block claims until metric, baseline and uncertainty/covariance are available
```

### 8.3 Cross-repo relationship registries

```text
relationship rows must name an explicit next verification action
accepted action verbs: Verify, Define, Check, Keep
VERIFIED_LIMITED is allowed only for narrow observed behavior
VERIFIED_LIMITED must not be read as validated integration
blocked claims must remain present for non-verified relationships
```

### 8.4 to_Add material

```text
classify before moving
preserve original intake
promote only through registry and audit
mark historical reports as historical
never treat to_Add/ as current scientific execution root
```
