#!/usr/bin/env python3
"""Validate dark-lens / isolated BH seed candidates v0.

Uses the OGLE-2011-BLG-0462 seed record as an external-only anchor.
This is a seed-level calculation, not raw microlensing model validation.
"""

from __future__ import annotations

from pathlib import Path

from real_seed_utils import base_payload, extract_value, find_seed, parse_pm, write_json

OUT = Path("data/results/compact_objects/wandering_bh_validation.json")


def mass_class(value: float | None) -> str:
    if value is None:
        return "TOKEN_VAZIO"
    if value < 2.5:
        return "neutron_star_or_low_mass_compact_candidate"
    if value < 5.0:
        return "lower_mass_gap_candidate"
    return "stellar_mass_black_hole_candidate"


def main() -> int:
    row = find_seed("REAL_SEED_OGLE_2011_BLG_0462")
    mass = parse_pm(extract_value(row, "lens_mass_msun"))
    distance = parse_pm(extract_value(row, "lens_distance_kpc"))
    velocity = parse_pm(extract_value(row, "space_velocity_km_s"))

    payload = base_payload("wandering_black_holes_dark_lens", ["REAL_SEED_OGLE_2011_BLG_0462"])
    payload.update(
        {
            "calculations": {
                "OGLE_2011_BLG_0462": {
                    "lens_mass_msun": mass,
                    "lens_distance_kpc": distance,
                    "space_velocity_km_s": velocity,
                    "mass_classification_v0": mass_class(mass.get("value")),
                    "silent_or_dark_lens_relevance_v0": "candidate mass is in stellar-mass black-hole range and seed source reports no detected lens light; still requires raw astrometric/photometric ingestion and alternative-model comparison",
                }
            },
            "required_next_data": [
                "microlensing light curve table",
                "astrometric displacement table",
                "lens-source geometry parameters",
                "luminous counterpart search limits",
                "alternative lens model comparison",
            ],
            "status": "seed_metric_ready_claim_blocked",
        }
    )
    write_json(OUT, payload)
    print(f"wrote {OUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
