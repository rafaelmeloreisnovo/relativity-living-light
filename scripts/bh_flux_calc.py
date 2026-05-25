#!/usr/bin/env python3
import argparse
import json
import math

G = 6.67430e-11
C = 299792458.0
M_SUN = 1.98847e30
YEAR_S = 365.25 * 24 * 3600


def compute(m_bh_solar, mdot_solar_year, unit_mass_kg):
    m_bh_kg = m_bh_solar * M_SUN
    mdot_kg_s = mdot_solar_year * M_SUN / YEAR_S
    rs_m = 2.0 * G * m_bh_kg / (C * C)
    area_m2 = 4.0 * math.pi * rs_m * rs_m
    phi_m = mdot_kg_s / area_m2
    ndot = mdot_kg_s / unit_mass_kg
    growth_s = mdot_kg_s / m_bh_kg
    rll_bh_flux_log_index = math.log10(1.0 + ndot) * math.log10(1.0 + phi_m)
    return {
        "M_bh_kg": m_bh_kg,
        "Mdot_kg_s": mdot_kg_s,
        "schwarzschild_radius_m": rs_m,
        "horizon_area_m2": area_m2,
        "mass_flux_kg_s_m2": phi_m,
        "unit_mass_kg": unit_mass_kg,
        "unit_count_per_second": ndot,
        "normalized_growth_per_second": growth_s,
        "rll_bh_flux_log_index": rll_bh_flux_log_index,
        "claim_boundary": "benchmark only; not cosmological proof"
    }


def main():
    parser = argparse.ArgumentParser(description="RLL black-hole mass-flux benchmark calculator")
    parser.add_argument("--m-bh-solar", type=float, required=True)
    parser.add_argument("--mdot-solar-year", type=float, required=True)
    parser.add_argument("--unit-mass-kg", type=float, default=3e-25)
    args = parser.parse_args()
    print(json.dumps(compute(args.m_bh_solar, args.mdot_solar_year, args.unit_mass_kg), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
