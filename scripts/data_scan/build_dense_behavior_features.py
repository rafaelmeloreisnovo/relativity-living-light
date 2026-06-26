#!/usr/bin/env python3
"""Build dense behavior features from seed-stage RLL artifacts.

This script converts existing seed artifacts into a denser feature matrix. It is
not a scientific prediction engine; it prepares mathematical routes for later
raw-data validation.
"""

from __future__ import annotations

import csv
import json
from pathlib import Path
from typing import Any

INGESTION_PLAN = Path("data/results/bootstrap/real_seed_ingestion_plan.json")
ORBITAL_RESULT = Path("data/results/orbital_dynamics/angular_momentum_shape_validation.json")
TOKEN_LEDGER = Path("data/results/bootstrap/token_vazio_priority_ledger.json")
NEGATIVE_LEDGER = Path("data/results/negative_results_ledger.json")

OUT_JSON = Path("data/results/bootstrap/dense_behavior_features.json")
OUT_TSV = Path("data/results/bootstrap/dense_behavior_features.tsv")
OUT_MD = Path("docs/science/DENSE_BEHAVIOR_FEATURES_REPORT.md")


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def route_priority_map(token_ledger: dict[str, Any]) -> dict[str, str]:
    priority: dict[str, str] = {}
    for item in token_ledger.get("items", []):
        route = item.get("route", "all")
        current = priority.get(route)
        new = item.get("priority", "P3")
        if current is None or new < current:
            priority[route] = new
    return priority


def blocked_routes(negative_ledger: dict[str, Any]) -> set[str]:
    return {item.get("route", "") for item in negative_ledger.get("items", [])}


def orbital_feature_map(orbital_result: dict[str, Any]) -> dict[str, dict[str, Any]]:
    mapping: dict[str, dict[str, Any]] = {}
    for item in orbital_result.get("items", []):
        calc = item.get("calculations_v1", {})
        inputs = item.get("inputs", {})
        mass = inputs.get("body_mass_kg")
        h = calc.get("specific_orbital_angular_momentum_km2_s")
        spin = calc.get("spin_angular_momentum_proxy_kg_m2_s")
        total_orbital_angular_momentum = None
        spin_orbit_ratio = None
        if mass is not None and h is not None:
            total_orbital_angular_momentum = mass * h * 1_000_000.0
        if total_orbital_angular_momentum and spin is not None:
            spin_orbit_ratio = spin / total_orbital_angular_momentum
        mapping[item.get("record_id", "")] = {
            "body_system": item.get("body_system"),
            "specific_orbital_angular_momentum_km2_s": h,
            "mean_orbital_speed_proxy_km_s": calc.get("mean_orbital_speed_proxy_km_s"),
            "spin_angular_momentum_proxy_kg_m2_s": spin,
            "total_orbital_angular_momentum_proxy_kg_m2_s": total_orbital_angular_momentum,
            "spin_orbit_ratio_proxy": spin_orbit_ratio,
            "flattening": calc.get("computed_flattening_from_radii"),
            "j2": inputs.get("j2"),
        }
    return mapping


def readiness_score(route_id: str, record_id: str, has_metric: bool) -> float:
    score = 0.0
    score += 0.20  # seed exists
    score += 0.15  # routed into orchestration
    if has_metric:
        score += 0.20
    if route_id == "orbital_shape_angular_momentum" and record_id.startswith("REAL_ORBIT_"):
        score += 0.10
    # raw data/checksum/baseline/error model are deliberately absent at this layer
    return round(score, 3)


def behavior_class(route_id: str, record_id: str, has_metric: bool, is_blocked: bool, priority: str | None) -> str:
    if route_id == "orbital_shape_angular_momentum" and record_id.startswith("REAL_ORBIT_"):
        return "reference_motion_profile"
    if priority in {"P0", "P1"}:
        return "high_value_next_measure"
    if has_metric:
        return "seed_metric_ready_claim_blocked"
    if is_blocked:
        return "negative_result_guarded"
    return "seed_only_waiting_raw_data"


