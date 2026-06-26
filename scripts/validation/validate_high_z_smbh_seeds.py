#!/usr/bin/env python3
"""Validate high-redshift SMBH seed v0.

Uses UHZ1 seed record as an external-only anchor.
Computes simple Eddington e-folding requirements, not a final growth model.
"""

from __future__ import annotations

import math
from pathlib import Path

from real_seed_utils import base_payload, extract_value, find_seed, parse_float, write_json

OUT = Path("data/results/high_z_smbh/seed_validation.json")
SALPETER_TIME_MYR = 45.0  # approximate e-folding time for radiatively efficient Eddington-limited growth


def seed_mass_required(final_mass: float, available_myr: float, eddington_fraction: float = 1.0) -> float:
    if final_mass <= 0 or available_myr <= 0 or eddington_fraction <= 0:
        return float("nan")
    e_folds = available_myr / SALPETER_TIME_MYR * eddington_fraction
    return final_mass / math.exp(e_folds)


def main() -> int:
    row = find_seed("REAL_SEED_UHZ1_HIGHZ_SMBH")
    z = parse_float(extract_value(row, "redshift"))
    mass = parse_float(extract_value(row, "estimated_BH_mass_msun"))
    age = parse_float(extract_value(row, "age_after_big_bang_myr"))

    # A deliberately simple lower-level seed calculation:
    # assume growth can start after 100 Myr, leaving age - 100 Myr.
    available = max((age or 0) - 100.0, 0.0)
    required_seed = seed_mass_required(mass or 0, available, 1.0)

    payload = base_payload("high_z_smbh_seeds", ["REAL_SEED_UHZ1_HIGHZ_SMBH"])
    payload.update(
        {
            "constants": {
                "salpeter_time_myr_assumed": SALPETER_TIME_MYR,
                "growth_start_age_myr_assumed": 100.0,
            },
            "calculations": {
                "UHZ1": {
                    "redshift": z,
                    "estimated_black_hole_mass_msun": mass,
                    "age_after_big_bang_myr": age,
                    "available_growth_time_myr_assumed": available,
                    "required_seed_mass_msun_at_eddington_v0": required_seed,
                    "classification_v0": "high_z_overmassive_black_hole_seed_constraint",
                    "interpretation_v0": "simple Eddington e-folding estimate only; requires raw photometry/spectroscopy, magnification check, accretion model, and host constraints before claim",
                }
            },
            "required_next_data": [
                "spectroscopic/photometric redshift source table",
                "black-hole mass estimation method and uncertainty",
                "lensing magnification check",
                "host-galaxy mass constraints",
                "light-seed vs heavy-seed vs direct-collapse baseline models",
            ],
            "status": "seed_metric_ready_claim_blocked",
        }
    )
    write_json(OUT, payload)
    print(f"wrote {OUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
