#!/usr/bin/env python3
"""Validate wandering/silent black-hole source readiness.

This complements the concrete OGLE dark-lens seed validator by scanning the
broader YAML ledger and failing closed when source slots are still TOKEN_VAZIO.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import yaml

SOURCE = Path("data/real/compact_objects/wandering_black_hole_sources.yml")
OUT = Path("data/results/compact_objects/wandering_bh_source_readiness.json")


def _records(doc: dict[str, Any]) -> list[dict[str, Any]]:
    records = doc.get("source_records", [])
    if not isinstance(records, list):
        raise SystemExit("source_records must be a list")
    return [record for record in records if isinstance(record, dict)]


def _has_reference(record: dict[str, Any]) -> bool:
    """Accept legacy and v1 source-reference fields."""
    for key in ("url_or_reference", "source_url", "doi", "arxiv"):
        value = record.get(key)
        if value not in (None, "", "TOKEN_VAZIO"):
            return True
    return False


def _missing_fields(record: dict[str, Any]) -> list[str]:
    keys = ("dataset_name", "provider", "local_path", "checksum_sha256")
    missing = []
    for key in keys:
        value = record.get(key)
        if value in (None, "", "TOKEN_VAZIO"):
            missing.append(key)
    if not _has_reference(record):
        missing.append("source_reference")
    if not record.get("raw_data_available", False):
        missing.append("raw_data_available")
    return missing


def _gate_summary(record: dict[str, Any], missing: list[str]) -> dict[str, bool]:
    """Small operator-facing gate map for failsafe/failover reviews."""
    required = record.get("observables_required_for_rll") or record.get("observables_required") or []
    claim_boundary = record.get("claim_boundary", {})
    raw_required = claim_boundary.get("raw_data_required", []) if isinstance(claim_boundary, dict) else []
    has_required_observables = bool(required or raw_required)
    return {
        "reference_present": _has_reference(record),
        "local_path_declared": record.get("local_path") not in (None, "", "TOKEN_VAZIO"),
        "checksum_present": record.get("checksum_sha256") not in (None, "", "TOKEN_VAZIO"),
        "raw_data_available": bool(record.get("raw_data_available", False)),
        "required_observables_mapped": has_required_observables,
        "claim_allowed": bool(record.get("claim_boundary", {}).get("claim_allowed", False)),
        "failsafe_closed": bool(missing),
    }


def main() -> int:
    doc = yaml.safe_load(SOURCE.read_text(encoding="utf-8"))
    if not isinstance(doc, dict):
        raise SystemExit(f"invalid YAML document: {SOURCE}")

    rows = []
    for record in _records(doc):
        missing = _missing_fields(record)
        rows.append(
            {
                "id": record.get("id", "TOKEN_VAZIO"),
                "candidate_type": record.get("candidate_type", "TOKEN_VAZIO"),
                "missing_fields": missing,
                "gate_summary": _gate_summary(record, missing),
                "status": "blocked_missing_observational_data" if missing else "metadata_ready_claim_blocked",
            }
        )

    payload = {
        "schema_version": "1.0",
        "module": "wandering_black_holes_and_lensing_gaps",
        "source": SOURCE.as_posix(),
        "claim_allowed": False,
        "claim_boundary": "readiness scan only; black-hole claims require lensing/dynamics, baseline alternatives, and checksums",
        "operator_hint": "TOKEN_VAZIO is a truthful block, not an error; replace only with measured archive artifacts.",
        "records": rows,
        "status": "blocked_missing_observational_data" if any(row["missing_fields"] for row in rows) else "metadata_ready_claim_blocked",
        "rollback": "preserve source YAML; remove generated JSON or git revert this validator output",
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(payload, indent=2, ensure_ascii=False, allow_nan=False) + "\n", encoding="utf-8")
    print(f"wrote {OUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
