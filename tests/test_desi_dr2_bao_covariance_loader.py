from __future__ import annotations

import importlib.util
import sys
from pathlib import Path


def load_module():
    path = Path(__file__).resolve().parents[1] / "scripts" / "check_desi_dr2_bao_covariance.py"
    spec = importlib.util.spec_from_file_location("desi_dr2_loader", path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def test_desi_dr2_core_shape():
    m = load_module()
    root = Path(__file__).resolve().parents[1]
    rows = m.read_mean(root / "data/real/cosmology/desi_bao_dr2_cobaya/desi_gaussian_bao_ALL_GCcomb_mean.tsv")
    cov = m.read_matrix(root / "data/real/cosmology/desi_bao_dr2_cobaya/desi_gaussian_bao_ALL_GCcomb_cov.tsv")
    assert len(rows) == 13
    assert len(cov) == 13
    assert all(len(row) == 13 for row in cov)
    assert rows[0][2] == "DV_over_rs"


def test_covariance_inverse_identity_size():
    m = load_module()
    inv = m.invert([[2.0, 0.0], [0.0, 4.0]])
    assert inv == [[0.5, 0.0], [0.0, 0.25]]


if __name__ == "__main__":
    test_desi_dr2_core_shape()
    test_covariance_inverse_identity_size()
    print("DESI DR2 BAO covariance loader tests passed")
