#!/usr/bin/env python3
"""Check the root schema contracts for claim-boundary discipline."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
SCHEMAS_DIR = ROOT / "schemas"


def stop(message: str) -> None:
    raise SystemExit(f"schema validation failed: {message}")


def load_json(path: Path) -> dict[str, Any]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        stop(f"not an object: {path}")
    return data


def require_text(schema: dict[str, Any], key: str, path: Path) -> None:
    value = schema.get(key)
    if not isinstance(value, str) or not value.strip():
        stop(f"missing non-empty {key}: {path}")


def validate_schema(path: Path) -> None:
    schema = load_json(path)

    for key in ["$schema", "$id", "title", "description", "type", "required", "properties"]:
        if key not in schema:
            stop(f"missing {key}: {path}")

    for key in ["$schema", "$id", "title", "description"]:
        require_text(schema, key, path)

    if schema.get("type") != "object":
        stop(f"schema must describe an object: {path}")

    required = schema.get("required")
    properties = schema.get("properties")
    if not isinstance(required, list) or not required:
        stop(f"required must be a non-empty list: {path}")
    if not isinstance(properties, dict) or not properties:
        stop(f"properties must be a non-empty object: {path}")

    description = schema["description"].lower()
    if "structural" not in description or "contract" not in description:
        stop(f"description must declare structural contract status: {path}")

    if "claim_allowed" in required:
        claim_allowed = properties.get("claim_allowed")
        if not isinstance(claim_allowed, dict) or claim_allowed.get("const") is not False:
            stop(f"claim_allowed must be const false: {path}")

    if path.name in {
        "relational_validation_package.schema.json",
        "relation_graph.schema.json",
    }:
        for gate in ["claim_allowed", "next_gate"]:
            if gate not in required:
                stop(f"missing required gate {gate}: {path}")


def validate_readme() -> None:
    readme = SCHEMAS_DIR / "README.md"
    if not readme.exists():
        stop("schemas/README.md is missing")
    text = readme.read_text(encoding="utf-8")
    for term in [
        "schema_parse_success != scientific_validation",
        "claim_allowed=false",
        "python tools/validate_schemas_claim_boundary.py",
    ]:
        if term not in text:
            stop(f"README missing term: {term}")


def main() -> int:
    paths = sorted(SCHEMAS_DIR.glob("*.schema.json"))
    if not paths:
        stop("no schema files found")
    for path in paths:
        validate_schema(path)
    validate_readme()
    print("OK: schemas are structural and claim-bounded")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