def main() -> int:
    plan = load_json(INGESTION_PLAN)
    orbital = load_json(ORBITAL_RESULT)
    token = load_json(TOKEN_LEDGER)
    negative = load_json(NEGATIVE_LEDGER)

    priority_by_route = route_priority_map(token)
    blocked = blocked_routes(negative)
    orbital_features = orbital_feature_map(orbital)

    dense_items: list[dict[str, Any]] = []
    for item in plan.get("items", []):
        record_id = item.get("record_id")
        route_id = item.get("route_id")
        has_metric = record_id in orbital_features or "validation" in item.get("expected_output", "")
        priority = priority_by_route.get(route_id) or priority_by_route.get("all")
        is_blocked = route_id in blocked or item.get("module") in blocked
        dense = {
            "record_id": record_id,
            "module": item.get("module"),
            "route_id": route_id,
            "claim_allowed": False,
            "raw_data_local": False,
            "checksum_present": False,
            "baseline_present": False,
            "error_model_present": False,
            "seed_present": True,
            "metric_seed_present": bool(has_metric),
            "priority": priority or "P3",
            "negative_result_guarded": bool(is_blocked),
            "readiness_score_seed_stage": readiness_score(route_id, record_id, bool(has_metric)),
            "behavior_class": behavior_class(route_id, record_id, bool(has_metric), bool(is_blocked), priority),
            "next_math_target": next_math_target(route_id),
        }
        if record_id in orbital_features:
            dense["orbital_features"] = orbital_features[record_id]
        dense_items.append(dense)

    payload = {
        "schema_version": "0.1",
        "status": "dense_behavior_features_generated",
        "claim_allowed": False,
        "source_artifacts": [
            str(INGESTION_PLAN),
            str(ORBITAL_RESULT),
            str(TOKEN_LEDGER),
            str(NEGATIVE_LEDGER),
        ],
        "total_items": len(dense_items),
        "feature_policy": "seed-derived features only; not final scientific prediction",
        "items": dense_items,
        "safe_conclusion": "Dense behavior features expose mathematical routes and behavior classes, but raw data, checksum, uncertainty, and baselines remain required before prediction claims.",
    }

    OUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    OUT_MD.parent.mkdir(parents=True, exist_ok=True)
    OUT_JSON.write_text(json.dumps(payload, indent=2, ensure_ascii=False, allow_nan=False) + "\n", encoding="utf-8")

    headers = [
        "record_id", "module", "route_id", "behavior_class", "priority", "readiness_score_seed_stage",
        "metric_seed_present", "raw_data_local", "baseline_present", "error_model_present", "claim_allowed", "next_math_target",
    ]
    with OUT_TSV.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=headers, delimiter="\t", extrasaction="ignore")
        writer.writeheader()
        for row in dense_items:
            writer.writerow(row)

    write_report(dense_items)
    print(f"wrote {OUT_JSON}")
    print(f"wrote {OUT_TSV}")
    print(f"wrote {OUT_MD}")
    return 0


def next_math_target(route_id: str) -> str:
    return {
        "compact_remnant_boundary": "mass_gap_overlap_probability",
        "wandering_dark_compact_mass": "astrometric_dark_mass_consistency",
        "residual_gravity_structures": "stream_membership_probability",
        "historical_impulse_slingshot": "traceback_probability",
        "high_z_smbh_seeds": "Eddington_growth_feasibility_grid",
        "orbital_shape_angular_momentum": "state_vector_vs_reference_h_residual",
    }.get(route_id, "TOKEN_VAZIO_NEXT_MATH_TARGET")


def write_report(items: list[dict[str, Any]]) -> None:
    counts: dict[str, int] = {}
    for item in items:
        counts[item["behavior_class"]] = counts.get(item["behavior_class"], 0) + 1
    lines = [
        "# Dense Behavior Features Report",
        "",
        "Status: seed-derived behavior feature layer",
        "Claim level: `claim_allowed=false`",
        "",
        "> This report densifies seen seed data into mathematical feature routes. It is not a final prediction claim.",
        "",
        "## Behavior classes",
        "",
        "| Class | Count |",
        "|---|---:|",
    ]
    for key in sorted(counts):
        lines.append(f"| `{key}` | {counts[key]} |")
    lines.extend([
        "",
        "## Highest readiness seed-stage items",
        "",
        "| Record | Route | Class | Score | Next math target |",
        "|---|---|---|---:|---|",
    ])
    for item in sorted(items, key=lambda x: x["readiness_score_seed_stage"], reverse=True)[:10]:
        lines.append(
            f"| `{item['record_id']}` | `{item['route_id']}` | `{item['behavior_class']}` | {item['readiness_score_seed_stage']} | `{item['next_math_target']}` |"
        )
    lines.extend([
        "",
        "## Safe conclusion",
        "",
        "Dense features expose behavior classes and next mathematical targets. Scientific prediction still requires raw data, checksum, uncertainty, and baselines.",
        "",
    ])
    OUT_MD.write_text("\n".join(lines), encoding="utf-8")


if __name__ == "__main__":
    raise SystemExit(main())
