#!/usr/bin/env python3
"""Validate minimal real dataset variance registries.

This check is structural only. It does not validate any scientific model.
"""
from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VARIANCE = ROOT / "data/real/cosmology/variance_policy_registry_minimal.csv"
ROUTES = ROOT / "data/real/cosmology/dataset_routes_minimal.csv"

REQUIRED_VARIANCE_COLUMNS = {
    "dataset_id",
    "axis",
    "uncertainty_policy",
    "covariance_status",
    "claim_boundary",
}
REQUIRED_ROUTE_COLUMNS = {"id", "axis", "path", "policy"}


def read_csv(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        raise SystemExit(f"missing registry: {path}")
    with path.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    if not rows:
        raise SystemExit(f"empty registry: {path}")
    return rows


def require_columns(rows: list[dict[str, str]], required: set[str], path: Path) -> None:
    missing = required - set(rows[0])
    if missing:
        raise SystemExit(f"{path} missing columns: {sorted(missing)}")


def require_nonempty(rows: list[dict[str, str]], fields: set[str], path: Path) -> None:
    for index, row in enumerate(rows, start=2):
        for field in fields:
            if not (row.get(field) or "").strip():
                raise SystemExit(f"{path}:{index} empty field: {field}")


def main() -> int:
    variance_rows = read_csv(VARIANCE)
    route_rows = read_csv(ROUTES)
    require_columns(variance_rows, REQUIRED_VARIANCE_COLUMNS, VARIANCE)
    require_columns(route_rows, REQUIRED_ROUTE_COLUMNS, ROUTES)
    require_nonempty(variance_rows, REQUIRED_VARIANCE_COLUMNS, VARIANCE)
    require_nonempty(route_rows, REQUIRED_ROUTE_COLUMNS, ROUTES)

    route_policies = {row["policy"] for row in route_rows}
    variance_policies = {row["uncertainty_policy"] for row in variance_rows}
    aliases = {"compressed": "diagonal_sigma", "covariance_summary": "covariance_summary", "diagonal": "diagonal_sigma"}
    unmapped = [policy for policy in route_policies if aliases.get(policy, policy) not in variance_policies]
    if unmapped:
        raise SystemExit(f"route policies not represented in variance registry: {sorted(unmapped)}")

    print("OK: real dataset variance registries are structurally coherent")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
