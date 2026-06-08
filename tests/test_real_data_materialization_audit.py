from __future__ import annotations

from pathlib import Path

import pandas as pd

from tools import real_data_materialization_audit as audit


def test_audit_maps_configured_synthetic_growth_to_real_file() -> None:
    rows = audit.build_rows()
    by_dataset = {row["dataset_id"]: row for row in rows if row["record_type"] == "configured_dataset"}

    assert by_dataset["fsigma8"]["real_replacement_id"] == "real_fsigma8"
    assert by_dataset["fsigma8"]["real_exists"] is True
    assert by_dataset["fsigma8"]["status"] == "real_replacement_ready"
    assert by_dataset["hz"]["real_replacement_id"] == "real_hz"


def test_real_fsigma8_file_is_not_smooth_synthetic_fixture() -> None:
    real_path = Path("data/real/cosmology/fsigma8_growth_real.csv")
    synthetic_path = Path("data/inputs/structure_d/fsigma8.csv")

    real_df = pd.read_csv(real_path)
    synthetic_df = pd.read_csv(synthetic_path)

    assert len(real_df) > len(synthetic_df)
    assert {"z", "fs8", "sigma", "survey", "reference", "source_url"}.issubset(real_df.columns)
    assert real_df["source_url"].str.startswith("https://").all()
    assert not real_df[["z", "fs8", "sigma"]].reset_index(drop=True).equals(
        synthetic_df[["z", "fs8", "sigma"]].reset_index(drop=True)
    )


def test_audit_outputs_are_atomic_and_include_rollback_metadata(tmp_path, monkeypatch) -> None:
    monkeypatch.setattr(audit, "RESULTS_DIR", tmp_path)
    monkeypatch.setattr(audit, "CSV_OUT", tmp_path / "audit.csv")
    monkeypatch.setattr(audit, "JSON_OUT", tmp_path / "audit.json")
    monkeypatch.setattr(audit, "MD_OUT", tmp_path / "audit.md")

    first = audit.run_audit()
    second = audit.run_audit()

    assert len(first["outputs"]) == 3
    assert all((tmp_path / name).exists() for name in ["audit.csv", "audit.json", "audit.md"])
    assert all(output["rollback_available"] is True for output in second["outputs"])
