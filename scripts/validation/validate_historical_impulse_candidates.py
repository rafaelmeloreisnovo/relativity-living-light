#!/usr/bin/env python3
"""Validate historical impulse / hypervelocity seed candidates v0.

Uses the LMC hypervelocity-star seed as an external-only anchor.
This script does not reconstruct orbits yet; it records the first calculable constraints.
"""

from __future__ import annotations

from pathlib import Path

from real_seed_utils import base_payload, extract_value, find_seed, parse_float, write_json

OUT = Path("data/results/kinematics/historical_impulse_validation.json")


def main() -> int:
    row = find_seed("REAL_SEED_LMC_HYPERVELOCITY_SMBH")
    count = parse_float(extract_value(row, "reported_HVS_count"))
    mass = parse_float(extract_value(row, "inferred_mass_msun"))

    payload = base_payload("historical_impulse_slingshot", ["REAL_SEED_LMC_HYPERVELOCITY_SMBH"])
    payload.update(
        {
            "calculations": {
                "LMC_HVS_traceback_seed": {
                    "reported_HVS_count": count,
                    "approximately_half_trace_to_LMC": True,
                    "inferred_central_mass_msun_approx": mass,
                    "mechanism_seed": "Hills_mechanism_forward_model",
                    "classification_v0": "historical_impulse_origin_trace_seed",
                    "interpretation_v0": "seed supports a future trajectory-memory/slingshot validation path; not a proof of an LMC SMBH without catalog ingestion and traceback recomputation",
                }
            },
            "required_next_data": [
                "HVS object-level catalog with position, proper motion, distance, radial velocity",
                "Milky Way and LMC potential models",
                "traceback probability computation",
                "Galactic Center vs LMC origin model comparison",
                "escape velocity context",
            ],
            "status": "seed_metric_ready_claim_blocked",
        }
    )
    write_json(OUT, payload)
    print(f"wrote {OUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
