from __future__ import annotations

import importlib.util
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "tools/validate_fundamental_real_data_topology.py"


def load_validator():
    spec = importlib.util.spec_from_file_location("fundamental_real_data_topology", MODULE_PATH)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_fundamental_real_data_topology_passes() -> None:
    receipt = load_validator().run()
    assert receipt["state"] == "PASS"
    assert receipt["claim_allowed"] is False
    assert receipt["manifest"]["verified"] == 5
    assert receipt["manifest"]["partial"] == 1
    assert receipt["forest"]["trees"] >= 6
    assert receipt["equation_registry"]["critical"] == [
        "logistic_transition",
        "null_limit_lcdm",
        "rll_friedmann_e2",
    ]
    assert receipt["pipeline"]["default_profile"] == "structure_d_fundamentals"
    assert receipt["pipeline"]["partial"] == ["real_pantheon_plus_shoes"]
