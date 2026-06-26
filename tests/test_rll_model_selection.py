from __future__ import annotations

import importlib.util
import math
import sys
from pathlib import Path


def load_module():
    path = Path(__file__).resolve().parents[1] / "rll_vs_lcdm.py"
    spec = importlib.util.spec_from_file_location("rll_vs_lcdm_under_test", path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def test_rll_transition_has_expected_midpoint_and_bounds():
    rll = load_module()
    assert math.isclose(rll.rll_transition_f(1.164, 1.164, 0.405), 0.5)
    assert 0.0 < rll.rll_transition_f(5.0, 1.164, 0.405) < 0.001
    assert 0.9 < rll.rll_transition_f(0.0, 1.164, 0.405) < 1.0


def test_rll_logistic_is_distinct_from_w0wa_adversary():
    rll = load_module()
    z = 0.8
    e_cpl = rll.e_w0wa(z, om=0.315, w0=-0.95, wa=-0.2)
    e_log = rll.e_rll_logistic(z, om=0.315, omega_s0=0.059, zt=1.164, wt=0.405)
    assert e_cpl > 0.0
    assert e_log > 0.0
    assert abs(e_cpl - e_log) > 1e-5


def test_bayes_factor_from_bic_favors_lower_bic():
    rll = load_module()
    assert rll.bayes_factor_from_bic(bic_candidate=10.0, bic_reference=14.0) > 1.0
    assert rll.bayes_factor_from_bic(bic_candidate=14.0, bic_reference=10.0) < 1.0
