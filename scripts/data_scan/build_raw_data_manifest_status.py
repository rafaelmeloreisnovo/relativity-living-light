#!/usr/bin/env python3
"""Build raw data manifest status from RAW_DATA_MANIFEST.yml.

This script is intentionally lightweight and stdlib-only. It extracts custody
records from the manifest, checks whether local raw files exist, computes sha256
for present files, and writes JSON/TSV status artifacts.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

MANIFEST = Path("data/raw/RAW_DATA_MANIFEST.yml")
OUT_JSON = Path("data/results/bootstrap/raw_data_manifest_status.json")
OUT_TSV = Path("data/results/bootstrap/raw_data_manifest_status.tsv")
REPORT = Path("docs/science/RAW_DATA_MANIFEST_STATUS.md")

KEYS = [
    "raw_id",
    "route_id",
    "record_id",
    "source_url",
    "access_date_utc",
    "license_or_terms",
    "source_version",
    "local_path",
    "sha256",
    "bytes",
    "raw_data_local",
    "status",
    "claim_allowed",
    "next_metric",
]


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def parse_manifest_records(text: str) -> list[dict[str, str]]:
    records: list[dict[str, str]] = []
    current: dict[str, str] | None = None
    for raw_line in text.splitlines():
        line = raw_line.strip()
        if line.startswith("- raw_id:"):
            if current:
                records.append(current)
            current = {"raw_id": line.split(":", 1)[1].strip()}
            continue
        if current is not None and ":" in line:
            key, value = line.split(":", 1)
            key = key.strip()
            value = value.strip()
            if key in KEYS:
                current[key] = value
    if current:
        records.append(current)
    return records


def normalize_bool(value: str | bool | None) -> bool:
    if isinstance(value, bool):
        return value
    return str(value).strip().lower() == "true"


def build_status() -> dict[str, object]:
    if not MANIFEST.exists():
        raise FileNotFoundError(MANIFEST)
    text = MANIFEST.read_text(encoding="utf-8")
    records = parse_manifest_records(text)
    items = []
    present = 0
    for rec in records:
        local_path = Path(rec.get("local_path", "TOKEN_VAZIO"))
        exists = local_path.exists() and local_path.is_file()
        actual_sha = sha256_file(local_path) if exists else "TOKEN_VAZIO"
        actual_bytes = local_path.stat().st_size if exists else None
        declared_sha = rec.get("sha256", "TOKEN_VAZIO")
        sha_matches = exists and declared_sha not in {"TOKEN_VAZIO", ""} and declared_sha == actual_sha
        if exists:
            present += 1
        items.append({
            "raw_id": rec.get("raw_id", "TOKEN_VAZIO"),
            "route_id": rec.get("route_id", "TOKEN_VAZIO"),
            "record_id": rec.get("record_id", "TOKEN_VAZIO"),
            "local_path": rec.get("local_path", "TOKEN_VAZIO"),
            "source_url": rec.get("source_url", "TOKEN_VAZIO"),
            "access_date_utc": rec.get("access_date_utc", "TOKEN_VAZIO"),
            "license_or_terms": rec.get("license_or_terms", "TOKEN_VAZIO"),
            "source_version": rec.get("source_version", "TOKEN_VAZIO"),
            "declared_sha256": declared_sha,
            "actual_sha256": actual_sha,
            "sha256_matches_manifest": sha_matches,
            "bytes": actual_bytes,
            "raw_file_present": exists,
            "raw_data_local": exists,
            "claim_allowed": False,
            "next_metric": rec.get("next_metric", "TOKEN_VAZIO"),
            "status": "raw_file_present_hash_ready" if exists else "pending_raw_ingestion",
        })
    return {
        "schema_version": "0.1",
        "status": "raw_data_manifest_status_generated",
        "claim_allowed": False,
        "manifest": str(MANIFEST),
        "total_records": len(items),
        "raw_files_present": present,
        "raw_files_missing": len(items) - present,
        "items": items,
        "safe_conclusion": "Raw data custody is scaffolded. Missing files remain TOKEN_VAZIO and cannot support claims.",
    }


def write_outputs(payload: dict[str, object]) -> None:
    OUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    OUT_JSON.write_text(json.dumps(payload, indent=2, ensure_ascii=False, allow_nan=False) + "\n", encoding="utf-8")
    headers = [
        "raw_id", "route_id", "record_id", "local_path", "raw_file_present", "raw_data_local",
        "declared_sha256", "actual_sha256", "sha256_matches_manifest", "bytes", "claim_allowed", "status", "next_metric",
    ]
    lines = ["\t".join(headers)]
    for item in payload["items"]:  # type: ignore[index]
        lines.append("\t".join(str(item.get(h, "")) for h in headers))
    OUT_TSV.write_text("\n".join(lines) + "\n", encoding="utf-8")

    lines_md = [
        "# Raw Data Manifest Status",
        "",
        "Status: raw-data custody status",
        "Claim level: `claim_allowed=false`",
        "",
        f"Total records: **{payload['total_records']}**",
        f"Raw files present: **{payload['raw_files_present']}**",
        f"Raw files missing: **{payload['raw_files_missing']}**",
        "",
        "| Raw ID | Route | File present | SHA matches | Next metric |",
        "|---|---|---:|---:|---|",
    ]
    for item in payload["items"]:  # type: ignore[index]
        lines_md.append(
            f"| `{item['raw_id']}` | `{item['route_id']}` | `{item['raw_file_present']}` | `{item['sha256_matches_manifest']}` | `{item['next_metric']}` |"
        )
    lines_md.extend([
        "",
        "## Safe conclusion",
        "",
        "Raw data custody is scaffolded. Missing files remain TOKEN_VAZIO and cannot support claims.",
        "",
    ])
    REPORT.write_text("\n".join(lines_md), encoding="utf-8")


def main() -> int:
    payload = build_status()
    write_outputs(payload)
    print(f"wrote {OUT_JSON}")
    print(f"wrote {OUT_TSV}")
    print(f"wrote {REPORT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
