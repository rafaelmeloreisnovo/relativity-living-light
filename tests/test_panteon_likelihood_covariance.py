from __future__ import annotations

import importlib.util
from pathlib import Path

import numpy as np
import pytest


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("panteon_likelihood", ROOT / "docs" / "panteon_likelihood.py")
panteon_likelihood = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(panteon_likelihood)


def _write_lcparam(data_dir: Path) -> None:
    (data_dir / "lcparam_full_long_zhel.txt").write_text(
        "zhel mb dmb\n"
        "0.01 35.0 0.10\n"
        "0.02 36.0 0.20\n",
        encoding="utf-8",
    )


def test_load_pantheon_reads_official_stat_sys_covariance_with_header(tmp_path: Path) -> None:
    _write_lcparam(tmp_path)
    (tmp_path / "Pantheon+SH0ES_STAT+SYS.cov").write_text(
        "2\n"
        "0.04\n"
        "0.01\n"
        "0.01\n"
        "0.09\n",
        encoding="utf-8",
    )

    z_hel, mu_obs, c_inv, meta = panteon_likelihood.load_pantheon(str(tmp_path))

    expected_cov = np.array([[0.04, 0.01], [0.01, 0.09]])
    assert np.allclose(z_hel, [0.01, 0.02])
    assert np.allclose(mu_obs, [35.0, 36.0])
    assert np.allclose(c_inv, np.linalg.inv(expected_cov))
    assert meta["covariance_used"] == "Pantheon+SH0ES_STAT+SYS.cov"
    assert meta["has_systematics"] is True


def test_load_pantheon_rejects_covariance_dimension_mismatch(tmp_path: Path) -> None:
    _write_lcparam(tmp_path)
    (tmp_path / "Pantheon+SH0ES_STAT+SYS.cov").write_text(
        "3\n"
        "0.04\n0.01\n0.01\n0.09\n",
        encoding="utf-8",
    )

    with pytest.raises(ValueError, match="cabeçalho declara 3 observações"):
        panteon_likelihood.load_pantheon(str(tmp_path))


def test_load_pantheon_fails_missing_covariance_by_default(tmp_path: Path) -> None:
    _write_lcparam(tmp_path)

    with pytest.raises(FileNotFoundError, match="fallback diagonal silencioso"):
        panteon_likelihood.load_pantheon(str(tmp_path))


def test_load_pantheon_allows_explicit_diagonal_fallback(tmp_path: Path) -> None:
    _write_lcparam(tmp_path)

    _, _, c_inv, meta = panteon_likelihood.load_pantheon(str(tmp_path), require_covariance=False)

    assert np.allclose(c_inv, np.diag([100.0, 25.0]))
    assert meta["covariance_used"] is False
    assert meta["has_systematics"] is False
