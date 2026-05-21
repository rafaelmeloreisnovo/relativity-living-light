from __future__ import annotations

import json
from pathlib import Path

import pandas as pd

from data.pipelines.structure_d import run_all


def test_partial_real_profile_exists_in_config() -> None:
    config_path = Path("data/pipelines/structure_d/datasets_config.json")
    cfg = json.loads(config_path.read_text(encoding="utf-8"))
    profiles = cfg.get("profiles", {})
    assert "structure_d_partial_real" in profiles
    assert profiles["structure_d_partial_real"]["active_datasets"] == ["real_hz", "real_bao"]


def test_partial_real_run_marks_regime_and_dof() -> None:
    result = run_all.main(profile_name="structure_d_partial_real")
    model_path = Path(result["output_paths"]["model_comparison"])
    df = pd.read_csv(model_path)
    assert "dof" in df.columns
    assert set(df["regime"].unique()) == {"partial_real"}

