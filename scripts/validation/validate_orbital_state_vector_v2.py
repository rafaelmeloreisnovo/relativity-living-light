#!/usr/bin/env python3
"""Validate orbital state-vector v2 against seed formula.

Computes h_vector = |r x v| from a Horizons Cartesian vector table and compares
it with h_seed = sqrt(mu*a*(1-e^2)) from the seed catalog.
"""

from __future__ import annotations

import csv
import json
import math
from pathlib import Path

SEED_CSV = Path("data/real/orbital_dynamics/orbital_shape_angular_momentum_seed_v1.csv")
RAW_VECTOR_CSV = Path("data/raw/orbital_dynamics/ephemerides/jpl_horizons_mars_vectors_2006_sample.csv")
OUT_JSON = Path("data/results/orbital_dynamics/orbital_state_vector_v2_validation.json")
OUT_MD = Path("docs/science/ORBITAL_STATE_VECTOR_V2_REPORT.md")


def load_mars_seed() -> dict[str, str]:
    with SEED_CSV.open("r", encoding="utf-8", newline="") as handle:
        for row in csv.DictReader(handle):
            if row["record_id"] == "REAL_ORBIT_MARS_HELIOCENTRIC_SHAPE_AM_V1":
                return row
    raise RuntimeError("Mars seed row not found")


def load_vector_rows() -> list[dict[str, str]]:
    with RAW_VECTOR_CSV.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def f(row: dict[str, str], key: str) -> float:
    return float(row[key])


def h_vector(row: dict[str, str]) -> dict[str, float]:
    x = f(row, "x_km")
    y = f(row, "y_km")
    z = f(row, "z_km")
    vx = f(row, "vx_km_s")
    vy = f(row, "vy_km_s")
    vz = f(row, "vz_km_s")
    hx = y * vz - z * vy
    hy = z * vx - x * vz
    hz = x * vy - y * vx
    mag = math.sqrt(hx * hx + hy * hy + hz * hz)
    return {"hx_km2_s": hx, "hy_km2_s": hy, "hz_km2_s": hz, "h_vector_km2_s": mag}


def main() -> int:
    seed = load_mars_seed()
    rows = load_vector_rows()
    if not rows:
        raise RuntimeError("No vector rows found")

    mu = float(seed["mu_central_km3_s2"])
    a = float(seed["semi_major_axis_km"])
    e = float(seed["eccentricity"])
    h_seed = math.sqrt(mu * a * (1.0 - e * e))

    items = []
    for row in rows:
        hv = h_vector(row)
        residual = hv["h_vector_km2_s"] - h_seed
        relative = residual / h_seed
        items.append({
            "record_id": seed["record_id"],
            "body_system": seed["body_system"],
            "calendar_tdb": row["calendar_tdb"],
            "jd_tdb": float(row["jd_tdb"]),
            "state_vector_km_km_s": {
                "x_km": f(row, "x_km"),
                "y_km": f(row, "y_km"),
                "z_km": f(row, "z_km"),
                "vx_km_s": f(row, "vx_km_s"),
                "vy_km_s": f(row, "vy_km_s"),
                "vz_km_s": f(row, "vz_km_s"),
            },
            "h_vector_components": hv,
            "h_seed_formula_km2_s": h_seed,
            "state_vector_vs_reference_h_residual_km2_s": residual,
            "state_vector_vs_reference_h_relative_residual": relative,
            "claim_allowed": False,
        })

    payload = {
        "schema_version": "0.1",
        "status": "orbital_state_vector_v2_generated",
        "module": "orbital_shape_angular_momentum",
        "claim_allowed": False,
        "input_raw_file": RAW_VECTOR_CSV.as_posix(),
        "seed_file": SEED_CSV.as_posix(),
        "formula": {
            "h_vector": "|r x v|",
            "h_seed": "sqrt(mu*a*(1-e^2))",
            "relative_residual": "(h_vector - h_seed) / h_seed",
        },
        "items": items,
        "claim_boundary": "This compares Horizons state-vector h with a seed formula. It is a v2 metric artifact, not a new-gravity or RLL superiority claim.",
        "required_next_data": [
            "longer state-vector time series",
            "baseline precision model",
            "uncertainty/error model",
            "same calculation for Earth/Jupiter/Moon where appropriate",
        ],
        "safe_conclusion": "Orbital v2 computes a real vector residual from raw state vectors, but final scientific claims remain blocked.",
    }

    OUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    OUT_MD.parent.mkdir(parents=True, exist_ok=True)
    OUT_JSON.write_text(json.dumps(payload, indent=2, ensure_ascii=False, allow_nan=False) + "\n", encoding="utf-8")
    write_report(payload)
    print(f"wrote {OUT_JSON}")
    print(f"wrote {OUT_MD}")
    return 0


def write_report(payload: dict) -> None:
    first = payload["items"][0]
    lines = [
        "# Orbital State Vector V2 Report",
        "",
        "Status: orbital state-vector v2 generated",
        "Claim level: `claim_allowed=false`",
        "",
        "## Formulae",
        "",
        "```text",
        "h_vector = |r x v|",
        "h_seed = sqrt(mu*a*(1-e^2))",
        "relative_residual = (h_vector - h_seed) / h_seed",
        "```",
        "",
        "## First row result",
        "",
        "| Field | Value |",
        "|---|---:|",
        f"| h_vector_km2_s | {first['h_vector_components']['h_vector_km2_s']} |",
        f"| h_seed_formula_km2_s | {first['h_seed_formula_km2_s']} |",
        f"| residual_km2_s | {first['state_vector_vs_reference_h_residual_km2_s']} |",
        f"| relative_residual | {first['state_vector_vs_reference_h_relative_residual']} |",
        "",
        "## Safe conclusion",
        "",
        "Orbital v2 computes a real vector residual from raw state vectors, but final scientific claims remain blocked.",
        "",
    ]
    OUT_MD.write_text("\n".join(lines), encoding="utf-8")


if __name__ == "__main__":
    raise SystemExit(main())
