#!/usr/bin/env python3
"""Validate the minimal RAFAELIA Omega schema reference layer.

This script intentionally uses only the Python standard library. It checks the
schema files themselves for JSON parseability and required structural markers;
it does not perform full JSON Schema validation of instances.
"""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCHEMA_DIR = ROOT / "schemas"
EXAMPLE_DIR = SCHEMA_DIR / "examples"

EPISTEMIC_STATES = {
    "fact",
    "hypothesis",
    "metaphor",
    "evidence",
    "token_vazio",
    "decision",
}

EXPECTED = {
    "omega_artifact.schema.json": {
        "artifact_id",
        "title",
        "origin_question",
        "context",
        "method",
        "hypotheses",
        "evidence",
        "relations",
        "revisions",
        "limitations",
        "status",
        "next_question",
        "created_at",
        "updated_at",
    },
    "omega_node.schema.json": {
        "node_id",
        "kind",
        "value",
        "semantic_vector_ref",
        "relation_weight",
        "evidence_score",
        "validation_score",
        "confidence",
        "parent",
        "timestamp",
        "hash",
    },
    "omega_relation.schema.json": {
        "relation_id",
        "source_node",
        "target_node",
        "relation_type",
        "evidence",
        "coherence",
        "reproducibility",
        "temporal_stability",
        "weight",
        "status",
        "created_at",
    },
    "omega_schema.json": {
        "omega_system",
        "identity",
        "artifacts",
        "nodes",
        "relations",
        "evidence_chain",
        "governance",
        "audit",
        "rollback",
        "next_state",
    },
}

EXAMPLES = {
    "omega_artifact.fact.example.json": "omega_artifact.schema.json",
    "omega_artifact.hypothesis.example.json": "omega_artifact.schema.json",
    "omega_artifact.metaphor.example.json": "omega_artifact.schema.json",
    "omega_artifact.evidence.example.json": "omega_artifact.schema.json",
    "omega_artifact.token_vazio.example.json": "omega_artifact.schema.json",
    "omega_artifact.decision.example.json": "omega_artifact.schema.json",
    "omega_node.example.json": "omega_node.schema.json",
    "omega_relation.example.json": "omega_relation.schema.json",
    "omega_system.example.json": "omega_schema.json",
}


def load_json(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as handle:
        payload = json.load(handle)
    if not isinstance(payload, dict):
        raise ValueError(f"{path}: top-level JSON value must be an object")
    return payload


def assert_required(schema_name: str, payload: dict) -> None:
    required = set(payload.get("required", []))
    missing = EXPECTED[schema_name] - required
    if missing:
        raise ValueError(f"{schema_name}: missing required fields: {sorted(missing)}")


def assert_schema_header(schema_name: str, payload: dict) -> None:
    for key in ("$schema", "$id", "title", "description", "type"):
        if key not in payload:
            raise ValueError(f"{schema_name}: missing schema header {key}")
    if payload["type"] != "object":
        raise ValueError(f"{schema_name}: expected top-level type object")


def collect_enums(value: object) -> set[str]:
    found: set[str] = set()
    if isinstance(value, dict):
        enum = value.get("enum")
        if isinstance(enum, list):
            found.update(item for item in enum if isinstance(item, str))
        for child in value.values():
            found.update(collect_enums(child))
    elif isinstance(value, list):
        for child in value:
            found.update(collect_enums(child))
    return found


def assert_epistemic_states(schema_name: str, payload: dict) -> None:
    if schema_name not in {"omega_artifact.schema.json", "omega_relation.schema.json"}:
        return
    states = collect_enums(payload)
    missing = EPISTEMIC_STATES - states
    if missing:
        raise ValueError(f"{schema_name}: missing epistemic states: {sorted(missing)}")


def assert_formula_markers(schema_name: str, payload: dict) -> None:
    text = json.dumps(payload, ensure_ascii=False, sort_keys=True)
    if schema_name == "omega_relation.schema.json" and "Peso_relação = Evidência × Coerência × Reprodutibilidade" not in text:
        raise ValueError(f"{schema_name}: canonical relation formula not found")
    if schema_name == "omega_schema.json" and "Ω(t+1) = F(Ω(t), D(t), E(t), P(t))" not in text:
        raise ValueError(f"{schema_name}: canonical Omega equation not found")


def assert_example_required(example_name: str, schema_name: str, payload: dict) -> None:
    missing = EXPECTED[schema_name] - set(payload)
    if missing:
        raise ValueError(f"{example_name}: missing fields required by {schema_name}: {sorted(missing)}")


def assert_example_epistemic_state(example_name: str, payload: dict) -> None:
    if not example_name.startswith("omega_artifact."):
        return
    expected_state = example_name.split(".")[1]
    actual_state = payload.get("status")
    if actual_state != expected_state:
        raise ValueError(f"{example_name}: expected status {expected_state}, found {actual_state}")
    if actual_state not in EPISTEMIC_STATES:
        raise ValueError(f"{example_name}: unsupported epistemic status {actual_state}")


def assert_no_metaphor_evidence_mix(example_name: str, payload: dict) -> None:
    if example_name != "omega_artifact.metaphor.example.json":
        return
    if payload.get("evidence"):
        raise ValueError(f"{example_name}: metaphor examples must not carry evidence entries")
    text = json.dumps(payload, ensure_ascii=False).lower()
    if "metaphor is not evidence" not in text and "metáfora não é evidência" not in text:
        raise ValueError(f"{example_name}: must explicitly state that metaphor is not evidence")


def assert_token_vazio_declares_gap(example_name: str, payload: dict) -> None:
    if example_name != "omega_artifact.token_vazio.example.json":
        return
    text = json.dumps(payload, ensure_ascii=False).lower()
    if "token_vazio" not in text:
        raise ValueError(f"{example_name}: must explicitly declare TOKEN_VAZIO")
    if not any(marker in text for marker in ("lacuna", "missing", "no omega kernel", "não existe", "no runtime")):
        raise ValueError(f"{example_name}: TOKEN_VAZIO example must declare a gap, not a conclusion")


def assert_relation_weight_consistency(example_name: str, payload: dict) -> None:
    if example_name != "omega_relation.example.json":
        return
    expected_weight = payload["evidence"] * payload["coherence"] * payload["reproducibility"]
    if abs(payload["weight"] - expected_weight) > 1e-12:
        raise ValueError(
            f"{example_name}: weight must follow Peso_relação = Evidência × Coerência × Reprodutibilidade"
        )


def validate_examples() -> None:
    for example_name, schema_name in sorted(EXAMPLES.items()):
        path = EXAMPLE_DIR / example_name
        if not path.exists():
            raise FileNotFoundError(f"Missing example fixture: {path}")
        payload = load_json(path)
        assert_example_required(example_name, schema_name, payload)
        assert_example_epistemic_state(example_name, payload)
        assert_no_metaphor_evidence_mix(example_name, payload)
        assert_token_vazio_declares_gap(example_name, payload)
        assert_relation_weight_consistency(example_name, payload)
        print(f"OK: {path.relative_to(ROOT)}")


def main() -> int:
    for schema_name in sorted(EXPECTED):
        path = SCHEMA_DIR / schema_name
        if not path.exists():
            raise FileNotFoundError(f"Missing schema: {path}")
        payload = load_json(path)
        assert_schema_header(schema_name, payload)
        assert_required(schema_name, payload)
        assert_epistemic_states(schema_name, payload)
        assert_formula_markers(schema_name, payload)
        print(f"OK: {path.relative_to(ROOT)}")
    validate_examples()
    print("OK: Omega schema reference layer passed minimal validation")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
