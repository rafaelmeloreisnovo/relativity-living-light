#!/usr/bin/env python3
"""Orbital shape angular momentum seed validator.

This v1 validator reads reference seed parameters and computes first-pass
kinematic/shape metrics. It does not use raw ephemeris vectors and does not
allow scientific claims.
"""

from __future__ import annotations

import csv
import json
import math
from pathlib import Path
from typing import Any

IN_CSV = Path("data/real/orbital_dynamics/orbital_shape_angular_momentum_seed_v1.csv")
OUT = Path("data/results/orbital_dynamics/angular_momentum_shape_validation.json")
REPORT = Path("docs/science/ORBITAL_SHAPE_ANGULAR_MOMENTUM_V1_REPORT.md")


def f(row: dict[str, str], key: str) -> float | None:
    value = (row.get(key, "") or "").strip()
    if value == "":
        return None
    return float(value)


def compute(row: dict[str, str]) -> dict[str, Any]:
    mu = f(row, "mu_central_km3_s2")
    a = f(row, "semi_major_axis_km")
    e = f(row, "eccentricity")
    mass = f(row, "body_mass_kg")
    radius_km = f(row, "radius_reference_km")
    eq_radius = f(row, "equatorial_radius_km")
    polar_radius = f(row, "polar_radius_km")
    rotation_period = f(row, "rotation_period_s")
    cbar = f(row, "normalized_moment_inertia")

    h = math.sqrt(mu * a * (1.0 - e * e)) if None not in (mu, a, e) else None
    mean_orbital_speed = h / a if None not in (h, a) else None
    omega = (2.0 * math.pi / rotation_period) if rotation_period else None
    spin_proxy = (
        cbar * mass * (radius_km * 1000.0) ** 2 * omega
        if None not in (cbar, mass, radius_km, omega)
        else None
    )
    computed_flattening = (
        (eq_radius - polar_radius) / eq_radius
        if None not in (eq_radius, polar_radius) and eq_radius != 0
        else None
    )

    return {
        "record_id": row.get("record_id"),
        "body_system": row.get("body_system"),
        "central_body": row.get("central_body"),
        "orbit_frame": row.get("orbit_frame"),
        "inputs": {
            "mu_central_km3_s2": mu,
            "semi_major_axis_km": a,
            "eccentricity": e,
            "body_mass_kg": mass,
            "radius_reference_km": radius_km,
            "rotation_period_s": rotation_period,
            "normalized_moment_inertia": cbar,
            "j2": f(row, "j2"),
            "flattening_seed": f(row, "flattening"),
        },
        "calculations_v1": {
            "specific_orbital_angular_momentum_km2_s": h,
            "mean_orbital_speed_proxy_km_s": mean_orbital_speed,
            "spin_angular_momentum_proxy_kg_m2_s": spin_proxy,
            "rotation_rate_rad_s": omega,
            "computed_flattening_from_radii": computed_flattening,
        },
        "source_reference": row.get("source_reference"),
        "source_reference_url": row.get("source_reference_url"),
        "status": "seed_metric_ready_claim_blocked",
        "claim_allowed": False,
    }


def load_rows() -> list[dict[str, str]]:
    if not IN_CSV.exists():
        raise FileNotFoundError(f"missing seed CSV: {IN_CSV}")
    with IN_CSV.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def write_report(items: list[dict[str, Any]]) -> None:
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# Orbital Shape Angular Momentum v1 Report",
        "",
        "Status: seed-level metric report",
        "Claim level: `claim_allowed=false`",
        "",
        "> These calculations use reference seed parameters only. Raw ephemeris vectors, gravity/shape models, uncertainty, and baselines remain required.",
        "",
        "| Record | Body | h specific km²/s | speed proxy km/s | spin proxy kg m²/s | Claim |",
        "|---|---|---:|---:|---:|---:|",
    ]
    for item in items:
        calc = item["calculations_v1"]
        lines.append(
            "| `{}` | {} | {:.6g} | {:.6g} | {:.6g} | `{}` |".format(
                item["record_id"],
                item["body_system"],
                calc["specific_orbital_angular_momentum_km2_s"] or 0.0,
                calc["mean_orbital_speed_proxy_km_s"] or 0.0,
                calc["spin_angular_momentum_proxy_kg_m2_s"] or 0.0,
                str(item["claim_allowed"]).lower(),
            )
        )
    lines.extend([
        "",
        "## Safe conclusion",
        "",
        "The orbital-shape-angular-momentum route now has first-pass computable seed metrics. It still does not validate a new gravity, deformation, or RLL claim.",
        "",
    ])
    REPORT.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    rows = load_rows()
    items = [compute(row) for row in rows]
    OUT.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "schema_version": "0.1",
        "module": "orbital_shape_angular_momentum",
        "input_file": str(IN_CSV),
        "data_status": "external_only_seed_reference_metrics",
        "claim_allowed": False,
        "claim_boundary": "seed-level calculations only; raw ephemerides, vectors, gravity/shape models, uncertainty, and baselines are required before scientific claims",
        "formulas": {
            "specific_orbital_angular_momentum": "h = sqrt(mu_central * a * (1 - e^2))",
            "mean_orbital_speed_proxy": "v ~= h / a",
            "spin_angular_momentum_proxy": "S ~= Cbar * M * R^2 * omega",
            "rotation_rate": "omega = 2*pi / rotation_period",
            "flattening_from_radii": "f = (Req - Rpole) / Req",
        },
        "items": items,
        "required_next_data": [
            "raw ephemeris state vectors from JPL Horizons or SPICE",
            "gravity harmonics with source/version",
            "shape or reference ellipsoid model with source/version",
            "rotation and pole orientation model",
            "uncertainty or covariance model",
            "Kepler/Newton/N-body/J2 baseline comparison",
        ],
        "safe_conclusion": "First-pass orbital and spin seed metrics were produced; no final orbital-shape deformation claim is allowed.",
        "status": "seed_metric_ready_claim_blocked",
    }
    OUT.write_text(json.dumps(payload, indent=2, ensure_ascii=False, allow_nan=False) + "\n", encoding="utf-8")
    write_report(items)
    print(f"wrote {OUT}")
    print(f"wrote {REPORT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
