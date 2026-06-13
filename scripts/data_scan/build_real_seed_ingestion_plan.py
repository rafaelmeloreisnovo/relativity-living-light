#!/usr/bin/env python3
"""Build an ingestion plan from RLL real observational seed catalogs.

This script reads seed CSV files and produces:
- data/results/bootstrap/real_seed_ingestion_plan.json
- data/results/bootstrap/real_seed_ingestion_plan.tsv
- docs/science/REAL_SEED_INGESTION_PLAN.md

It does not download raw data and does not validate scientific claims.
"""

from __future__ import annotations

import csv
import json
from dataclasses import dataclass, asdict
from pathlib import Path

SEED_CSVS = [
    Path("data/real/bootstrap/real_observational_seed_v0.csv"),
    Path("data/real/bootstrap/real_observational_seed_v1.csv"),
    Path("data/real/bootstrap/real_observational_seed_v2_orbital_shape.csv"),
    Path("data/real/orbital_dynamics/orbital_shape_angular_momentum_seed_v1.csv"),
]

OUT_JSON = Path("data/results/bootstrap/real_seed_ingestion_plan.json")
OUT_TSV = Path("data/results/bootstrap/real_seed_ingestion_plan.tsv")
OUT_MD = Path("docs/science/REAL_SEED_INGESTION_PLAN.md")

MODULE_ROUTE = {
    "compact_remnant_boundary": {
        "route_id": "compact_remnant_boundary",
        "target_ledger": "data/real/compact_objects/remnant_boundary_sources.yml",
        "validator": "scripts/validation/validate_compact_remnant_boundary.py",
        "expected_output": "data/results/compact_objects/remnant_boundary_validation.json",
        "next_raw_path": "data/raw/compact_objects/",
    },
    "wandering_black_holes": {
        "route_id": "wandering_dark_compact_mass",
        "target_ledger": "data/real/compact_objects/wandering_black_hole_sources.yml",
        "validator": "scripts/validation/validate_dark_lens_candidates.py",
        "expected_output": "data/results/compact_objects/wandering_bh_validation.json",
        "next_raw_path": "data/raw/astrometry/gaia_bh/",
    },
    "residual_gravity_structures": {
        "route_id": "residual_gravity_structures",
        "target_ledger": "data/real/structure/residual_gravity_sources.yml",
        "validator": "scripts/validation/validate_residual_gravity_structures.py",
        "expected_output": "data/results/structure/residual_gravity_validation.json",
        "next_raw_path": "data/raw/structure/stellar_streams/",
    },
    "historical_impulse_slingshot": {
        "route_id": "historical_impulse_slingshot",
        "target_ledger": "data/real/kinematics/hypervelocity_sources.yml",
        "validator": "scripts/validation/validate_historical_impulse_candidates.py",
        "expected_output": "data/results/kinematics/historical_impulse_validation.json",
        "next_raw_path": "data/raw/kinematics/hypervelocity_stars/",
    },
    "high_z_smbh_seeds": {
        "route_id": "high_z_smbh_seeds",
        "target_ledger": "data/real/high_z_smbh/high_z_seed_sources.yml",
        "validator": "scripts/validation/validate_high_z_smbh_seeds.py",
        "expected_output": "data/results/high_z_smbh/seed_validation.json",
        "next_raw_path": "data/raw/high_z_smbh/",
    },
    "orbital_shape_angular_momentum": {
        "route_id": "orbital_shape_angular_momentum",
        "target_ledger": "data/real/orbital_dynamics/angular_momentum_shape_sources.yml",
        "validator": "scripts/validation/validate_orbital_shape_angular_momentum.py",
        "expected_output": "data/results/orbital_dynamics/angular_momentum_shape_validation.json",
        "next_raw_path": "data/raw/orbital_dynamics/",
    },
}


@dataclass
class IngestionItem:
    record_id: str
    module: str
    object_or_event: str
    source_type: str
    reference: str
    reference_url: str
    route_id: str
    target_ledger: str
    validator: str
    expected_output: str
    next_raw_path: str
    status: str
    claim_allowed: bool


