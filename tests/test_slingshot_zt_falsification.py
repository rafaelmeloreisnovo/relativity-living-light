from __future__ import annotations

import json
from argparse import Namespace
from pathlib import Path

import yaml

from scripts import slingshot_zt_falsification as scan


def test_protocol_is_claim_blocked_and_has_required_scan_fields() -> None:
    protocol = yaml.safe_load(Path("protocols/05_slingshot_zt_falsification.yml").read_text(encoding="utf-8"))

    assert protocol["module"] == "slingshot_zt_falsification"
    assert protocol["claim_policy"]["claim_allowed"] is False
    assert protocol["scan_zt"]["zt_range"] == [0.3, 0.5, 0.7, 0.9, 1.0, 1.2, 1.5, 1.8, 2.0]
    assert {item["id"] for item in protocol["falsifiers"]} == {"F_ZT_01", "F_ZT_02", "F_ZT_03"}


def test_run_scan_materializes_csv_json_and_falsifier_statuses(tmp_path: Path) -> None:
    args = Namespace(bao=None, hz=None, h0=None, omega_m=None, omega_s0=None, wt=None)
    summary = scan.run_scan(Path("protocols/05_slingshot_zt_falsification.yml"), tmp_path, args)

    assert (tmp_path / "zt_scan.csv").exists()
    assert (tmp_path / "summary.json").exists()
    assert (tmp_path / "zt_0.3.json").exists()
    assert len(summary["scan"]) == 9
    assert summary["assessment"]["claim_allowed"] is False
    assert set(summary["assessment"]["falsifiers"]) == {"F_ZT_01", "F_ZT_02", "F_ZT_03"}
    persisted = json.loads((tmp_path / "summary.json").read_text(encoding="utf-8"))
    assert persisted["assessment"]["best"]["zt_bao"] in [row["zt"] for row in persisted["scan"]]
