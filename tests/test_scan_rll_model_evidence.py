"""Tests for tools/scan_rll_model_evidence.py.

Validates H0_all_equal detection, claim status derivation, and warning
emission — all of which are required by issue #423.
"""
from __future__ import annotations

import csv
import json
from pathlib import Path

import pytest

from tools.scan_rll_model_evidence import scan

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

_COLS = [
    "model", "chi2", "AIC", "AICc", "BIC",
    "N", "k", "dof",
    "H0", "Om", "Os0", "zt", "wt",
]

_REGISTRY_SCHEMA = "rll.parameter_origin_registry.v2"


def _make_csv(tmp_path: Path, rows: list[dict]) -> Path:
    path = tmp_path / "results.csv"
    fieldnames = list(rows[0].keys()) if rows else _COLS
    with path.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    return path


def _make_registry(tmp_path: Path, schema: str = _REGISTRY_SCHEMA) -> Path:
    path = tmp_path / "registry.json"
    path.write_text(json.dumps({"schema": schema}), encoding="utf-8")
    return path


def _base_rows(h0_lcdm: float = 67.0, h0_wcdm: float = 67.5,
               h0_cpl: float = 68.0, h0_rll: float = 67.0,
               os0_rll: float = 0.05) -> list[dict]:
    """Four-model result table with configurable H0 and Os0 values."""
    return [
        {"model": "LCDM_joint", "chi2": "100", "AIC": "106", "AICc": "106.5", "BIC": "112",
         "N": "64", "k": "3", "dof": "61", "H0": str(h0_lcdm), "Om": "0.31", "Os0": "", "zt": "", "wt": ""},
        {"model": "wCDM_joint", "chi2": "99", "AIC": "107", "AICc": "107.5", "BIC": "115",
         "N": "64", "k": "4", "dof": "60", "H0": str(h0_wcdm), "Om": "0.31", "Os0": "", "zt": "", "wt": ""},
        {"model": "CPL_w0waCDM_joint", "chi2": "90", "AIC": "100", "AICc": "101", "BIC": "110",
         "N": "64", "k": "5", "dof": "59", "H0": str(h0_cpl), "Om": "0.30", "Os0": "", "zt": "", "wt": ""},
        {"model": "RLL_joint", "chi2": "95", "AIC": "107", "AICc": "108", "BIC": "118",
         "N": "64", "k": "6", "dof": "58", "H0": str(h0_rll), "Om": "0.31", "Os0": str(os0_rll), "zt": "1.2", "wt": "0.4"},
    ]


# ---------------------------------------------------------------------------
# H0_all_equal detection
# ---------------------------------------------------------------------------

def test_h0_all_equal_true_emits_warning(tmp_path: Path) -> None:
    """When all H0 values are identical, H0_all_equal=True and a warning is emitted."""
    rows = _base_rows(h0_lcdm=60.0, h0_wcdm=60.0, h0_cpl=60.0, h0_rll=60.0)
    result = scan(_make_csv(tmp_path, rows), _make_registry(tmp_path))

    assert result.H0_all_equal is True
    assert any("H0_all_equal=True" in w for w in result.warnings), (
        "Expected H0_all_equal=True warning in warnings list"
    )


def test_h0_all_equal_warning_references_ablation_matrix(tmp_path: Path) -> None:
    """The H0_all_equal warning must reference the ablation matrix file."""
    rows = _base_rows(h0_lcdm=60.0, h0_wcdm=60.0, h0_cpl=60.0, h0_rll=60.0)
    result = scan(_make_csv(tmp_path, rows), _make_registry(tmp_path))

    assert result.H0_all_equal is True
    assert any("h0_rd_ablation_matrix" in w for w in result.warnings), (
        "H0_all_equal warning must reference the h0_rd_ablation_matrix file"
    )