def read_rows(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f))
    for row in rows:
        row["_seed_catalog"] = str(path)
    return rows


def first_nonempty(row: dict[str, str], *keys: str, default: str = "TOKEN_VAZIO") -> str:
    for key in keys:
        value = (row.get(key, "") or "").strip()
        if value:
            return value
    return default


def build_item(row: dict[str, str]) -> IngestionItem:
    module = row.get("module", "TOKEN_VAZIO")
    route = MODULE_ROUTE.get(module, {})
    return IngestionItem(
        record_id=first_nonempty(row, "record_id"),
        module=module,
        object_or_event=first_nonempty(row, "object_or_event", "body_system"),
        source_type=first_nonempty(row, "source_type", default="reference_seed"),
        reference=first_nonempty(row, "reference", "source_reference"),
        reference_url=first_nonempty(row, "reference_url", "source_reference_url"),
        route_id=route.get("route_id", "TOKEN_VAZIO_ROUTE"),
        target_ledger=row.get("target_ledger") or route.get("target_ledger", "TOKEN_VAZIO_LEDGER"),
        validator=route.get("validator", "TOKEN_VAZIO_VALIDATOR"),
        expected_output=row.get("expected_result") or route.get("expected_output", "TOKEN_VAZIO_OUTPUT"),
        next_raw_path=route.get("next_raw_path", "TOKEN_VAZIO_RAW_PATH"),
        status="planned_external_seed_ingestion",
        claim_allowed=False,
    )


def write_outputs(items: list[IngestionItem]) -> None:
    OUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    OUT_MD.parent.mkdir(parents=True, exist_ok=True)

    payload = {
        "schema_version": "0.1",
        "status": "real_seed_ingestion_plan_generated",
        "claim_allowed": False,
        "total_items": len(items),
        "routes": sorted({item.route_id for item in items}),
        "items": [asdict(item) for item in items],
        "safe_conclusion": "This is an ingestion plan. Raw data, checksums, baselines, and full metrics are still required before claims.",
    }
    OUT_JSON.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    headers = list(asdict(items[0]).keys()) if items else [
        "record_id", "module", "object_or_event", "source_type", "reference", "reference_url",
        "route_id", "target_ledger", "validator", "expected_output", "next_raw_path", "status", "claim_allowed",
    ]
    lines = ["\t".join(headers)]
    for item in items:
        data = asdict(item)
        lines.append("\t".join(str(data[h]) for h in headers))
    OUT_TSV.write_text("\n".join(lines) + "\n", encoding="utf-8")

    md = [
        "# Real Seed Ingestion Plan",
        "",
        "Status: generated ingestion plan",
        "Claim level: planned ingestion only; no scientific claim",
        "",
        "> Raw data, checksums, baselines, and full metrics are still required before claims.",
        "",
        f"Total planned items: **{len(items)}**",
        "",
        "| Record | Module | Route | Target ledger | Validator | Expected output |",
        "|---|---|---|---|---|---|",
    ]
    for item in items:
        md.append(
            f"| `{item.record_id}` | `{item.module}` | `{item.route_id}` | `{item.target_ledger}` | `{item.validator}` | `{item.expected_output}` |"
        )
    md.extend(
        [
            "",
            "## Safe conclusion",
            "",
            "This file is an operational queue. It maps real seed records into repository paths and future validation steps, but does not claim scientific validation.",
            "",
        ]
    )
    OUT_MD.write_text("\n".join(md), encoding="utf-8")


def main() -> int:
    rows: list[dict[str, str]] = []
    for path in SEED_CSVS:
        rows.extend(read_rows(path))
    items = [build_item(row) for row in rows]
    write_outputs(items)
    print(f"wrote {OUT_JSON}")
    print(f"wrote {OUT_TSV}")
    print(f"wrote {OUT_MD}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
