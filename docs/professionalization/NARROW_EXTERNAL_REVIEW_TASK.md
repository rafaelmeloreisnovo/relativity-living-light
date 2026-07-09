# Narrow External Review Task

## Status

`review_task / narrow_scope / claim_boundary`

## Purpose

This document turns the external review packet into one concrete, low-risk review task.

It is designed for a university reviewer, research advisor, reproducibility auditor or technical collaborator who can spend limited time reviewing the repository without being asked to validate the whole theory.

## Task name

```text
Evidence-boundary audit for the professionalization layer
```

## Task goal

Verify whether the professional-facing documents correctly preserve the difference between:

```text
research program
validated physical theory
institutional readiness
institutional acceptance
professional presentation
scientific proof
```

## Scope

Review only these files:

```text
docs/professionalization/README.md
docs/professionalization/INSTITUTIONAL_READINESS_DOSSIER.md
docs/professionalization/PROFESSIONAL_DOCUMENT_QUALITY_STANDARD.md
docs/professionalization/EXTERNAL_REVIEW_PACKET.md
docs/professionalization/PROFESSIONAL_DOCUMENTS_REGISTRY.yml
docs/governance/PROFESSIONALIZATION_CHARTER_LINK.md
```

Optional governance reference:

```text
docs/governance/OPERATIONAL_EXCELLENCE_INTEGRITY_CHARTER.md
docs/yml/YML_ONTO_EPISTEMIC_REGISTRY.md
```

## Out of scope

This task does not review:

- cosmological correctness;
- numerical results;
- model comparison;
- physical validity;
- legal/IP status;
- market valuation;
- full repository architecture;
- all historical authorial files.

## Reviewer procedure

```text
1. Read the scoped files.
2. Identify every place where the documents describe RLL's value.
3. Classify each value statement as one of:
   - safe professional framing;
   - scientific claim;
   - legal/commercial claim;
   - TOKEN_VAZIO / needs evidence.
4. Check whether each strong statement has a visible claim boundary.
5. Check whether external review is clearly separated from endorsement.
6. Check whether institutional readiness is clearly separated from acceptance.
7. Write a short review note using the output template below.
```

## Acceptance criteria

The task passes if the reviewer can answer **yes** to all items:

```text
[ ] The professionalization layer does not claim RLL is validated.
[ ] The institutional dossier separates readiness from acceptance.
[ ] The external review packet separates routing from endorsement.
[ ] The registry blocks market/legal/scientific overclaim.
[ ] Missing evidence is not hidden for presentation quality.
[ ] The next action remains narrow and reviewable.
```

## Failure criteria

The task fails if any file implies that:

```text
professional polish = scientific validation
external review route = external endorsement
institutional readiness = institutional acceptance
authorship/provenance = physical truth
documentation = market valuation
governance note = legal conclusion
```

## Reviewer output template

```markdown
# Evidence-Boundary Audit Note

## Reviewer role

TOKEN_VAZIO

## Files reviewed

TOKEN_VAZIO

## Pass/fail

TOKEN_VAZIO

## Strongest safe framing found

TOKEN_VAZIO

## Strongest overclaim risk found

TOKEN_VAZIO

## Required correction, if any

TOKEN_VAZIO

## Recommended next narrow task

TOKEN_VAZIO
```

## Expected output state

A completed review should produce one of:

| Output state | Meaning |
|---|---|
| `PASS_WITH_BOUNDARIES` | Professional layer is safe enough for limited external review |
| `PASS_WITH_MINOR_EDITS` | Small wording fixes needed |
| `CLAIM_BOUNDARY_WEAK` | Some statements risk overclaim |
| `REVIEW_BLOCKED` | Missing documents, unclear boundary or unstable scope |

## Repository action after review

If the task passes:

```text
- mark the professionalization layer as external_review_route_ready;
- do not promote scientific claims;
- choose one scientific or reproducibility task separately.
```

If the task fails:

```text
- correct only the weak wording or missing boundary;
- do not expand scope;
- do not move to scientific claims.
```

## Final boundary

This task audits framing and documentation boundaries only.

It does not validate RLL, refute RLL, determine market value, create legal rights, replace peer review or replace institutional acceptance.
