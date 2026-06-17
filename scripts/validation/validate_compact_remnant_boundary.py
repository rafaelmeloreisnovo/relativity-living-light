#!/usr/bin/env python3
"""Validate compact-remnant boundary seeds v0.

This script performs only seed-level checks:
- GW230529 primary mass overlap with lower mass gap.
- PSR J0740+6620 consistency as a high-mass neutron-star constraint.

It does not ingest posterior samples or EOS tables yet.
"""

from __future__ import annotations

from pathlib import Path

from real_seed_utils import base_payload, extract_value, find_seed, parse_asymmetric_radius, parse_pm, parse_range, write_json

OUT = Path("data/results/compact_objects/remnant_boundary_validation.json")


def classify_mass_gap(mass_range: list[float] | None) -> str:
    if not mass_range:
        return "TOKEN_VAZIO"
    low, high = mass_range
    if high < 2.5:
        return "neutron_star_range_candidate"
    if low <= 5.0 and high >= 2.5:
        return "lower_mass_gap_overlap"
    if low > 5.0:
        return "stellar_black_hole_range_candidate"
    return "ambiguous"


def main() -> int:
    gw = find_seed("REAL_SEED_GW230529_181500")
    ns = find_seed("REAL_SEED_PSR_J0740_6620")

    primary_range = parse_range(extract_value(gw, "primary_mass_msun_90pct_range"))
    secondary_range = parse_range(extract_value(gw, "secondary_mass_msun_90pct_range"))
    ns_mass = parse_pm(extract_value(ns, "gravitational_mass_msun"))
    ns_radius = parse_asymmetric_radius(extract_value(ns, "radius_km_68pct"))

    payload = base_payload(
        "compact_remnant_boundary",
        ["REAL_SEED_GW230529_181500", "REAL_SEED_PSR_J0740_6620"],
    )
    payload.update(
        {
            "calculations": {
                "GW230529_181500": {
                    "primary_mass_msun_90pct_range": primary_range,
                    "secondary_mass_msun_90pct_range": secondary_range,
                    "primary_classification_v0": classify_mass_gap(primary_range),
                    "secondary_classification_v0": classify_mass_gap(secondary_range),
                    "interpretation_v0": "primary overlaps the lower compact-object mass gap; component nature remains classification-boundary, not proof of BH or NS without posterior/baseline ingestion",
                },
                "PSR_J0740_6620": {
                    "mass_msun": ns_mass,
                    "radius_km": ns_radius,
                    "classification_v0": "high_mass_neutron_star_constraint",
                    "interpretation_v0": "seed anchor for neutron-star maximum mass and EOS boundary; not a standalone EOS validation",
                },
            },
            "required_next_data": [
                "LVK/GWOSC posterior samples for GW230529_181500",
                "pulsar timing mass table for PSR J0740+6620",
                "EOS baseline table or literature constraints",
                "uncertainty propagation and posterior overlap calculation",
            ],
            "status": "seed_metric_ready_claim_blocked",
        }
    )
    write_json(OUT, payload)
    print(f"wrote {OUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
