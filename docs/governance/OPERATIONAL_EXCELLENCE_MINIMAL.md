# Operational Excellence Minimal Rules

## Status

`governance_record / operational_excellence / claim_boundary`

## Purpose

This note defines minimal rules for coherent future evolution of the repository.

It improves scientific, bibliographic, authorial, audit and interoperability discipline.

It does not validate or refute any scientific claim.

## Core rule

```text
Do not make the repository look more certain than the evidence allows.
```

## Minimum practices

| Area | Practice |
|---|---|
| Scientific integrity | Separate fact, hypothesis, result, metaphor and claim. |
| Bibliographic integrity | Record source, author, date, identifier and use. |
| Authorial integrity | Preserve names, contribution context, file history and provenance. |
| Usability | Make the next valid command or review path visible. |
| Auditability | Record what changed, why, and what remains blocked. |
| Interoperability | Prefer stable identifiers, manifests, checksums and schema validation. |
| Review discipline | Mark sensitive uncertainty as `TOKEN_VAZIO` or `REVIEW_REQUIRED`. |

## Scientific promotion block

Forbidden promotion:

```text
smoke test -> final validation
metadata-ready -> real validated
mock/synthetic -> observational proof
documentation update -> scientific result
analogy -> evidence
historical priority -> physical truth
```

## Bibliographic record template

```yaml
reference:
  title: TOKEN_VAZIO
  authors: TOKEN_VAZIO
  year: TOKEN_VAZIO
  doi_or_url: TOKEN_VAZIO
  accessed_utc: TOKEN_VAZIO
  source_type: paper | dataset | code | standard | documentation | other
  used_for: TOKEN_VAZIO
  claim_supported: TOKEN_VAZIO
  claim_not_supported: TOKEN_VAZIO
```

## Contribution record template

```yaml
contribution_record:
  artifact_path: TOKEN_VAZIO
  contributor_name: TOKEN_VAZIO
  contribution_type: TOKEN_VAZIO
  contribution_evidence: commit | issue | pull_request | file_history | signed_statement | TOKEN_VAZIO
  claim_allowed: TOKEN_VAZIO
  claim_blocked: TOKEN_VAZIO
```

## Reuse review template

```yaml
reuse_review:
  artifact_path: TOKEN_VAZIO
  source_origin: TOKEN_VAZIO
  terms_or_license: TOKEN_VAZIO
  attribution_needed: TOKEN_VAZIO
  redistribution_state: TOKEN_VAZIO
  derivative_state: TOKEN_VAZIO
  review_required: true
```

## Future assistant rule

When asked for the next coherent GitHub step:

```text
1. Read nearest governance and audit files.
2. Prefer one small coherent change.
3. Preserve provenance, authorial context and source context.
4. Do not delete first; classify first.
5. Do not inflate scientific, authorial, reuse or commercial claims.
6. Mark uncertainty as TOKEN_VAZIO.
7. Add audit notes when regime, canonicity, source or claim boundary changes.
8. Keep the change testable, reversible and explainable.
9. End with FEITO, NAO FEITO and BLOQUEADO.
```

## Final boundary

This document improves operational excellence and future coherent evolution.

It does not:

- validate RLL;
- refute RLL;
- create final scientific proof;
- settle sensitive disputes;
- override existing repository governance;
- replace specialist review.
