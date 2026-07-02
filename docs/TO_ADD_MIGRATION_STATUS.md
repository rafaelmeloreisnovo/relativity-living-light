# to_Add Migration Status

## Status

`manual_status_note / controlled_legacy_intake / claim_boundary`

## Boundary

```text
claim_allowed=false
to_Add/ is historical intake only
to_Add/ is not an operational science root
new executable logic under to_Add/ is blocked
scientific claims must use canonical paths, not to_Add/ paths
```

## Why this note exists

`to_Add/README.md` references this status file and the validator output path. This note makes the state consultable without claiming that a fresh validator run was executed in this commit.

## Canonical ledger

```text
docs/yml/TO_ADD_MIGRATION_LEDGER.yml
```

The ledger maps the historical Structure D bundle into canonical paths under:

```text
data/pipelines/
data/inputs/
results/
docs/
```

## Validator

```bash
python3 tools/validate_to_add_migration.py
```

The validator is structural only. It checks canonical paths and wrapper targets. It does not execute scientific logic and does not validate RLL.

## Generated output state

Expected generated output:

```text
data/results/to_add_migration_validation.json
```

Current status in this note:

```text
TOKEN_VAZIO_GENERATED_OUTPUT
```

Reason: this commit does not claim the validator was run.

## Safe next step

```text
Run python3 tools/validate_to_add_migration.py.
If it passes, commit or upload the generated validation JSON/status.
If it fails, correct only missing canonical paths or wrapper targets.
Do not add new execution logic under to_Add/.
Do not use to_Add/ as evidence for current scientific claims.
```
