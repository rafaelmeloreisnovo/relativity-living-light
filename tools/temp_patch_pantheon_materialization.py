#!/usr/bin/env python3
from pathlib import Path

runtime = Path("tools/rll_pipeline_fase24_1_runtime.py")
tests = Path("tests/test_rll_pipeline_fase24_1_runtime.py")
s = runtime.read_text(encoding="utf-8")
old = '''    _replace_step(13, commands=(command(\n        "bash", "-lc",\n        f"mkdir -p artifacts/linear/current_run && "\n        f"PYTHONPATH=products/rll-evidence-runner/src {py} -m rll_evidence.pantheon_fit_ascii "\n        "--catalog data/real/cosmology/pantheon_plus/Pantheon+_Data/4_DISTANCES_AND_COVAR/Pantheon+SH0ES.dat "\n        "--covariance data/real/cosmology/pantheon_plus/Pantheon+_Data/4_DISTANCES_AND_COVAR/Pantheon+SH0ES_STAT+SYS.cov "\n        "--output artifacts/linear/current_run/pantheon_fit_result.json "\n        "--seeds 11,23,37,53,71 --maxiter 250 --integration-points 4096 --z-min 0.01",\n        requires=(\n            "products/rll-evidence-runner/src/rll_evidence/pantheon_fit_ascii.py",\n            "data/real/cosmology/pantheon_plus/Pantheon+_Data/4_DISTANCES_AND_COVAR/Pantheon+SH0ES.dat",\n            "data/real/cosmology/pantheon_plus/Pantheon+_Data/4_DISTANCES_AND_COVAR/Pantheon+SH0ES_STAT+SYS.cov",\n            "data/real/cosmology/pantheon_plus/Pantheon+_Data/4_DISTANCES_AND_COVAR/Pantheon+SH0ES_STAT+SYS.cov.sha256",\n        ),\n    ),), candidates=())'''
new = '''    _replace_step(13, commands=(command(\n        "bash", "-lc",\n        f"mkdir -p artifacts/linear/current_run && "\n        f"{py} scripts/fetch_pantheon_covariance.py "\n        "--output-dir data/real/cosmology/pantheon_plus/Pantheon+_Data/4_DISTANCES_AND_COVAR "\n        "--receipt artifacts/linear/current_run/pantheon_covariance_materialization.json && "\n        f"PYTHONPATH=products/rll-evidence-runner/src {py} -m rll_evidence.pantheon_fit_ascii "\n        "--catalog data/real/cosmology/pantheon_plus/Pantheon+_Data/4_DISTANCES_AND_COVAR/Pantheon+SH0ES.dat "\n        "--covariance data/real/cosmology/pantheon_plus/Pantheon+_Data/4_DISTANCES_AND_COVAR/Pantheon+SH0ES_STAT+SYS.cov "\n        "--output artifacts/linear/current_run/pantheon_fit_result.json "\n        "--seeds 11,23,37,53,71 --maxiter 250 --integration-points 4096 --z-min 0.01",\n        requires=(\n            "scripts/fetch_pantheon_covariance.py",\n            "products/rll-evidence-runner/src/rll_evidence/pantheon_fit_ascii.py",\n            "data/real/cosmology/pantheon_plus/Pantheon+_Data/4_DISTANCES_AND_COVAR/Pantheon+SH0ES.dat",\n        ),\n    ),), candidates=())'''
if old not in s:
    raise SystemExit("current Pantheon step block not found")
runtime.write_text(s.replace(old, new), encoding="utf-8")

t = tests.read_text(encoding="utf-8")
t = t.replace(
    '    assert "rll_evidence.pantheon_fit_ascii" in joined\n    assert "Pantheon+SH0ES_STAT+SYS.cov" in joined\n    assert "scripts/pantheon/models.py" not in spec.requires\n    assert "pantheon_fit_result.json" in joined\n',
    '    assert "scripts/fetch_pantheon_covariance.py" in joined\n    assert "rll_evidence.pantheon_fit_ascii" in joined\n    assert "Pantheon+SH0ES_STAT+SYS.cov" in joined\n    assert "scripts/pantheon/models.py" not in spec.requires\n    assert not any(path.endswith("Pantheon+SH0ES_STAT+SYS.cov") for path in spec.requires)\n    assert "pantheon_covariance_materialization.json" in joined\n    assert "pantheon_fit_result.json" in joined\n'
)
tests.write_text(t, encoding="utf-8")
print("Pantheon materialization patch applied")
