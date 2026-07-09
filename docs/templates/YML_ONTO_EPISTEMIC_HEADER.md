# YML Onto-Epistemic Header Template Notes

Use these fields when classifying YAML or YML artifacts.

## Ontology fields

- artifact_kind
- system_role
- canonical_path
- lifecycle
- owner_layer
- canonical
- duplicate_of
- consumed_by
- produced_by

## Epistemic fields

- default_state
- allowed_states
- current_state
- claim_allowed
- claim_blocked
- evidence_required_for_promotion
- promotion_rule
- claim_boundary

## Allowed states

- VERIFIED
- DECLARED_BY_AUTHOR
- TOKEN_VAZIO
- CONTRADICTION
- METADATA_READY
- REAL_VALIDATED_BLOCKED
- SYNTHETIC_ONLY
- CLAIM_BLOCKED
- AUDIT_PENDING

## Boundary

Metadata-ready does not imply real validation. Promotion requires traceable source, hash or artifact, command, metric, baseline or adversary, uncertainty policy when applicable, and explicit claim boundary.
