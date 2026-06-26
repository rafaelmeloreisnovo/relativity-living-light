#!/usr/bin/env python3
"""Validate residual-gravity structure source readiness.

This validator is intentionally fail-closed: the current YAML ledger contains
TOKEN_VAZIO source slots, so the script records readiness gaps and keeps
claim_allowed=false instead of inventing measurements.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import yaml

SOURCE = Path("data/real/structure/residual_gravity_sources.yml")
OUT = Path("data/results/structure/residual_gravity_validation.json")


def _records(doc: dict[str, Any]) -> list[dict[str, Any]]:
    records = doc.get("source_records", [])
    if not isinstance(records, list):
        raise SystemExit("source_records must be a list")
    return [record for record in records if isinstance(record, dict)]


def _missing_fields(record: dict[str, Any]) -> list[str]:
    keys = ("dataset_name", "provider", "url_or_reference", "local_path", "checksum_sha256")
    missing = []
    for key in keys:
        value = record.get(key)
        if value in (None, "", "TOKEN_VAZIO"):
            missing.append(key)
    if not record.get("raw_data_available", False):
        missing.append("raw_data_available")
    return missing


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
                "status": "blocked_missing_observational_data" if missing else "metadata_ready_claim_blocked",
            }
        )

    payload = {
        "schema_version": "0.1",
        "module": "gravitational_residual_memory_and_compact_gaps",
        "source": SOURCE.as_posix(),
        "claim_allowed": False,
        "claim_boundary": "readiness scan only; residual-gravity claims require mass/kinematic/lensing evidence and baselines",
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
