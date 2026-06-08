from __future__ import annotations

import csv
import importlib.util
import json
from pathlib import Path

import pandas as pd
import pytest


MODULE_PATH = Path(__file__).resolve().parents[1] / "scripts" / "compute_rll_real_pipeline.py"
SPEC = importlib.util.spec_from_file_location("compute_rll_real_pipeline", MODULE_PATH)
assert SPEC is not None and SPEC.loader is not None
compute = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(compute)


def _write_minimal_real_inputs(base: Path, hz_source: str = "repo") -> None:
    base.mkdir(parents=True, exist_ok=True)
    with (base / "Hz_data_real.csv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=["z", "H_obs", "sigma_H", "source"])
        writer.writeheader()
        writer.writerow({"z": "0.1", "H_obs": "72.0", "sigma_H": "2.0", "source": hz_source})
    with (base / "BAO_data_real.csv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=["z_eff", "DV_over_rs", "sigma", "survey"])
        writer.writeheader()
        writer.writerow({"z_eff": "0.3", "DV_over_rs": "8.0", "sigma": "0.2", "survey": "fixture"})
    (base / "CMB_shift_real.json").write_text(
        json.dumps({"survey": "fixture", "reference": "unit-test"}),
        encoding="utf-8",
    )


def test_resolve_inputs_auto_prefers_materialized_over_repo(tmp_path: Path) -> None:
    raw = tmp_path / "run" / "raw"
    materialized = raw / "cosmology_curated"
    repo = tmp_path / "data" / "real"
    _write_minimal_real_inputs(repo, hz_source="repo")
    _write_minimal_real_inputs(materialized, hz_source="materialized")

    resolved = compute.resolve_inputs(raw, repo, "auto")

    assert resolved["Hz_data_real.csv"] == materialized / "Hz_data_real.csv"
    hz = pd.read_csv(resolved["Hz_data_real.csv"])
    assert hz.loc[0, "source"] == "materialized"


def test_resolve_inputs_repo_mode_does_not_fall_back_to_materialized(tmp_path: Path) -> None:
    raw = tmp_path / "run" / "raw"
    materialized = raw / "cosmology_curated"
    repo = tmp_path / "data" / "real"
    _write_minimal_real_inputs(materialized, hz_source="materialized")

    with pytest.raises(FileNotFoundError, match="Hz_data_real.csv"):
        compute.resolve_inputs(raw, repo, "repo")


def test_main_writes_manifest_and_tables_from_repo_inputs(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    repo = tmp_path / "data" / "real"
    out = tmp_path / "artifacts" / "real-data-contract"
    _write_minimal_real_inputs(repo)

    monkeypatch.setattr(
        "sys.argv",
        [
            "compute_rll_real_pipeline.py",
            "--output-dir",
            str(out),
            "--real-data-dir",
            str(repo),
            "--data-source",
            "repo",
        ],
    )

    assert compute.main() == 0
    manifest = json.loads((out / "MANIFEST.json").read_text(encoding="utf-8"))
    assert manifest["data_source_mode"] == "repo"
    assert manifest["status"] == "Real data computed from non-synthetic inputs"
    assert {row["status"] for row in manifest["input_files"]} == {"used_real_non_synthetic"}
    assert manifest["validation_status"]["claim_boundary"] == "local dynamic layer cannot be promoted to background cosmology without scale bridge"
    assert "Phi_pre" in manifest["validation_status"]["local_dynamic_layer"]
    assert (out / "tables" / "Hz_processed.csv").exists()
    assert (out / "tables" / "BAO_processed.csv").exists()
    assert (out / "tables" / "model_comparison.csv").exists()


def test_validation_status_payload_separates_background_growth_and_local_dynamic_layers() -> None:
    status = compute.validation_status_payload()

    assert "Omega_b_h2" in status["background_parameters"]
    assert "fsigma8" in status["growth_parameters"]
    assert "delta_m" in status["growth_parameters"]
    assert "Phi_pre" in status["local_dynamic_layer"]
    assert "G_pre" in status["local_dynamic_layer"]
    assert "neighbouring_orbital_ellipses" in status["local_dynamic_layer"]
    assert "binary_stars_or_black_holes_with_converging_vector_motion" in status["scale_bridge_examples"]
    assert "apollo_lunar_impact_dynamic_memory_without_cosmological_promotion" in status["scale_bridge_examples"]
    assert "non-operational until dimensions" in status["symbolic_complexity_marker"]
    assert status["claim_boundary"] == "local dynamic layer cannot be promoted to background cosmology without scale bridge"
