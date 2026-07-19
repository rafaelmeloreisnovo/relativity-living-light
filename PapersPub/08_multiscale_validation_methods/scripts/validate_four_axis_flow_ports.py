#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path


def validate() -> dict[str, object]:
    center = (3.0, 0.0)
    radius = 1.0
    definitions = (
        ("upper", "vertical", math.pi / 2.0, (0, 1)),
        ("lower", "vertical", 3.0 * math.pi / 2.0, (0, -1)),
        ("right", "horizontal", 0.0, (1, 0)),
        ("left", "horizontal", math.pi, (-1, 0)),
        ("upper_right", "diagonal_rising", math.pi / 4.0, (1, 1)),
        ("lower_left", "diagonal_rising", 5.0 * math.pi / 4.0, (-1, -1)),
        ("upper_left", "diagonal_falling", 3.0 * math.pi / 4.0, (-1, 1)),
        ("lower_right", "diagonal_falling", 7.0 * math.pi / 4.0, (1, -1)),
    )
    ports = []
    for name, axis, angle, direction in definitions:
        nx, ny = math.cos(angle), math.sin(angle)
        px, py = center[0] + radius * nx, center[1] + radius * ny
        tangent = (-ny, nx)
        line_c = -(nx * px + ny * py)
        ports.append(
            {
                "name": name,
                "axis": axis,
                "angle": angle,
                "direction": direction,
                "position": (px, py),
                "normal": (nx, ny),
                "tangent": tangent,
                "line": (nx, ny, line_c),
            }
        )

    by_axis: dict[str, list[dict[str, object]]] = {}
    for port in ports:
        by_axis.setdefault(port["axis"], []).append(port)

    expected = {
        (0, 1),
        (0, -1),
        (1, 0),
        (-1, 0),
        (1, 1),
        (-1, -1),
        (-1, 1),
        (1, -1),
    }

    checks = {
        "four_axes": len(by_axis) == 4,
        "eight_ports": len(ports) == 8,
        "two_ports_per_axis": all(len(items) == 2 for items in by_axis.values()),
        "opposed_midpoint_is_center": all(
            math.isclose(
                (items[0]["position"][0] + items[1]["position"][0]) / 2.0,
                center[0],
                abs_tol=1e-12,
            )
            and math.isclose(
                (items[0]["position"][1] + items[1]["position"][1]) / 2.0,
                center[1],
                abs_tol=1e-12,
            )
            for items in by_axis.values()
        ),
        "diameter_is_2r": all(
            math.isclose(
                math.hypot(
                    items[0]["position"][0] - items[1]["position"][0],
                    items[0]["position"][1] - items[1]["position"][1],
                ),
                2.0 * radius,
                abs_tol=1e-12,
            )
            for items in by_axis.values()
        ),
        "ports_on_circle": all(
            math.isclose(
                math.hypot(
                    port["position"][0] - center[0],
                    port["position"][1] - center[1],
                ),
                radius,
                abs_tol=1e-12,
            )
            for port in ports
        ),
        "tangent_perpendicular": all(
            math.isclose(
                port["normal"][0] * port["tangent"][0]
                + port["normal"][1] * port["tangent"][1],
                0.0,
                abs_tol=1e-12,
            )
            for port in ports
        ),
        "tangent_line_distance_is_r": all(
            math.isclose(
                abs(
                    port["line"][0] * center[0]
                    + port["line"][1] * center[1]
                    + port["line"][2]
                )
                / math.hypot(port["line"][0], port["line"][1]),
                radius,
                abs_tol=1e-12,
            )
            for port in ports
        ),
        "eight_matrix_directions": {port["direction"] for port in ports}
        == expected,
        "diagonal_normalization": all(
            math.isclose(
                abs(dc / math.hypot(dc, dr)),
                1.0 / math.sqrt(2.0),
                abs_tol=1e-12,
            )
            and math.isclose(
                abs(dr / math.hypot(dc, dr)),
                1.0 / math.sqrt(2.0),
                abs_tol=1e-12,
            )
            for dc, dr in expected
            if abs(dc) == abs(dr) == 1
        ),
        "torus_sweep_preserves_meridian_radius": all(
            math.isclose(
                math.hypot(
                    math.hypot(
                        port["position"][0] * math.cos(0.73),
                        port["position"][0] * math.sin(0.73),
                    )
                    - center[0],
                    port["position"][1] - center[1],
                ),
                radius,
                abs_tol=1e-12,
            )
            for port in ports
        ),
        "physical_claims_blocked": True,
    }
    passed = sum(checks.values())
    return {
        "schema": "paper.validation.four_axis_flow_ports.v1",
        "checks_total": len(checks),
        "checks_passed": passed,
        "checks_failed": len(checks) - passed,
        "exact_geometry_state": "PASS" if all(checks.values()) else "FAIL",
        "physical_claims_state": "TOKEN_VAZIO",
        "claim_allowed": False,
        "axis_count": 4,
        "port_count": 8,
        "checks": checks,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        default="PapersPub/08_multiscale_validation_methods/results/four_axis_flow_ports_validation.json",
    )
    args = parser.parse_args()
    report = validate()
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(
        json.dumps(report, indent=2, ensure_ascii=False, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(report, indent=2, ensure_ascii=False, sort_keys=True))
    return 0 if report["exact_geometry_state"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
