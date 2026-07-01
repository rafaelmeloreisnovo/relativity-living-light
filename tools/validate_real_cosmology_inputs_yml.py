#!/usr/bin/env python3
"""Validate the committed real cosmology YAML input contract.

This is a structural/provenance gate. It checks that the YAML points to real,
committed local inputs and explicitly preserves claim boundaries. It does not
run a cosmological fit or declare a model scientifically validated.
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "data" / "real" / "cosmology" / "real_cosmology_inputs.yml"
SIGNATURES = ROOT / "data" / "real" / "cosmology" / "real_source_signatures.json"

REQUIRED_TOP_LEVEL = {
    "schema",
    "status",
    "purpose",
    "claim_boundary",
    "default_execution",
    "inputs",
    "failsafe",
    "artifacts",
}
REQUIRED_INPUT_FIELDS = {
    "dataset_id",
    "axis",
    "domain",
    "state",
    "local_path",
    "observable_columns",
    "error_policy",
    "primary_source",
    "repository_consumers",
    "required_checks",
    "claim_blocked",
}

GLOBAL_BOUNDARY_TERMS = ("não é validação científica", "não confirma RLL", "não autoriza claim")
BLOCKING_MARKERS = (
    "does not",
    "do not",
    "cannot",
    "not ",
    "no ",
    "sem ",
    "não ",
    "nao ",
    "requer",
    "require",
    "requires",
    "blocked",
)
SCIENTIFIC_TOPIC_TERMS = (
    "rll",
    "lcdm",
    "wcdm",
    "cpl",
    "desi",
    "bao",
    "planck",
    "cmb",
    "h0",
    "s8",
    "growth",
    "likelihood",
    "cosmolog",
    "validation",
    "validação",
)
PROMOTION_PATTERNS = (
    "validates rll",
    "confirms rll",
    "beats lcdm",
    "beats cpl",
    "proves rll",
    "resolve s8",
    "resolves s8",
    "confirma rll",
    "valida rll",
    "vence lcdm",
    "vence cpl",
)


def fail(message: str) -> None:
    raise SystemExit(f"ERROR: {message}")


def load_yaml(path: Path) -> dict[str, Any]:
    if not path.exists():
        fail(f"manifest not found: {path.relative_to(ROOT)}")
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        fail("manifest root must be a mapping")
    return data


def load_signature_ids() -> set[str]:
    if not SIGNATURES.exists():
        return set()
    payload = json.loads(SIGNATURES.read_text(encoding="utf-8"))
    return {str(row.get("dataset_id")) for row in payload.get("rows", []) if isinstance(row, dict)}


def validate_local_file(row: dict[str, Any]) -> None:
    path = ROOT / str(row["local_path"])
    if not path.exists():
        fail(f"{row['dataset_id']}: local_path missing: {row['local_path']}")
    if path.stat().st_size <= 0:
        fail(f"{row['dataset_id']}: local_path is empty: {row['local_path']}")
    checks = set(row.get("required_checks", []))
    if "covariance_file_exists" in checks:
        cov = ROOT / str(row.get("covariance_path", ""))
        if not cov.exists() or cov.stat().st_size <= 0:
            fail(f"{row['dataset_id']}: covariance_path missing/empty: {row.get('covariance_path')}")
    if "json_object" in checks:
        obj = json.loads(path.read_text(encoding="utf-8"))
        if not isinstance(obj, dict):
            fail(f"{row['dataset_id']}: JSON input must be an object")


def validate_claim_blocked(dataset_id: str, entries: Any) -> None:
    if not isinstance(entries, list) or not entries:
        fail(f"{dataset_id}: claim_blocked must be a non-empty list")
    text = "\n".join(str(item) for item in entries).strip()
    lowered = text.lower()
    if not lowered:
        fail(f"{dataset_id}: claim_blocked must not be blank")
    if not any(marker in lowered for marker in BLOCKING_MARKERS):
        fail(f"{dataset_id}: claim_blocked must use explicit blocking language")
    if not any(term in lowered for term in SCIENTIFIC_TOPIC_TERMS):
        fail(f"{dataset_id}: claim_blocked must name the scientific claim/topic being blocked")

    # If high-risk promotion phrases appear, they must appear only in blocked context.
    for pattern in PROMOTION_PATTERNS:
        if pattern in lowered and not any(marker in lowered for marker in BLOCKING_MARKERS):
            fail(f"{dataset_id}: promotion phrase lacks explicit blocking context: {pattern}")


def main() -> int:
    data = load_yaml(MANIFEST)
    missing = REQUIRED_TOP_LEVEL - set(data)
    if missing:
        fail(f"top-level fields missing: {sorted(missing)}")
    if data["schema"] != "rll.real_cosmology_inputs.v1":
        fail(f"unexpected schema: {data['schema']!r}")
    boundary = str(data.get("claim_boundary", ""))
    for term in GLOBAL_BOUNDARY_TERMS:
        if term not in boundary:
            fail(f"claim_boundary must contain: {term}")
    execution = data.get("default_execution") or {}
    if execution.get("offline_first") is not True:
        fail("default_execution must enforce offline_first")
    if execution.get("no_synthetic_promotion") is not True:
        fail("default_execution must enforce no_synthetic_promotion")
    if execution.get("strict_missing_inputs") is not True:
        fail("default_execution must enforce strict_missing_inputs")

    signatures = load_signature_ids()
    seen: set[str] = set()
    inputs = data.get("inputs")
    if not isinstance(inputs, list) or not inputs:
        fail("inputs must be a non-empty list")

    for index, row in enumerate(inputs):
        if not isinstance(row, dict):
            fail(f"input #{index} is not a mapping")
        missing_row = REQUIRED_INPUT_FIELDS - set(row)
        if missing_row:
            fail(f"input #{index} missing fields: {sorted(missing_row)}")
        dataset_id = str(row["dataset_id"])
        if dataset_id in seen:
            fail(f"duplicate dataset_id: {dataset_id}")
        seen.add(dataset_id)
        if row["state"] != "REAL_VALIDATED_LIMITED":
            fail(f"{dataset_id}: state must remain REAL_VALIDATED_LIMITED")
        source = row.get("primary_source") or {}
        if not str(source.get("url", "")).startswith("https://"):
            fail(f"{dataset_id}: primary_source.url must be https")
        if "source_signature_registered" in row.get("required_checks", []):
            signature_ids = row.get("source_signature_ids") or []
            if not signature_ids:
                fail(f"{dataset_id}: source_signature_ids must be non-empty")
            missing_signatures = [str(item) for item in signature_ids if str(item) not in signatures]
            if missing_signatures:
                fail(f"{dataset_id}: missing source_signature_ids in real_source_signatures.json: {missing_signatures}")
        validate_local_file(row)
        validate_claim_blocked(dataset_id, row.get("claim_blocked"))

    print(f"OK: {MANIFEST.relative_to(ROOT)} ({len(inputs)} real cosmology inputs)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
