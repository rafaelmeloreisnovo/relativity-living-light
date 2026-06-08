import importlib.util
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "bh_flux_calc.py"

spec = importlib.util.spec_from_file_location("bh_flux_calc", SCRIPT)
bh_flux_calc = importlib.util.module_from_spec(spec)
spec.loader.exec_module(bh_flux_calc)


def test_compute_returns_required_fields():
    out = bh_flux_calc.compute(
        m_bh_solar=4.3e6,
        mdot_solar_year=1e-8,
        unit_mass_kg=3e-25,
    )
    required = {
        "M_bh_solar",
        "M_bh_kg",
        "Mdot_solar_year",
        "Mdot_kg_s",
        "schwarzschild_radius_m",
        "horizon_area_m2",
        "mass_flux_kg_s_m2",
        "unit_mass_kg",
        "unit_count_per_second",
        "normalized_growth_per_second",
        "C_B",
        "C_pol",
        "Theta_rad",
        "S_Kerr",
        "rll_bh_flux_base_log_index",
        "rll_bh_flux_weighted_index",
        "claim_boundary",
    }
    assert required.issubset(out.keys())


def test_physical_outputs_are_positive_for_positive_accretion():
    out = bh_flux_calc.compute(4.3e6, 1e-8, 3e-25)
    assert out["M_bh_kg"] > 0.0
    assert out["Mdot_kg_s"] > 0.0
    assert out["schwarzschild_radius_m"] > 0.0
    assert out["horizon_area_m2"] > 0.0
    assert out["mass_flux_kg_s_m2"] > 0.0
    assert out["unit_count_per_second"] > 0.0
    assert out["normalized_growth_per_second"] > 0.0


def test_weighted_index_scales_linearly_with_weights():
    base = bh_flux_calc.compute(1e6, 1e-8, 3e-25)
    weighted = bh_flux_calc.compute(
        1e6,
        1e-8,
        3e-25,
        c_b=2.0,
        c_pol=0.5,
        theta_rad=3.0,
        s_kerr=1.0,
    )
    assert weighted["rll_bh_flux_weighted_index"] == base["rll_bh_flux_base_log_index"] * 3.0


def test_zero_accretion_has_zero_unit_count_and_zero_index():
    out = bh_flux_calc.compute(1e6, 0.0, 3e-25)
    assert out["Mdot_kg_s"] == 0.0
    assert out["unit_count_per_second"] == 0.0
    assert out["rll_bh_flux_base_log_index"] == 0.0
    assert out["rll_bh_flux_weighted_index"] == 0.0


def test_invalid_inputs_raise_value_error():
    for args in [
        (0.0, 1e-8, 3e-25),
        (1e6, -1e-8, 3e-25),
        (1e6, 1e-8, 0.0),
    ]:
        try:
            bh_flux_calc.compute(*args)
        except ValueError:
            pass
        else:
            raise AssertionError("expected ValueError")
