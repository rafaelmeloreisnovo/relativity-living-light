#!/usr/bin/env python3
"""Emit the RLL multi-repository science trace ledger.

This script is intentionally deterministic and offline. It does not call the
GitHub API. It validates the checked-in JSON ledger and writes normalized JSON
and CSV artifacts for CI/archive use.

Claim rule:
    corpus presence = documented authorial trail
    corpus presence != scientific/medical/material validation
"""

from __future__ import annotations

import csv
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "data" / "results" / "rll_multirepo_science_trace_ledger.json"
OUT_JSON = ROOT / "data" / "results" / "rll_multirepo_science_trace_ledger.normalized.json"
OUT_CSV = ROOT / "data" / "results" / "rll_multirepo_science_trace_ledger.normalized.csv"

REQUIRED_ENTRY_KEYS = [
    "id",
    "repo",
    "path",
    "commit_sha",
    "created_at",
    "terms",
    "domains",
    "exact_or_adjacent",
    "evidence_summary",
    "claim_class",
    "claim_status",
    "next_action",
]

CSV_COLUMNS = [
    "id",
    "repo",
    "path",
    "commit_sha",
    "created_at",
    "terms",
    "domains",
    "exact_or_adjacent",
    "claim_class",
    "claim_status",
    "next_action",
]


def _load_ledger(path: Path) -> dict[str, Any]:
    if not path.exists():
        raise FileNotFoundError(f"Missing ledger: {path}")
    data = json.loads(path.read_text(encoding="utf-8"))
    if data.get("claim_rule") != "corpus_presence_is_authorial_trail_not_scientific_validation":
        raise ValueError("claim_rule must preserve the anti-promotion boundary")
    entries = data.get("entries")
    if not isinstance(entries, list) or not entries:
        raise ValueError("ledger entries must be a non-empty list")
    return data


def _validate_entry(entry: dict[str, Any]) -> None:
    missing = [key for key in REQUIRED_ENTRY_KEYS if key not in entry]
    if missing:
        raise ValueError(f"{entry.get('id', '<unknown>')} missing keys: {missing}")
    if not isinstance(entry["terms"], list):
        raise TypeError(f"{entry['id']} terms must be a list")
    if not isinstance(entry["domains"], list):
        raise TypeError(f"{entry['id']} domains must be a list")
    if "CLAIM_BLOCKED" not in entry["claim_status"] and entry["claim_status"] != "N/A":
        raise ValueError(f"{entry['id']} must keep claim boundary blocked unless explicitly justified")


def _normalize(data: dict[str, Any]) -> dict[str, Any]:
    entries = data["entries"]
    for entry in entries:
        _validate_entry(entry)
    return {
        "schema": data["schema"],
        "claim_rule": data["claim_rule"],
        "entry_count": len(entries),
        "entries": sorted(entries, key=lambda item: (item["created_at"], item["id"])),
    }


def _write_outputs(normalized: dict[str, Any]) -> None:
    OUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    OUT_JSON.write_text(
        json.dumps(normalized, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    with OUT_CSV.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=CSV_COLUMNS)
        writer.writeheader()
        for entry in normalized["entries"]:
            row = {column: entry.get(column, "") for column in CSV_COLUMNS}
            row["terms"] = "|".join(entry["terms"])
            row["domains"] = "|".join(entry["domains"])
            writer.writerow(row)


def main() -> int:
    data = _load_ledger(INPUT)
    normalized = _normalize(data)
    _write_outputs(normalized)
    print(f"[OK] emitted {normalized['entry_count']} multi-repo science trace entries")
    print(f"[OK] json: {OUT_JSON}")
    print(f"[OK] csv:  {OUT_CSV}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
