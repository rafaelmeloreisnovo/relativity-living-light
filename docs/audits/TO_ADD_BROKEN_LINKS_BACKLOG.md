# to_Add Broken Links Backlog

## Status

`audit_backlog / historical_intake / claim_boundary`

## Purpose

This backlog promotes the historical `to_Add/TODO_GAPS.md` list into an auditable location without moving or deleting the original file.

The source list records links or paths that were missing in the historical ZIP intake. This backlog does not claim that every link is still broken in the current repository tree.

## Claim boundary

```text
claim_allowed=false
This is a repository-audit backlog, not scientific evidence.
Broken links do not validate or refute RLL.
Historical missing paths must be rechecked before repair, redirect or archival closure.
```

## Source

```text
to_Add/TODO_GAPS.md
```

## Recheck batch 2026-07-02 — source documents

This batch checks only whether the documents that contain historical broken-link entries still exist in the current tree. It does not yet verify every link target.

| Source document | Current state | Evidence |
|---|---|---|
| `COMPREHENSIVE_REPOSITORY_ANALYSIS.md` | `SOURCE_FOUND_CURRENT` | file exists on `main`; fetched 2026-07-02 |
| `docs/INDICE_MESTRE.md` | `SOURCE_FOUND_CURRENT` | file exists on `main`; fetched 2026-07-02 |
| `docs/README_HISTORICO_INTEGRAL_47d054c.md` | `SOURCE_FOUND_CURRENT` | file exists on `main`; fetched 2026-07-02 |
| `docs/README_ROOT_LEGACY_ARCHIVE.md` | `SOURCE_FOUND_CURRENT` | file exists on `main`; fetched 2026-07-02 |

Recheck conclusion:

```text
The source documents are present in the current repository tree.
The link targets remain PENDING_RECHECK until checked individually.
No link repair, redirect, deletion, placeholder creation or scientific claim is made by this batch.
```

## Items requiring target recheck

### COMPREHENSIVE_REPOSITORY_ANALYSIS.md

- `./ANALISE_COMPLETA/` resolved historically to `relativity-living-light-main/ANALISE_COMPLETA` and was marked missing in the ZIP intake.

### docs/INDICE_MESTRE.md

- `../news/archive_legacy/` resolved historically to `relativity-living-light-main/news/archive_legacy` and was marked missing in the ZIP intake.

### docs/README_HISTORICO_INTEGRAL_47d054c.md

- `ANALISE_COMPLETA/00_INDICE_MESTRE.md`
- `docs/BOOSTERS.md`
- `docs/ANALISE_ARTIGO_NATURE_PT.md`
- `docs/NATURE_ARTICLE_ANALYSIS.md`
- `docs/ARTICLE_ANALYSIS_SUMMARY.md`
- `docs/CONCEPTUAL_FRAMEWORK.md`
- `docs/ANALYSIS_INDEX.md`
- `docs/REFERENCES.md`
- `...`

These were marked missing in the historical ZIP intake, often because paths resolved under `docs/docs/` or `docs/ANALISE_COMPLETA/`.

### docs/README_ROOT_LEGACY_ARCHIVE.md

- `ANALISE_COMPLETA/00_INDICE_MESTRE.md`
- `docs/BOOSTERS.md`
- `docs/ANALISE_ARTIGO_NATURE_PT.md`
- `docs/NATURE_ARTICLE_ANALYSIS.md`
- `docs/ARTICLE_ANALYSIS_SUMMARY.md`
- `docs/CONCEPTUAL_FRAMEWORK.md`
- `docs/ANALYSIS_INDEX.md`
- `docs/REFERENCES.md`
- `...`

These were marked missing in the historical ZIP intake, often because paths resolved under `docs/docs/` or `docs/ANALISE_COMPLETA/`.

## Audit states

| State | Meaning |
|---|---|
| `PENDING_RECHECK` | Item copied from historical intake and not yet verified against current tree. |
| `SOURCE_FOUND_CURRENT` | The document containing a historical broken-link entry exists in the current tree. |
| `SOURCE_MISSING_CURRENT` | The document containing a historical broken-link entry is absent from the current tree. |
| `BROKEN_CURRENT` | Recheck confirms the link target is still broken now. |
| `RESOLVED_CURRENT` | Recheck confirms the link target now resolves. |
| `REDIRECT_RECOMMENDED` | A current canonical target exists and a redirect/update should be proposed. |
| `ARCHIVE_ONLY` | Historical link should remain documented but not repaired as active navigation. |
| `TOKEN_VAZIO_TARGET` | No coherent current target has been located yet. |

## Default target state

```text
PENDING_RECHECK
```

## Safe next step

```text
Check the target paths one by one against the current tree.
If a canonical target exists, propose a redirect/update.
If no target exists, mark TOKEN_VAZIO_TARGET.
Do not create empty placeholder folders just to silence a broken link.
Do not treat broken links as scientific evidence.
```
