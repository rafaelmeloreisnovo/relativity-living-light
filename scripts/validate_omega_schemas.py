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
    print("OK: Omega schema reference layer passed minimal validation")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
