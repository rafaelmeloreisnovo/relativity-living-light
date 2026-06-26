from __future__ import annotations

import argparse
import importlib.util
import sys
from pathlib import Path


def load_module():
    path = Path(__file__).resolve().parents[1] / "scripts" / "check_rll_growth.py"
    spec = importlib.util.spec_from_file_location("check_rll_growth_under_test", path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def params(**kw):
    base = dict(
        omega_m=0.315,
        omega_s0=0.059,
        zt=1.164,
        wt=0.405,
        w0=-1.0,
        wa=0.0,
        sigma8_0=0.811,
        a_min=1.0e-3,
        steps=800,
        model="all",
        z_max=1.0,
        z_step=0.5,
        data=None,
        out_json="unused.json",
        out_csv="unused.csv",
    )
    base.update(kw)
    return argparse.Namespace(**base)


def test_lcdm_growth_normalizes_to_one_today():
    g = load_module()
    rows = g.integrate_growth("lcdm", params())
    assert abs(rows[-1]["D"] - 1.0) < 1e-9
    assert 0.4 < rows[-1]["f_growth"] < 0.7


def test_rll_growth_prediction_is_finite_and_positive():
    g = load_module()
    rows = g.integrate_growth("rll", params())
    for key in ["D", "f_growth", "fsigma8"]:
        assert rows[-1][key] > 0.0
    assert g.interp(rows, 1.0, "D") < 1.0


def test_evaluate_all_models_contains_adversary_and_rll():
    g = load_module()
    summary, predictions = g.evaluate_models(params())
    assert set(summary["models"].keys()) == {"lcdm", "w0wa", "rll"}
    assert predictions
    assert summary["assumptions"]["nonlinear_power"] == "TOKEN_VAZIO"