def test_h0_not_all_equal_no_warning(tmp_path: Path) -> None:
    """When H0 values differ across models, H0_all_equal=False and no H0 warning is emitted."""
    rows = _base_rows(h0_lcdm=67.0, h0_wcdm=67.5, h0_cpl=68.0, h0_rll=67.2)
    result = scan(_make_csv(tmp_path, rows), _make_registry(tmp_path))

    assert result.H0_all_equal is False
    assert not any("H0_all_equal" in w for w in result.warnings)


# ---------------------------------------------------------------------------
# Claim status derivation
# ---------------------------------------------------------------------------

def test_claim_blocked_when_rll_os0_collapsed_to_zero(tmp_path: Path) -> None:
    """When RLL Os0=0, claim_status must be CLAIM_BLOCKED."""
    rows = _base_rows(os0_rll=0.0)
    result = scan(_make_csv(tmp_path, rows), _make_registry(tmp_path))

    assert result.claim_status == "CLAIM_BLOCKED"
    assert any("Os0" in r or "collapsed" in r for r in result.blocking_reasons)


def test_claim_blocked_when_rll_worse_than_cpl(tmp_path: Path) -> None:
    """When RLL AICc/BIC > CPL AICc/BIC (and Os0>0), claim_status is CLAIM_BLOCKED."""
    rows = _base_rows(os0_rll=0.05)
    # Default rows already have RLL AICc=108 > CPL AICc=101
    result = scan(_make_csv(tmp_path, rows), _make_registry(tmp_path))

    assert result.claim_status == "CLAIM_BLOCKED"


def test_pass_limited_when_rll_not_worse_than_cpl(tmp_path: Path) -> None:
    """When RLL AICc <= CPL AICc and BIC <= CPL BIC, claim_status is PASS_LIMITED."""
    rows = [
        {"model": "LCDM_joint", "chi2": "100", "AIC": "106", "AICc": "107", "BIC": "112",
         "N": "64", "k": "3", "dof": "61", "H0": "67", "Om": "0.31", "Os0": "", "zt": "", "wt": ""},
        {"model": "wCDM_joint", "chi2": "99", "AIC": "107", "AICc": "108", "BIC": "115",
         "N": "64", "k": "4", "dof": "60", "H0": "67.5", "Om": "0.31", "Os0": "", "zt": "", "wt": ""},
        {"model": "CPL_w0waCDM_joint", "chi2": "90", "AIC": "100", "AICc": "101", "BIC": "110",
         "N": "64", "k": "5", "dof": "59", "H0": "68", "Om": "0.30", "Os0": "", "zt": "", "wt": ""},
        # RLL better than CPL on both criteria
        {"model": "RLL_joint", "chi2": "89", "AIC": "101", "AICc": "100", "BIC": "109",
         "N": "64", "k": "6", "dof": "58", "H0": "67.2", "Om": "0.31", "Os0": "0.06", "zt": "1.2", "wt": "0.4"},
    ]
    result = scan(_make_csv(tmp_path, rows), _make_registry(tmp_path))

    assert result.claim_status == "PASS_LIMITED"


def test_claim_blocked_when_rll_absent(tmp_path: Path) -> None:
    """When no RLL row is present, claim_status is CLAIM_BLOCKED."""
    rows = [
        {"model": "LCDM_joint", "chi2": "100", "AIC": "106", "AICc": "107", "BIC": "112",
         "N": "64", "k": "3", "dof": "61", "H0": "67", "Om": "0.31", "Os0": "", "zt": "", "wt": ""},
        {"model": "CPL_w0waCDM_joint", "chi2": "90", "AIC": "100", "AICc": "101", "BIC": "110",
         "N": "64", "k": "5", "dof": "59", "H0": "68", "Om": "0.30", "Os0": "", "zt": "", "wt": ""},
    ]
    result = scan(_make_csv(tmp_path, rows), _make_registry(tmp_path))

    assert result.claim_status == "CLAIM_BLOCKED"
    assert any("RLL" in r for r in result.blocking_reasons)


