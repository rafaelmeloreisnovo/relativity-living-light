# Operational Excellence and Integrity Charter

## Status

`governance_record / operational_excellence / bibliographic_integrity / claim_boundary`

## Purpose

This charter defines practical rules for scientific operational excellence, bibliographic integrity, authorship traceability, privacy, interoperability and AI-assisted repository evolution.

It is a governance artifact. It does not validate RLL, does not create legal rights by itself, does not determine patentability, does not assign commercial terms and does not replace qualified legal, academic or institutional review.

## Core rule

```text
Evidence before claim.
Attribution before reuse.
License before distribution.
Provenance before promotion.
Consent before personal-data exposure.
Audit before reorganization.
Formal review before commercial or legal conclusions.
```

## Reference anchors

This repository should align with recognized structural references where applicable:

- FAIR: findable, accessible, interoperable and reusable digital objects.
- CRediT: structured contributor-role description.
- ICMJE/COPE-style publication ethics: contribution, conflicts, correction, copyright, responsible AI use and misconduct handling.
- SPDX/REUSE-style licensing discipline: machine-readable license and attribution metadata.
- ORCID/ROR/DOI/DataCite-style persistent identifiers where applicable.

These are reference anchors, not automatic compliance claims. Compliance must be checked artifact by artifact.

---

## 1. Scientific operational excellence

| Practice | Rule | Minimum artifact |
|---|---|---|
| Reproducibility | Results should point to command, environment, inputs and outputs. | manifest / report / checksum |
| Robustness | Smoke tests must not be promoted to final fits. | `claim_allowed=false` when preliminary |
| Falsifiability | A hypothesis must name what would count against it. | falsification matrix / negative ledger |
| Version control | Important changes must be committed with scoped messages. | Git commit SHA |
| Baseline | Claims require a comparison target. | LCDM / CPL / baseline / adversary |
| Uncertainty | Metrics without uncertainty remain bounded. | covariance/error/TOKEN_VAZIO marker |
| Negative results | Failed, blocked or negative outcomes remain visible. | negative ledger / audit note |
| No silent promotion | Passing CI is not scientific validation. | explicit claim boundary |

---

## 2. Bibliographic integrity

Required practices:

1. record source title, author, year and URL/DOI when available;
2. record access date for web sources and mutable datasets;
3. separate primary literature, secondary literature, documentation and commentary;
4. do not cite a source as support for a claim it does not make;
5. mark unavailable evidence as `TOKEN_VAZIO`;
6. distinguish exact quote, paraphrase, inference and analogy;
7. avoid fabricated citations, fake DOIs or invented bibliographic metadata;
8. use persistent identifiers when available: DOI, ORCID, ROR, arXiv ID, commit SHA, release tag;
9. keep AI-assisted provenance visible when AI contributes to drafting, refactoring or summarization;
10. for copyrighted sources, quote minimally and prefer summary with citation.

Minimum reference record:

```yaml
reference:
  title: TOKEN_VAZIO
  authors: TOKEN_VAZIO
  year: TOKEN_VAZIO
  identifier: TOKEN_VAZIO
  url: TOKEN_VAZIO
  accessed_utc: TOKEN_VAZIO
  source_type: TOKEN_VAZIO
  supports_claim: TOKEN_VAZIO
  quote_or_paraphrase: TOKEN_VAZIO
  rights_or_license: TOKEN_VAZIO
```

---

## 3. Authorship and contribution traceability

Authorship traceability means preserving who contributed what, when, how and under which evidential boundary.

Required practices:

| Area | Practice |
|---|---|
| Authorship | State who authored, drafted, edited, reviewed, coded or curated when known. |
| Contribution roles | Use CRediT-like roles where practical: conceptualization, methodology, software, data curation, validation, visualization, writing, review/editing. |
| AI assistance | Record when AI helped draft, refactor, summarize, translate or generate scaffolding. |
| Prior art | Record earlier files, commits, notebooks, timestamps, drafts and external references. |
| Similarity review | Mark overlap as `NEEDS_REVIEW`, not automatic wrongdoing or automatic originality. |
| Attribution | Credit upstream datasets, papers, code, libraries and ideas. |

Minimum contribution record:

```yaml
contribution:
  artifact_path: TOKEN_VAZIO
  contributor: TOKEN_VAZIO
  role: TOKEN_VAZIO
  evidence: TOKEN_VAZIO
  timestamp_or_commit: TOKEN_VAZIO
  ai_assisted: TOKEN_VAZIO
  review_status: TOKEN_VAZIO
```

---

## 4. Rights, licensing and commercial caution

This repository may record authorial intent, license preference, provenance and evidence of creation. It must not pretend that a repository note alone creates enforceable legal rights, commercial entitlement, patentability or publication acceptance.

Required practices:

1. every distributed source file should have a clear license path or repository-level license;
2. use SPDX identifiers where possible;
3. keep copyright notices separate from scientific validity claims;
4. do not ingest third-party datasets unless license or terms allow intended use;
5. record dataset license, redistribution terms and citation requirements;
6. patent-sensitive or commercial-sensitive ideas should be documented as provenance, not as legal strategy;
7. commercial terms require separate written instruments and review;
8. suspected attribution problems should be recorded as evidence-review items, not final conclusions without review.

