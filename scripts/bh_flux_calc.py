#!/usr/bin/env python3
"""RLL black-hole mass-flux benchmark calculator.

This script computes a reproducible diagnostic layer for black-hole
mass accretion. It is a benchmark wrapper only; it is not a substitute
for GR, Kerr geometry, GRMHD simulations, radiative transfer, or
observational parameter inference.
"""

import argparse
import json
import math

G = 6.67430e-11
C = 299792458.0
M_SUN = 1.98847e30
YEAR_S = 365.25 * 24 * 3600

PRESETS = {
    "sgr-a-star": {
        "m_bh_solar": 4.3e6,
        "mdot_solar_year": 1e-8,
        "description": "Approximate quiet Galactic Center black-hole benchmark."
    },
    "m87-star-low": {
        "m_bh_solar": 6.5e9,
        "mdot_solar_year": 3e-4,
        "description": "Low-order M87* EHT-style accretion benchmark."
    },
    "quasar-demo": {
        "m_bh_solar": 1e9,
        "mdot_solar_year": 1.0,
        "description": "Illustrative active quasar-scale benchmark."
    },
}


def clamp_weight(value, name):
    if value < 0.0:
        raise ValueError(f"{name} must be non-negative")
    return value


def compute(
    m_bh_solar,
    mdot_solar_year,
    unit_mass_kg,
    c_b=1.0,
    c_pol=1.0,
    theta_rad=1.0,
    s_kerr=1.0,
):
    if m_bh_solar <= 0.0:
        raise ValueError("m_bh_solar must be positive")
    if mdot_solar_year < 0.0:
        raise ValueError("mdot_solar_year must be non-negative")
    if unit_mass_kg <= 0.0:
        raise ValueError("unit_mass_kg must be positive")

    c_b = clamp_weight(c_b, "c_b")
    c_pol = clamp_weight(c_pol, "c_pol")
    theta_rad = clamp_weight(theta_rad, "theta_rad")
    s_kerr = clamp_weight(s_kerr, "s_kerr")

    m_bh_kg = m_bh_solar * M_SUN
    mdot_kg_s = mdot_solar_year * M_SUN / YEAR_S
    rs_m = 2.0 * G * m_bh_kg / (C * C)
    area_m2 = 4.0 * math.pi * rs_m * rs_m
    phi_m = mdot_kg_s / area_m2 if area_m2 > 0.0 else float("nan")
    ndot = mdot_kg_s / unit_mass_kg
    growth_s = mdot_kg_s / m_bh_kg

    base_log_index = math.log10(1.0 + ndot) * math.log10(1.0 + phi_m)
    weighted_index = base_log_index * c_b * c_pol * theta_rad * s_kerr

    return {
        "M_bh_solar": m_bh_solar,
        "M_bh_kg": m_bh_kg,
        "Mdot_solar_year": mdot_solar_year,
        "Mdot_kg_s": mdot_kg_s,
        "schwarzschild_radius_m": rs_m,
        "horizon_area_m2": area_m2,
        "mass_flux_kg_s_m2": phi_m,
        "unit_mass_kg": unit_mass_kg,
        "unit_count_per_second": ndot,
        "normalized_growth_per_second": growth_s,
        "C_B": c_b,
        "C_pol": c_pol,
        "Theta_rad": theta_rad,
        "S_Kerr": s_kerr,
        "rll_bh_flux_base_log_index": base_log_index,
        "rll_bh_flux_weighted_index": weighted_index,
        "claim_boundary": "benchmark only; not cosmological proof"
    }


def main():
    parser = argparse.ArgumentParser(description="RLL black-hole mass-flux benchmark calculator")
    parser.add_argument("--preset", choices=sorted(PRESETS), help="Use a named benchmark preset")
    parser.add_argument("--m-bh-solar", type=float, help="Black-hole mass in solar masses")
    parser.add_argument("--mdot-solar-year", type=float, help="Accretion rate in solar masses per year")
    parser.add_argument("--unit-mass-kg", type=float, default=3e-25, help="Reference microscopic mass unit in kg")
    parser.add_argument("--c-b", type=float, default=1.0, help="Magnetic-field coherence/normalization weight")
    parser.add_argument("--c-pol", type=float, default=1.0, help="Polarization coherence/normalization weight")
    parser.add_argument("--theta-rad", type=float, default=1.0, help="Radiative coupling/normalization weight")
    parser.add_argument("--s-kerr", type=float, default=1.0, help="Spin/Kerr correction placeholder")
    args = parser.parse_args()

    if args.preset:
        preset = PRESETS[args.preset]
        m_bh_solar = args.m_bh_solar if args.m_bh_solar is not None else preset["m_bh_solar"]
        mdot_solar_year = args.mdot_solar_year if args.mdot_solar_year is not None else preset["mdot_solar_year"]
        description = preset["description"]
    else:
        if args.m_bh_solar is None or args.mdot_solar_year is None:
            parser.error("Either --preset or both --m-bh-solar and --mdot-solar-year are required")
        m_bh_solar = args.m_bh_solar
        mdot_solar_year = args.mdot_solar_year
        description = "custom benchmark"

    result = compute(
        m_bh_solar,
        mdot_solar_year,
        args.unit_mass_kg,
        args.c_b,
        args.c_pol,
        args.theta_rad,
        args.s_kerr,
    )
    result["description"] = description
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
