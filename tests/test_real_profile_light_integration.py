import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import json
import os
from tempfile import TemporaryDirectory
from unittest import mock

import pandas as pd

from data.pipelines.structure_d import run_all, run_all_real


def _write_minimal_real_fixture(base_dir: Path) -> Path:
    data_dir = base_dir / "fixture_data"
    data_dir.mkdir(parents=True, exist_ok=True)

    hz_path = data_dir / "Hz_data_real_small.csv"
    hz_path.write_text(
        "z,H_obs,sigma_H,source\n"
        "0.1,69.0,2.0,fixture\n"
        "0.5,88.0,3.0,fixture\n",
        encoding="utf-8",
    )

    bao_path = data_dir / "BAO_data_real_small.csv"
    bao_path.write_text(
        "z_eff,DV_over_rs,sigma,survey\n"
        "0.2,8.0,0.5,fixture\n"
        "0.6,13.0,0.7,fixture\n",
        encoding="utf-8",
    )

    cmb_path = data_dir / "CMB_shift_real_small.json"
    cmb_path.write_text(
        json.dumps(
            {
                "R_obs": 1.75,
                "la_obs": 301.0,
                "R_sig": 0.03,
                "la_sig": 0.35,
            }
        ),
        encoding="utf-8",
    )

    cfg = {
        "default_profile": "structure_d_real_validation",
        "validation": {
            "min_points_with_z": 2,
        },
        "profiles": {
            "structure_d_real_validation": {
                "run_name": "real_min_fixture",
                "active_datasets": ["real_hz", "real_bao", "real_cmb_shift"],
            }
        },
        "datasets": {
            "real_hz": {
                "format": "csv",
                "path": str(hz_path),
                "observable": "Hz",
                "error_model": "errors",
                "columns": {"z": "z", "value": "H_obs", "error": "sigma_H"},
                "metadata": {
                    "survey": "fixture",
                    "redshift_range": "[0.1, 0.5]",
                    "reference": "integration-test",
                },
            },
            "real_bao": {
                "format": "csv",
                "path": str(bao_path),
                "observable": "DV_over_rs",
                "error_model": "errors",
                "columns": {"z": "z_eff", "value": "DV_over_rs", "error": "sigma"},
                "metadata": {
                    "survey": "fixture",
                    "redshift_range": "[0.2, 0.6]",
                    "reference": "integration-test",
                },
            },
            "real_cmb_shift": {
                "format": "json_scalars",
                "path": str(cmb_path),
                "observable": "CMB_shift",
                "error_model": "errors",
                "keys": {"values": ["R_obs", "la_obs"], "errors": ["R_sig", "la_sig"]},
                "metadata": {
                    "survey": "fixture",
                    "redshift_range": "z=1089.92",
                    "reference": "integration-test",
                },
            },
        },
    }

    cfg_path = base_dir / "datasets_config_min_real.json"
    cfg_path.write_text(json.dumps(cfg), encoding="utf-8")
    return cfg_path


def test_real_profile_light_integration_generates_outputs_with_expected_schema():
    with TemporaryDirectory() as tmp_dir:
        tmp_path = Path(tmp_dir)
        cfg_path = _write_minimal_real_fixture(tmp_path)
        results_dir = tmp_path / "results"

        with (
            mock.patch.object(run_all, "RESULTS", str(results_dir)),
            mock.patch.object(run_all_real, "RESULTS", str(results_dir)),
            mock.patch.dict(os.environ, {"STRUCTURE_D_MAXITER_LCDM": "1", "STRUCTURE_D_MAXITER_RLL": "1"}),
        ):
            run_all.main(config_path=str(cfg_path), profile_name="structure_d_real_validation")

        required = [
            "model_comparison.csv",
            "covariance_usage.csv",
            "rll_regime_summary.csv",
            "reproduction_contract.json",
        ]
        for filename in required:
            assert (results_dir / filename).exists(), f"missing output: {filename}"

        for filename, expected_header in run_all.EXPECTED_SCHEMA_BY_OUTPUT.items():
            actual_header = list(pd.read_csv(results_dir / filename, nrows=0).columns)
            assert actual_header == expected_header, f"schema mismatch in {filename}"

        df_model = pd.read_csv(results_dir / "model_comparison.csv")
        assert set(df_model["model"]) == {"LCDM", "RLL_like+AGN"}
        assert set(df_model["profile_name"]) == {"structure_d_real_validation"}
        assert set(df_model["run_name"]) == {"real_min_fixture"}
