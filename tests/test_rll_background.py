from __future__ import annotations

import importlib.util
import sys
from pathlib import Path


def load_module():
    path = Path(__file__).resolve().parents[1] / "scripts" / "check_rll_background.py"
    spec = importlib.util.spec_from_file_location("check_rll_background_under_test", path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def test_rll_background_central_parameters_pass_minimum_gate():
    bg = load_module()
    z_values = [0.0, 0.5, 1.164, 2.0, 5.0]
    for z in z_values:
        assert bg.f_transition(z, 1.164, 0.405) >= 0.0
        assert bg.f_transition(z, 1.164, 0.405) <= 1.0
        assert bg.w_eff(z, 1.164, 0.405) >= -1.0
        assert bg.kinetic_gate(z, 0.315, 0.059, 1.164, 0.405) >= 0.0


def test_rll_background_transition_midpoint():
    bg = load_module()
    assert bg.f_transition(1.164, 1.164, 0.405) == 0.5


def test_rll_background_rejects_non_positive_width():
    bg = load_module()
    try:
        bg.f_transition(1.0, 1.164, 0.0)
    except ValueError as exc:
        assert "wt" in str(exc)
    else:
        raise AssertionError("non-positive wt must raise ValueError")
