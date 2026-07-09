#!/usr/bin/env python3
"""Validate that claim_allowed=true cannot appear without evidence gates.

This is a structural repository guard. It does not validate RLL, execute
cosmology, prove mathematics, select a model, or promote scientific claims.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parents[1]

SCAN_ROOTS = [
    ROOT / "data",
    ROOT / "results",
    ROOT / "docs" / "yml",
    ROOT / "schemas",
]

SUFFIXES = {".json", ".yml", ".yaml"}

EVIDENCE_GROUPS = {
    "source": {
        "source",
        "source_path",
        "source_paths",
        "source_reference",
        "source_signature_ids",
        "primary_source",
        "primary_reference",
        "materialized_data_or_primary_reference",
    },
    "checksum": {
        "checksum",
        "checksums",
        "sha256",
        "raw_sha256",
        "checksum_or_source_signature",
        "input_hash_manifest",
        "source_signature_ids",
    },
    "metric": {"metric", "metrics", "metric_name", "metric_names"},
    "baseline": {"baseline", "baselines", "baseline_or_adversary"},
    "uncertainty": {
        "uncertainty",
        "uncertainty_or_covariance_status",
        "uncertainty_or_error_policy",
        "error_policy",
        "covariance_path",
        "covariance_or_error_model",
    },
    "execution": {
        "command",
        "commands",
        "reproducibility_command",
        "validation_commands",
        "executable_command_or_artifact",
        "ingestion_command",
    },
    "boundary": {"claim_boundary", "claim_blocked", "falsifier", "next_gate"},
}

SKIP_DIRS = {
    ".git",
    ".github",
    "__pycache__",
    ".pytest_cache",
    ".mypy_cache",
    "node_modules",
    ".venv",
    "venv",
}


def fail(message: str) -> None:
    raise SystemExit(f"claim_allowed gate failed: {message}")


def load_document(path: Path) -> Any:
    text = path.read_text(encoding="utf-8")
    if path.suffix == ".json":
        return json.loads(text)
    return yaml.safe_load(text)


def walk_values(value: Any) -> list[Any]:
    found = [value]
    if isinstance(value, dict):
        for child in value.values():
            found.extend(walk_values(child))
    elif isinstance(value, list):
        for child in value:
            found.extend(walk_values(child))
    return found


def has_non_empty_value(value: Any) -> bool:
    if value is True:
        return True
    if value in (None, False):
        return False
    if isinstance(value, str):
        return bool(value.strip()) and "TOKEN_VAZIO" not in value
    if isinstance(value, list):
        return any(has_non_empty_value(item) for item in value)
    if isinstance(value, dict):
        return any(has_non_empty_value(item) for item in value.values())
    return True


def mapping_satisfies_group(mapping: dict[str, Any], names: set[str]) -> bool:
    for key, value in mapping.items():
        if key in names and has_non_empty_value(value):
            return True
    return False


def collect_claim_true_mappings(value: Any) -> list[dict[str, Any]]:
    matches: list[dict[str, Any]] = []
    if isinstance(value, dict):
        if value.get("claim_allowed") is True:
            matches.append(value)
        for child in value.values():
            matches.extend(collect_claim_true_mappings(child))
    elif isinstance(value, list):
        for child in value:
            matches.extend(collect_claim_true_mappings(child))
    return matches


def validate_claim_true_mapping(path: Path, mapping: dict[str, Any]) -> None:
    missing = [
        group
        for group, field_names in EVIDENCE_GROUPS.items()
        if not mapping_satisfies_group(mapping, field_names)
    ]
    if missing:
        rel = path.relative_to(ROOT)
        fail(f"{rel} has claim_allowed=true without evidence groups: {missing}")


def iter_candidate_files() -> list[Path]:
    paths: list[Path] = []
    for root in SCAN_ROOTS:
        if not root.exists():
            continue
        for path in root.rglob("*"):
            if any(part in SKIP_DIRS for part in path.parts):
                continue
            if path.is_file() and path.suffix in SUFFIXES:
                paths.append(path)
    return sorted(paths)


def validate_file(path: Path) -> None:
    data = load_document(path)
    for mapping in collect_claim_true_mappings(data):
        validate_claim_true_mapping(path, mapping)


def main() -> int:
    for path in iter_candidate_files():
        validate_file(path)
    print("OK: claim_allowed=true is evidence-gated or absent")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
