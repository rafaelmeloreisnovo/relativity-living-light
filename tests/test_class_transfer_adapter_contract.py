from __future__ import annotations

import json
from pathlib import Path


def test_class_transfer_adapter_contract_is_present():
    path = Path(__file__).resolve().parents[1] / "src" / "rll" / "class_transfer_adapter_contract.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    assert data["status"] == "class_transfer_adapter_contract_available"
    assert data["model"] == "rll"
    assert data["backend_target"] == "CLASS_or_CAMB_custom_transfer_layer"
    assert data["exact_cl_cmb"] == "TOKEN_VAZIO"
    assert data["exact_nonlinear_pk"] == "TOKEN_VAZIO"
