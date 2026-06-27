#!/usr/bin/env python3
"""Validate real wandering/runaway black-hole source metadata.

This gate is intentionally conservative: the source layer may contain real
observational references and numeric observables, but every RLL claim remains
blocked until raw data, checksums, baselines, uncertainties, and reproducible
artifacts exist.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import sys
from pathlib import Path
from typing import Any

try:
    import yaml
except Exception as exc:  # pragma: no cover - environment guard
    raise SystemExit(f"PyYAML is required for this validator: {exc}") from exc

ROOT = Path(__file__).resolve().parents[2]
DEFAULT_MANIFEST = ROOT / "data" / "real" / "compact_objects" / "wandering_black_hole_sources.yml"
DEFAULT_OUT = ROOT / "data" / "results" / "compact_objects" / "wandering_black_hole_sources_validation.json"

REQUIRED_RECORD_FIELDS = [
    "id",
    "status",
    "source_type",
    "source_title",
    "source_url",
    "access_date_utc",
    "raw_data_available",
    "local_path",
    "checksum_sha256",
    "observables_recorded",
    "claim_boundary",
]


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def load_manifest(path: Path) -> dict[str, Any]:
    if not path.exists():
        raise FileNotFoundError(path)
    payload = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise ValueError("manifest top-level must be a mapping")
    return payload


def validate_csv(csv_path: Path, expected_sha256: str, expected_rows: int) -> tuple[list[str], list[dict[str, str]]]:
    errors: list[str] = []
    if not csv_path.exists():
        return [f"missing csv_table.path: {csv_path.relative_to(ROOT)}"], []

    observed_sha256 = sha256_file(csv_path)
    if observed_sha256 != expected_sha256:
        errors.append(f"CSV sha256 mismatch: expected {expected_sha256}, got {observed_sha256}")

    with csv_path.open("r", encoding="utf-8", newline="") as fh:
        rows = list(csv.DictReader(fh))

    if len(rows) != expected_rows:
        errors.append(f"CSV row count mismatch: expected {expected_rows}, got {len(rows)}")

    for row in rows:
        if str(row.get("claim_allowed", "")).lower() != "false":
            errors.append(f"{row.get('object_id', 'UNKNOWN')}: CSV claim_allowed must be false")
        if not row.get("source_url"):
            errors.append(f"{row.get('object_id', 'UNKNOWN')}: CSV missing source_url")
        numeric_values = [
            row.get("redshift_z"),
            row.get("offset_kpc"),
            row.get("wake_length_kpc"),
            row.get("velocity_km_s"),
            row.get("contrail_length_kpc"),
            row.get("brightness_temperature_lower_limit_K"),
        ]
        if not any(value not in (None, "") for value in numeric_values):
            errors.append(f"{row.get('object_id', 'UNKNOWN')}: CSV has no numeric observable")

    return errors, rows


def validate_manifest(payload: dict[str, Any]) -> dict[str, Any]:
    errors: list[str] = []
    warnings: list[str] = []

    if payload.get("claim_allowed") is not False:
        errors.append("top-level claim_allowed must be false")

    policy = payload.get("claim_policy") or {}
    if not isinstance(policy, dict):
        errors.append("claim_policy must be a mapping")
    elif policy.get("no_superiority") is not True:
        errors.append("claim_policy.no_superiority must be true")

    csv_block = payload.get("csv_table") or {}
    if not isinstance(csv_block, dict):
        errors.append("csv_table must be a mapping")
        csv_rows: list[dict[str, str]] = []
    else:
        csv_path = ROOT / str(csv_block.get("path", ""))
        csv_errors, csv_rows = validate_csv(
            csv_path,
            str(csv_block.get("sha256", "")),
            int(csv_block.get("rows", -1)),
        )
        errors.extend(csv_errors)
        if csv_block.get("claim_allowed") is not False:
            errors.append("csv_table.claim_allowed must be false")

    records = payload.get("source_records") or []
    if not isinstance(records, list) or not records:
        errors.append("source_records must be a non-empty list")
        records = []

    record_ids = set()
    for record in records:
        if not isinstance(record, dict):
            errors.append("each source_records item must be a mapping")
            continue
        record_id = str(record.get("id", "UNKNOWN"))
        record_ids.add(record_id)
        for field in REQUIRED_RECORD_FIELDS:
            if field not in record:
                errors.append(f"{record_id}: missing field {field}")
        if not str(record.get("source_url", "")).startswith("https://"):
            errors.append(f"{record_id}: source_url must be https")
        if record.get("source_type") not in {"arxiv_preprint", "journal_article", "catalog", "archive"}:
            errors.append(f"{record_id}: unsupported source_type {record.get('source_type')}")
        if record.get("raw_data_available") is True and record.get("checksum_sha256") == "TOKEN_VAZIO":
            errors.append(f"{record_id}: raw_data_available=true requires checksum_sha256")
        boundary = record.get("claim_boundary") or {}
        if not isinstance(boundary, dict) or boundary.get("claim_allowed") is not False:
            errors.append(f"{record_id}: claim_boundary.claim_allowed must be false")
        observables = record.get("observables_recorded") or {}
        if not isinstance(observables, dict) or not observables:
            errors.append(f"{record_id}: observables_recorded must contain at least one value")
        if record.get("local_path") == "TOKEN_VAZIO":
            warnings.append(f"{record_id}: external-only boundary; local raw file not materialized")

    csv_ids = {row.get("object_id") for row in csv_rows}
    if record_ids and csv_ids and record_ids != csv_ids:
        errors.append(f"CSV object_id set does not match YAML id set: csv={sorted(csv_ids)} yaml={sorted(record_ids)}")

    return {
        "status": "PASS" if not errors else "FAIL",
        "claim_allowed": False,
        "records": len(records),
        "csv_rows": len(csv_rows),
        "errors": errors,
        "warnings": warnings,
        "safe_conclusion": "real source metadata present; RLL claims remain blocked pending raw data, checksums, baselines, uncertainties, and artifacts",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate wandering black-hole real source metadata.")
    parser.add_argument("--manifest", default=str(DEFAULT_MANIFEST))
    parser.add_argument("--out", default=str(DEFAULT_OUT))
    parser.add_argument("--no-write", action="store_true")
    args = parser.parse_args()

    manifest = load_manifest(Path(args.manifest))
    result = validate_manifest(manifest)

    print(json.dumps(result, indent=2, ensure_ascii=False))

    if not args.no_write:
        out = Path(args.out)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    return 0 if result["status"] == "PASS" else 1


if __name__ == "__main__":
    sys.exit(main())
