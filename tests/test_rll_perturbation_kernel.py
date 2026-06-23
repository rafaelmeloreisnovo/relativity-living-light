from __future__ import annotations

import argparse
import importlib.util
import sys
from pathlib import Path


def load_module():
    path = Path(__file__).resolve().parents[1] / "src" / "rll" / "rll_perturbation_kernel.py"
    spec = importlib.util.spec_from_file_location("rll_perturbation_kernel_under_test", path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def test_kernel_solves_positive_growth():
    k = load_module()
    p = argparse.Namespace(omega_m=0.315, omega_s0=0.059, zt=1.164, wt=0.405, a_min=1e-3, steps=400, out_csv="x.csv", out_json="x.json")
    rows = k.solve_kernel(p)
    assert rows[-1]["delta"] == 1.0
    assert rows[-1]["growth_rate"] > 0.0
    assert rows[0]["delta"] < rows[-1]["delta"]


def test_kernel_rejects_nonpositive_width():
    k = load_module()
    try:
        k.f_transition(0.0, 1.0, 0.0)
    except ValueError:
        pass
    else:
        raise AssertionError("expected ValueError")
