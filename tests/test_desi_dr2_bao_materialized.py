import csv
from pathlib import Path


POINTS = Path("data/real/cosmology/desi_dr2_bao_primary_points.csv")
COVARIANCE = Path("data/real/cosmology/desi_dr2_bao_covariance_summary.csv")


def test_desi_dr2_primary_points_contract():
    rows = list(csv.DictReader(POINTS.open(newline="", encoding="utf-8")))

    assert len(rows) == 13
    assert {row["release"] for row in rows} == {"desi_dr2_bao_2025"}
    assert {row["primary_likelihood"] for row in rows} == {"true"}
    assert min(float(row["z_eff"]) for row in rows) == 0.295
    assert max(float(row["z_eff"]) for row in rows) == 2.330
    assert {row["observable"] for row in rows} == {"DV_over_rd", "DM_over_rd", "DH_over_rd"}

    bgs = [row for row in rows if row["tracer"] == "BGS"]
    assert bgs == [
        {
            **bgs[0],
            "observable": "DV_over_rd",
            "value": "7.942",
            "sigma": "0.075",
        }
    ]


def test_desi_dr2_covariance_summary_contract():
    blocks = list(csv.DictReader(COVARIANCE.open(newline="", encoding="utf-8")))

    assert len(blocks) == 6
    assert {block["observable_a"] for block in blocks} == {"DM_over_rd"}
    assert {block["observable_b"] for block in blocks} == {"DH_over_rd"}
    assert all(float(block["correlation_coefficient"]) < 0 for block in blocks)
    assert all(float(block["covariance"]) < 0 for block in blocks)