def test_claim_blocked_when_cpl_absent(tmp_path: Path) -> None:
    """When no CPL row is present, claim_status is CLAIM_BLOCKED (no baseline for comparison)."""
    rows = [
        {"model": "LCDM_joint", "chi2": "100", "AIC": "106", "AICc": "107", "BIC": "112",
         "N": "64", "k": "3", "dof": "61", "H0": "67", "Om": "0.31", "Os0": "", "zt": "", "wt": ""},
        {"model": "RLL_joint", "chi2": "89", "AIC": "101", "AICc": "100", "BIC": "109",
         "N": "64", "k": "6", "dof": "58", "H0": "67.2", "Om": "0.31", "Os0": "0.06", "zt": "1.2", "wt": "0.4"},
    ]
    result = scan(_make_csv(tmp_path, rows), _make_registry(tmp_path))

    assert result.claim_status == "CLAIM_BLOCKED"
    assert any("CPL" in r or "baseline" in r.lower() for r in result.blocking_reasons)


# ---------------------------------------------------------------------------
# N-k-dof consistency
# ---------------------------------------------------------------------------

def test_dof_mismatch_is_flagged_and_blocks_claim(tmp_path: Path) -> None:
    """A row where N-k != dof should receive a local flag and block the claim."""
    rows = _base_rows()
    # Corrupt dof of CPL row
    rows[2]["dof"] = "55"  # should be 59
    result = scan(_make_csv(tmp_path, rows), _make_registry(tmp_path))

    assert result.claim_status == "CLAIM_BLOCKED"
    flagged = [ms for ms in result.model_scans if ms.dof_consistent is False]
    assert flagged, "Expected at least one row with dof_consistent=False"
    assert any("N-k-dof" in flag for ms in flagged for flag in ms.local_flags)


# ---------------------------------------------------------------------------
# Output structure
# ---------------------------------------------------------------------------

def test_scan_returns_all_expected_model_classes(tmp_path: Path) -> None:
    """Scan result lists all four required model classes when they are present."""
    rows = _base_rows()
    result = scan(_make_csv(tmp_path, rows), _make_registry(tmp_path))

    assert set(result.models_present) == {"LCDM", "wCDM", "CPL", "RLL"}


def test_scan_reports_missing_models(tmp_path: Path) -> None:
    """Missing required model classes are reported in missing_required_model_classes."""
    rows = [
        {"model": "LCDM_joint", "chi2": "100", "AIC": "106", "AICc": "107", "BIC": "112",
         "N": "64", "k": "3", "dof": "61", "H0": "67", "Om": "0.31", "Os0": "", "zt": "", "wt": ""},
    ]
    result = scan(_make_csv(tmp_path, rows), _make_registry(tmp_path))

    assert "RLL" in result.missing_required_model_classes
    assert "CPL" in result.missing_required_model_classes


def test_scan_best_by_aicc_and_bic_are_correct(tmp_path: Path) -> None:
    """best_by_AICc and best_by_BIC are the model with lowest respective values."""
    rows = _base_rows()
    result = scan(_make_csv(tmp_path, rows), _make_registry(tmp_path))

    # CPL has AICc=101 (lowest) and BIC=110 (lowest)
    assert result.best_by_AICc == "CPL_w0waCDM_joint"
    assert result.best_by_BIC == "CPL_w0waCDM_joint"


def test_scan_on_current_joint_real_likelihood(tmp_path: Path) -> None:
    """Smoke test: scan_rll_model_evidence can process the canonical results CSV without error."""
    root = Path(__file__).resolve().parents[1]
    results_csv = root / "results" / "structure_d" / "joint_real_likelihood.csv"
    registry = root / "data" / "inputs" / "cosmology_joint" / "parameter_origin_registry.json"

    if not results_csv.exists():
        pytest.skip("joint_real_likelihood.csv not available")

    result = scan(results_csv, registry)
    # Must produce a definite claim_status
    assert result.claim_status in {"CLAIM_BLOCKED", "PASS_LIMITED", "PARTIAL", "TOKEN_VAZIO", "AUDIT_FAIL"}
    # CPL should be the best model in the current table
    assert result.best_by_AICc is not None
    assert result.best_by_BIC is not None