Minimum rights record:

```yaml
rights:
  artifact_path: TOKEN_VAZIO
  rights_holder: TOKEN_VAZIO
  license: TOKEN_VAZIO
  spdx_identifier: TOKEN_VAZIO
  third_party_material: false
  third_party_license: TOKEN_VAZIO
  redistribution_allowed: TOKEN_VAZIO
  attribution_required: TOKEN_VAZIO
  commercial_review_required: TOKEN_VAZIO
```

---

## 5. Independent-inventor caution

Independent work can be lost or misread when provenance is weak.

Operational lesson:

```text
Do not rely on memory alone.
Do not rely on informal recognition alone.
Preserve dated artifacts, source files, commits, witnesses, licenses and review notes.
Record derivations, tests, drafts and comparisons.
Treat recognition as evidence, not as complete validation.
```

This is a provenance rule, not legal advice and not a claim about any specific external party.

---

## 6. Privacy and safe publication

Required practices:

1. do not commit credentials or private access material;
2. do not commit personal data unless necessary, lawful and documented;
3. separate public scientific data from private notes or personal identifiers;
4. redact private contact details unless consent and purpose are clear;
5. mark sensitive imports as `PRIVATE_REVIEW_REQUIRED`;
6. use synthetic fixtures for tests unless real data are licensed, public and safe;
7. record purpose, minimization, retention and access boundary when personal data are necessary.

Minimum privacy record:

```yaml
privacy:
  contains_personal_data: TOKEN_VAZIO
  contains_sensitive_data: TOKEN_VAZIO
  permission_or_basis: TOKEN_VAZIO
  minimization_applied: TOKEN_VAZIO
  public_release_allowed: TOKEN_VAZIO
  redaction_required: TOKEN_VAZIO
```

---

## 7. Interoperability and usability

Required practices:

1. prefer stable ASCII paths for executable and CI-critical files;
2. preserve authorial titles inside document bodies when filenames are normalized;
3. provide README files for major directories;
4. provide examples and dry-run modes for risky scripts;
5. make defaults safe, non-destructive and offline-first where possible;
6. separate raw data, processed data, results, docs, scripts, tools and tests;
7. keep machine-readable registries in YAML/CSV/JSON;
8. keep human-readable explanations in Markdown;
9. prefer small commits with one responsibility each;
10. document failure modes and rollback paths.

Interoperability questions:

```text
Can a human understand the artifact?
Can a script locate the artifact?
Can CI validate the artifact?
Can another repository cite the artifact?
Can a reviewer reconstruct provenance?
Can a license scanner identify rights metadata?
Can a bibliography identify authorship and source?
```

---

## 8. AI next-step evolution rule

When a future user asks an AI assistant for the next coherent GitHub step, apply this rule before editing:

```text
1. Read the nearest governance, audit, registry or claim-boundary file.
2. Choose the smallest useful non-destructive change.
3. Prefer traceability before moving files.
4. Prefer provenance before promoting claims.
5. Prefer tests or validators before new scientific claims.
6. Check license, attribution and privacy risks.
7. Mark unknowns as TOKEN_VAZIO instead of inventing support.
8. Do not state final legal conclusions without review.
9. Do not treat similarity as wrongdoing without evidence and review.
10. Commit with a scoped message and record what remains blocked.
```

Allowed next-step classes:

```text
docs: governance, audit, registry notes
ci: safe validation or linting checks
test: tests for existing behavior
tools: non-destructive validators or manifest generators
data: registries/manifests, not unreviewed data dumps
refactor: only after classification and backup
science: only when evidence, baseline and claim boundary exist
```

Blocked next-step classes:

```text
claim promotion without evidence
license-unknown redistribution
privacy-sensitive publication
commercial/legal assertion without instrument
large reorganization without manifest
silent deletion of authorial material
```

---

## 9. Excellence matrix

| Dimension | Minimum standard | Failure mode prevented |
|---|---|---|
| Usability | README, examples, dry-run | expert-only opacity |
| Reliability | tests, CI, deterministic commands | fragile execution |
| Integrity | hashes, manifests, negative ledgers | hidden manipulation |
| Privacy | redaction, minimization, access control | accidental exposure |
| Auditability | commit SHA, source, reason | unreconstructable history |
| Comfortability | safe defaults, clear paths | hostile workflow |
| Compliance | license/privacy/review states | accidental violation |
| Transparency | claim boundaries and limitations | inflated claims |
| Authorship traceability | contribution records and prior-art trail | uncredited work |
| Interoperability | FAIR/SPDX/CRediT-like metadata | isolated artifacts |

---

## Final boundary

This charter strengthens the repository as a knowledge system.

It does not:

- prove RLL;
- patent RLL;
- assign commercial terms;
- create a final legal conclusion;
- replace legal counsel;
- replace peer review;
- convert authorship into scientific validity;
- convert operational excellence into physical truth.

It does:

- protect provenance;
- improve attribution;
- reduce reuse ambiguity;
- improve auditability;
- improve scientific discipline;
- give future AI steps a safe evolutionary rule.
