from __future__ import annotations

import json
from pathlib import Path


def test_transfer_contract_exists_and_keeps_exact_outputs_open():
    path = Path(__file__).resolve().parents[1] / "src" / "rll" / "rll_transfer_bridge_contract.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    assert data["status"] == "transfer_bridge_contract_available"
    assert "T_k_z" in data["outputs"]
    assert "P_linear_bridge" in data["outputs"]
    assert data["exact_cl_cmb"] == "TOKEN_VAZIO"
    assert data["exact_nonlinear_pk"] == "TOKEN_VAZIO"
