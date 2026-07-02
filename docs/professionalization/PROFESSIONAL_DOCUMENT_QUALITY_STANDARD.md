# Professional Document Quality Standard

## Status

`documentation_standard / professional_quality_gate / claim_boundary`

## Purpose

This standard defines the minimum quality expected from professional-facing documents in the Relativity Living Light repository.

It is a documentation-quality artifact. It does not validate RLL, does not promote scientific claims and does not replace peer review.

## Core rule

```text
A professional document must make review easier and overclaim harder.
```

## Required front matter by meaning

Each professional-facing document should answer these questions near the top:

| Field | Required meaning |
|---|---|
| Title | What document this is |
| Status | Governance/science/data/audit/professionalization state |
| Audience | Who should read it |
| Purpose | Why the document exists |
| Scope | What the document covers |
| Evidence state | What supports it and what remains missing |
| Claim allowed | What may safely be inferred |
| Claim blocked | What must not be inferred |
| Next action | The smallest responsible follow-up |

## Recommended document header

```markdown
# DOCUMENT TITLE

## Status

`TOKEN_VAZIO`

## Audience

- TOKEN_VAZIO

## Purpose

TOKEN_VAZIO

## Scope

TOKEN_VAZIO

## Evidence state

| Item | State | Evidence |
|---|---|---|
| TOKEN_VAZIO | TOKEN_VAZIO | TOKEN_VAZIO |

## Claim allowed

TOKEN_VAZIO

## Claim blocked

TOKEN_VAZIO

## Next responsible action

TOKEN_VAZIO
```

## Quality levels

| Level | Meaning | Minimum requirements |
|---|---|---|
| `draft` | Early document | purpose and claim boundary visible |
| `review_ready` | Ready for internal review | evidence table, blocked claims, next action |
| `institutional_ready` | Ready for external institution | concise summary, references, provenance, limitations |
| `canonical` | Authoritative repository document | linked from index, reviewed, stable path, update rule |
| `deprecated` | Preserved but no longer primary | pointer to replacement, reason, date/commit |

## Evidence-state vocabulary

Use explicit states rather than ambiguous prose:

```text
VERIFIED
DECLARED_BY_AUTHOR
TOKEN_VAZIO
CONTRADICTION
METADATA_READY
CLAIM_BLOCKED
SYNTHETIC_ONLY
AUDIT_PENDING
REAL_VALIDATED_BLOCKED
```

## Writing standard

Professional documents should be:

- concise before detailed;
- explicit about uncertainty;
- separated into evidence, interpretation and action;
- free of unsupported superiority claims;
- clear about whether they are scientific, symbolic, governance, operational or authorial;
- linked to canonical evidence when possible;
- readable by someone outside the project.

## Forbidden patterns

Avoid these patterns:

```text
Passing CI means science is validated.
A metaphor proves a scientific model.
A large repository proves correctness.
A timestamp proves physical truth.
An institutional-looking document implies institutional acceptance.
A smoke test implies robust validation.
A missing contradiction implies confirmation.
```

## Required limitation language

When a document discusses external value, institutional readiness, legal/IP questions or commercial potential, it must include a boundary like:

```text
This document is not legal advice, not a valuation, not a patentability opinion, not a peer-review decision and not a scientific validation of RLL.
```

When a document discusses science, it must include a boundary like:

```text
This document does not validate RLL unless it links to real data, baseline, metric, uncertainty/covariance where applicable, reproducible command, output artifact and falsification boundary.
```

## Review checklist

Before marking a professional document as review-ready, check:

```text
[ ] It states audience and purpose.
[ ] It states claim allowed and claim blocked.
[ ] It separates fact, interpretation and next action.
[ ] It uses TOKEN_VAZIO instead of invented support.
[ ] It avoids market/legal/scientific overclaim.
[ ] It links to canonical source documents when possible.
[ ] It preserves limitations and negative results.
[ ] It names the next responsible action.
```

## Final boundary

This standard improves document quality and reviewability.

It does not:

- make RLL true;
- make a document institutional-approved;
- assign commercial value;
- replace scientific review;
- replace legal review;
- replace external reproducibility.
