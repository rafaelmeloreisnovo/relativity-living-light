#!/usr/bin/env python3
"""Shared helpers for RLL real observational seed validation v0.

These helpers intentionally use only the Python standard library.
The seed v0 CSV is an external-only seed catalog, not a raw-catalog ingestion.
"""

from __future__ import annotations

import csv
import json
import re
from pathlib import Path
from typing import Any

DEFAULT_SEED_CSV = Path("data/real/bootstrap/real_observational_seed_v0.csv")


def load_seed_rows(path: Path = DEFAULT_SEED_CSV) -> list[dict[str, str]]:
    if not path.exists():
        raise FileNotFoundError(f"seed CSV not found: {path}")
    with path.open("r", encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def find_seed(record_id: str, rows: list[dict[str, str]] | None = None) -> dict[str, str]:
    rows = rows if rows is not None else load_seed_rows()
    for row in rows:
        if row.get("record_id") == record_id:
            return row
    raise KeyError(f"record_id not found in seed CSV: {record_id}")


def extract_value(row: dict[str, str], key: str) -> str | None:
    """Extract key values from compact seed CSV fields.

    Accepts both strict forms such as `mass=1.0` and approximate forms
    such as `mass≈1.0` or `mass~1.0`. This avoids losing real seed
    values that are explicitly approximate.
    """
    separators = ("=", "≈", "~", ":")
    for field in ("key_observable_1", "key_observable_2", "key_observable_3"):
        value = (row.get(field, "") or "").strip()
        for sep in separators:
            prefix = f"{key}{sep}"
            if value.startswith(prefix):
                return value[len(prefix):].strip()
    return None


def parse_float(text: str | None) -> float | None:
    if text is None:
        return None
    cleaned = text.replace("≈", "").replace("~", "").replace(",", "").strip()
    match = re.search(r"[-+]?\d+(?:\.\d+)?(?:[eE][-+]?\d+)?", cleaned)
    return float(match.group(0)) if match else None


def parse_range(text: str | None) -> list[float] | None:
    if text is None:
        return None
    cleaned = text.replace("≈", "").replace("~", "").replace(",", "")
    nums = re.findall(r"[-+]?\d+(?:\.\d+)?", cleaned)
    if len(nums) >= 2:
        return [float(nums[0]), float(nums[1])]
    return None


def parse_pm(text: str | None) -> dict[str, float | None]:
    if text is None:
        return {"value": None, "minus": None, "plus": None}
    cleaned = text.replace("±", "+/-")
    nums = re.findall(r"[-+]?\d+(?:\.\d+)?", cleaned)
    if len(nums) >= 2:
        return {"value": float(nums[0]), "minus": float(nums[1]), "plus": float(nums[1])}
    if len(nums) == 1:
        return {"value": float(nums[0]), "minus": None, "plus": None}
    return {"value": None, "minus": None, "plus": None}


def parse_asymmetric_radius(text: str | None) -> dict[str, float | None]:
    # Example: 13.7+2.6-1.5
    if text is None:
        return {"value": None, "minus": None, "plus": None}
    nums = re.findall(r"\d+(?:\.\d+)?", text)
    if len(nums) >= 3:
        return {"value": float(nums[0]), "plus": float(nums[1]), "minus": float(nums[2])}
    return parse_pm(text)


def ensure_parent(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)


def write_json(path: Path, payload: dict[str, Any]) -> None:
    ensure_parent(path)
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False, allow_nan=False) + "\n", encoding="utf-8")


def base_payload(module: str, records: list[str]) -> dict[str, Any]:
    return {
        "schema_version": "0.1",
        "module": module,
        "input_seed_records": records,
        "data_status": "external_only_seed",
        "claim_allowed": False,
        "claim_boundary": "seed-derived calculation only; not a final validation claim",
    }
