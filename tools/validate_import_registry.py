#!/usr/bin/env python3
from __future__ import annotations

import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "data/import_registry.csv"
REQUIRED = ["dataset_id", "source_url_or_local_path", "expected_shape", "claim_boundary", "promotion_blocked"]


def shape(obj):
    if isinstance(obj, dict):
        return "object"
    if isinstance(obj, list):
        return "array"
    return type(obj).__name__


def main() -> int:
    with REGISTRY.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    if not rows:
        raise SystemExit("empty registry")
    for col in REQUIRED:
        if col not in rows[0]:
            raise SystemExit(f"missing column: {col}")
    for row in rows:
        for col in REQUIRED:
            if not row[col].strip():
                raise SystemExit(f"empty field: {col}")
        if row["promotion_blocked"].lower() != "true":
            raise SystemExit("promotion must remain blocked")
        source = ROOT / row["source_url_or_local_path"]
        payload = json.loads(source.read_text(encoding="utf-8"))
        if shape(payload) != row["expected_shape"]:
            raise SystemExit("shape mismatch")
    print("OK: import registry")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
