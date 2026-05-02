import math

from rll.desi_dha_extractor import run_dha_pipeline


def test_desi_dha_pipeline_detects_expected_omega_band():
    result = run_dha_pipeline(rng_seed=12345)
    expected = 2 * math.pi / math.log(1000)
    assert abs(result["best_omega"] - expected) < 0.2
    assert 0.0 <= result["fap"] <= 1.0
    assert abs(result["omega_fit"] - expected) < 0.2
