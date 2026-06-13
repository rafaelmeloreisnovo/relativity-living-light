# RLL 1234.zip Chunk Text Audit

Status: text-source audit placeholder.

Purpose: treat `1234.zip` as a text evidence source without promoting unread content to scientific claim.

## 1. Current evidence

The uploaded/session-visible checksum listing identifies text chunks named:

```text
part_01.txt
part_02.txt
part_03.txt
part_04.txt
part_05.txt
part_06.txt
part_07.txt
part_08.txt
part_09.txt
part_10.txt
```

Each listed part has a SHA-256 hash in the external checksum record.

This document does not yet claim the content of those parts. It only reserves the audit path.

## 2. Claim states

| Item | Status | Note |
|---|---|---|
| `1234.zip` exists as a user-provided archive | VERIFIED in session/upload context |
| `part_01.txt` through `part_10.txt` are listed in checksum text | VERIFIED in session/checksum context |
| Full text content of all chunks | TOKEN_VAZIO |
| Formula ancestry evidence inside chunks | TOKEN_VAZIO |
| Mobile/Termux provenance inside chunks | TOKEN_VAZIO |
| Dates/timestamps inside chunks | TOKEN_VAZIO |
| Relation to RLL v1.0.0 tag | TOKEN_VAZIO |

## 3. Audit target

The audit must read only text content and classify findings into:

| Class | Meaning |
|---|---|
| FORMULA | equations, parameter definitions, derivations |
| PROVENANCE | device, runtime, Termux/mobile, path, command, metadata |
| TIMESTAMP | dates, commit references, DOI references, file times |
| ARTIFACT | image, CSV, figure, plot, table, generated output |
| FALSE_POSITIVE | failed/rejected/partial result |
| CLAIM_BOUNDARY | explicit limits, uncertainty, TOKEN_VAZIO, no-claim text |
| OTHER | relevant but not categorized yet |

## 4. Required output after reading chunks

Future completed audit should produce:

| Output | Purpose |
|---|---|
| chunk inventory | size/hash/status for each part |
| formula hit table | exact chunk + line/snippet + formula component |
| provenance hit table | mobile/Termux/log/path evidence |
| timestamp table | dates and chain-of-custody markers |
| false-positive table | rejected or failed outputs |
| RLL link table | relation to tag, DOI, GitHub commits and later validation |

## 5. Safe claim language

Allowed now:

> `1234.zip` is a text evidence source that must be audited chunk by chunk before being used as proof.

Not allowed yet:

> `1234.zip` proves the RLL formula ancestry.

Not allowed yet:

> `1234.zip` proves mobile/Termux execution.

Not allowed yet:

> `1234.zip` proves scientific correctness.

## 6. Link into traceability

This document is linked from:

- `docs/RLL_TRACEABILITY_MAP.md`
- `docs/INDICE_MESTRE.md`
- `README.md`

Final status remains pending until text chunks are read and cited by exact part/line or local manifest.
