from __future__ import annotations

import json
import os
import subprocess
import sys
from pathlib import Path


def test_preflight_real_json_missing_files_exits_2() -> None:
    env = os.environ.copy()
    env["PYTHONPATH"] = str(Path.cwd() / "src")
    completed = subprocess.run(
        [sys.executable, "-m", "rll.cli", "preflight-real", "--json"],
        capture_output=True,
        text=True,
        check=False,
        env=env,
    )
    assert completed.returncode == 2
    payload = json.loads(completed.stdout)
    assert payload["check"] == "preflight-real"
    assert payload["passed"] is False
    assert len(payload["missing"]) >= 1


def test_preflight_real_plain_missing_files_exits_2() -> None:
    env = os.environ.copy()
    env["PYTHONPATH"] = str(Path.cwd() / "src")
    completed = subprocess.run(
        [sys.executable, "-m", "rll.cli", "preflight-real"],
        capture_output=True,
        text=True,
        check=False,
        env=env,
    )
    assert completed.returncode == 2
    assert "Preflight real-data validation" in completed.stdout
    assert "MISSING" in completed.stdout
