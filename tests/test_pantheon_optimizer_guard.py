from __future__ import annotations

import importlib.util
from pathlib import Path
from types import SimpleNamespace

import numpy as np
import pytest

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("panteon_likelihood", ROOT / "docs" / "panteon_likelihood.py")
panteon_likelihood = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(panteon_likelihood)


def test_optimizer_diagnostics_record_initial_final_and_movement() -> None:
    def objective(theta, *_args):
        return float((theta[0] - 0.25) ** 2 + 3.0)

    res, diagnostics = panteon_likelihood._run_global_then_local_optimizer(
        objective,
        np.array([0.75]),
        [(0.0, 1.0)],
        (),
        "toy",
    )

    assert res.fun < diagnostics["initial_chi2"]
    assert diagnostics["final_chi2"] == pytest.approx(res.fun)
    assert diagnostics["nfev"] > 0
    assert diagnostics["parameter_movement_l2"] > 0.1
    assert "message" in diagnostics


def test_optimizer_guard_rejects_false_initial_point_convergence(monkeypatch: pytest.MonkeyPatch) -> None:
    def fake_differential_evolution(*_args, **_kwargs):
        return SimpleNamespace(x=np.array([0.5]), fun=1.0e9, nit=0, nfev=1, message="fake global stop")

    def fake_minimize(_objective, candidate, *_args, **_kwargs):
        return SimpleNamespace(
            x=np.asarray(candidate, dtype=float),
            fun=1.0e9,
            nit=0,
            nfev=1,
            success=True,
            message="fake local success at initial point",
        )

    monkeypatch.setattr(panteon_likelihood, "differential_evolution", fake_differential_evolution)
    monkeypatch.setattr(panteon_likelihood, "minimize", fake_minimize)

    def objective(theta, *_args):
        return float(1.0e9 + 1.0e6 * theta[0])

    with pytest.raises(RuntimeError, match="optimizer guard failed"):
        panteon_likelihood._run_global_then_local_optimizer(
            objective,
            np.array([0.5]),
            [(0.0, 1.0)],
            (),
            "toy",
        )
