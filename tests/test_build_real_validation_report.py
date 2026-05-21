from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


def test_build_real_validation_report_generates_outputs(tmp_path: Path) -> None:
    input_json = tmp_path / "model_comparison.json"
    input_json.write_text(
        json.dumps(
            {
                "n_obs": 10,
                "rll": {"chi2": 12.0, "AIC": 22.0, "BIC": 24.0},
                "lcdm": {"chi2": 13.0, "AIC": 17.0, "BIC": 18.0},
            }
        ),
        encoding="utf-8",
    )

    out_json = tmp_path / "real_validation_report.json"
    out_table = tmp_path / "model_comparison_table.md"

    completed = subprocess.run(
        [
            sys.executable,
            "scripts/build_real_validation_report.py",
            "--input-json",
            str(input_json),
            "--out-json",
            str(out_json),
            "--out-table",
            str(out_table),
        ],
        check=False,
        capture_output=True,
        text=True,
    )

    assert completed.returncode == 0, completed.stderr
    payload = json.loads(out_json.read_text(encoding="utf-8"))
    assert payload["rll"]["chi2"] == 12.0
    assert payload["lcdm"]["n_params"] == 2
    assert "| RLL |" in out_table.read_text(encoding="utf-8")
