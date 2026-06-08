import json
from pathlib import Path

import rll_vs_lcdm


def test_default_bao_input_is_desi_dr2_primary_not_legacy():
    args = rll_vs_lcdm.build_arg_parser().parse_args([])

    assert args.bao == rll_vs_lcdm.DEFAULT_BAO_PATH
    assert args.bao != rll_vs_lcdm.LEGACY_BAO_PATH
    assert len(rll_vs_lcdm.load_bao(Path(args.bao), bao_format=args.bao_format)) == 13


def test_desi_dr2_primary_bao_loader_reads_observable_metadata():
    points = rll_vs_lcdm.load_bao(Path(rll_vs_lcdm.DEFAULT_BAO_PATH), bao_format="desi_dr2_primary")

    assert len(points) == 13
    assert {p.observable for p in points} == {"DV_over_rd", "DM_over_rd", "DH_over_rd"}
    assert {p.release for p in points} == {"desi_dr2_bao_2025"}
    assert {p.tracer for p in points} >= {"BGS", "LRG1", "Lya"}


def test_legacy_bao_loader_remains_optional_and_uses_ten_dv_points():
    points = rll_vs_lcdm.load_bao(Path(rll_vs_lcdm.LEGACY_BAO_PATH), bao_format="legacy_dv")

    assert len(points) == 10
    assert {p.observable for p in points} == {"DV_over_rd"}
    assert {p.release for p in points} == {"legacy_dv"}


def test_default_main_run_reports_thirteen_bao_and_covariance_blocks(tmp_path):
    out_json = tmp_path / "summary.json"
    out_csv = tmp_path / "predictions.csv"

    rll_vs_lcdm.main(["--out-json", str(out_json), "--out-csv", str(out_csv)])

    summary = json.loads(out_json.read_text(encoding="utf-8"))
    assert summary["input"]["n_bao"] == 13
    assert summary["input"]["n_total"] == 46
    assert summary["bao_covariance"]["mode"] == "block_covariance_summary"
    assert summary["bao_covariance"]["n_correlated_blocks"] == 6
    assert not summary["bao_covariance"]["missing_covariance_blocks"]
