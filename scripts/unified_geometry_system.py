"""Unified geometric system generator (non-binary outputs only).

Generates CSV summaries and a JSON manifest for:
triangle, square, circle, cube, sphere, tetrahedron, bipyramid, torus.
"""

from __future__ import annotations

import argparse
import csv
import json
import math
from dataclasses import dataclass, asdict
from pathlib import Path


@dataclass
class ShapeRecord:
    name: str
    dimension: int
    area: float | None
    volume: float | None
    delta: float | None
    radial_scale: float | None
    invariant_I: float | None


def triangle_area(a: float) -> float:
    return (math.sqrt(3) / 4.0) * a * a


def square_area(a: float) -> float:
    return a * a


def circle_area(r: float) -> float:
    return math.pi * r * r


def cube_volume(a: float) -> float:
    return a**3


def sphere_volume(r: float) -> float:
    return (4.0 / 3.0) * math.pi * r**3


def tetrahedron_volume(a: float) -> float:
    return a**3 / (6.0 * math.sqrt(2))


def bipyramid_volume(a: float) -> float:
    return 2.0 * tetrahedron_volume(a)


def torus_area(R: float, r: float) -> float:
    return 4.0 * math.pi**2 * R * r


def torus_volume(R: float, r: float) -> float:
    return 2.0 * math.pi**2 * R * r * r


def build_records(a: float, r: float, R: float) -> list[ShapeRecord]:
    delta = R - r
    radial_scale = R / r
    invariant_I = R * R - r * r

    return [
        ShapeRecord("triangle_equilateral", 2, triangle_area(a), None, None, None, None),
        ShapeRecord("square", 2, square_area(a), None, None, None, None),
        ShapeRecord("circle", 2, circle_area(r), None, None, None, None),
        ShapeRecord("cube", 3, None, cube_volume(a), None, None, None),
        ShapeRecord("sphere", 3, None, sphere_volume(r), None, None, None),
        ShapeRecord("tetrahedron", 3, None, tetrahedron_volume(a), None, None, None),
        ShapeRecord("bipyramid", 3, None, bipyramid_volume(a), None, None, None),
        ShapeRecord("torus", 3, torus_area(R, r), torus_volume(R, r), delta, radial_scale, invariant_I),
    ]


def write_csv(records: list[ShapeRecord], out_csv: Path) -> None:
    out_csv.parent.mkdir(parents=True, exist_ok=True)
    with out_csv.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(asdict(records[0]).keys()))
        writer.writeheader()
        for rec in records:
            writer.writerow(asdict(rec))


def write_manifest(records: list[ShapeRecord], out_json: Path, a: float, r: float, R: float) -> None:
    out_json.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "parameters": {"a": a, "r": r, "R": R, "Delta": R - r, "lambda": R / r, "I": R * R - r * r},
        "records": [asdict(x) for x in records],
        "policy": "textual_artifacts_only",
    }
    out_json.write_text(json.dumps(payload, indent=2), encoding="utf-8")


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--a", type=float, default=1.0)
    p.add_argument("--r", type=float, default=1.0)
    p.add_argument("--R", type=float, default=2.0)
    p.add_argument("--out-csv", default="results/unified_geometry/shapes.csv")
    p.add_argument("--out-json", default="results/unified_geometry/manifest.json")
    args = p.parse_args()

    if args.r <= 0 or args.R <= 0 or args.a <= 0:
        raise ValueError("a, r, R must be positive")
    if args.R <= args.r:
        raise ValueError("Require R > r for ring torus")

    records = build_records(args.a, args.r, args.R)
    write_csv(records, Path(args.out_csv))
    write_manifest(records, Path(args.out_json), args.a, args.r, args.R)


if __name__ == "__main__":
    main()
