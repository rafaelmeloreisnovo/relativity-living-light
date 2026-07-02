#!/usr/bin/env python3
"""Normalize model-comparison CSV columns for downstream audit bridges.

This tool is intentionally structural: it preserves existing columns and values,
adds compatibility aliases when they are missing, and does not interpret model
performance or promote scientific claims.
"""

from __future__ import annotations

import argparse
import csv
from pathlib import Path
from typing import Iterable

ALIASES: tuple[tuple[str, str], ...] = (
    ("AIC", "aic"),
    ("BIC", "bic"),
    ("chi2", "chi2_total"),
)

CLAIM_BOUNDARY = (
    "Column normalization is structural compatibility only; it does not validate "
    "RLL, select a winning model, or promote any scientific claim."
)


def _case_insensitive_lookup(row: dict[str, str], key: str) -> str | None:
    if key in row and row[key] != "":
        return row[key]
    lowered = {name.lower(): name for name in row}
    source = lowered.get(key.lower())
    if source is None:
        return None
    value = row.get(source)
    return value if value != "" else None


def _append_missing(fieldnames: list[str], required: Iterable[str]) -> list[str]:
    out = list(fieldnames)
    existing = {name.lower() for name in out}
    for name in required:
        if name.lower() not in existing:
            out.append(name)
            existing.add(name.lower())
    return out


def normalize_model_comparison_csv(path: Path) -> dict[str, object]:
    if not path.exists():
        raise FileNotFoundError(path)

    with path.open("r", encoding="utf-8", newline="") as fh:
        reader = csv.DictReader(fh)
        if reader.fieldnames is None:
            raise ValueError(f"CSV has no header: {path}")
        fieldnames = list(reader.fieldnames)
        rows = [dict(row) for row in reader]

    required_aliases = [alias for _, alias in ALIASES]
    output_fields = _append_missing(fieldnames, required_aliases)
    added = [name for name in output_fields if name not in fieldnames]

    for row in rows:
        for source, alias in ALIASES:
            if row.get(alias) not in (None, ""):
                continue
            value = _case_insensitive_lookup(row, source)
            if value is not None:
                row[alias] = value
        for field in output_fields:
            row.setdefault(field, "")

    with path.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=output_fields)
        writer.writeheader()
        writer.writerows(rows)

    return {
        "path": str(path),
        "rows": len(rows),
        "added_columns": added,
        "claim_boundary": CLAIM_BOUNDARY,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("csv_path", type=Path)
    args = parser.parse_args()
    summary = normalize_model_comparison_csv(args.csv_path)
    print(summary)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
