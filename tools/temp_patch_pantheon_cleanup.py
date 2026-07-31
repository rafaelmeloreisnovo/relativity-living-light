#!/usr/bin/env python3
from pathlib import Path

runtime = Path("tools/rll_pipeline_fase24_1_runtime.py")
tests = Path("tests/test_rll_pipeline_fase24_1_runtime.py")
s = runtime.read_text(encoding="utf-8")
old = '''        f"mkdir -p artifacts/linear/current_run && "
        f"{py} scripts/fetch_pantheon_covariance.py "'''
new = '''        "COV_DIR=data/real/cosmology/pantheon_plus/Pantheon+_Data/4_DISTANCES_AND_COVAR; "
        "COV_FILE=\\\"$COV_DIR/Pantheon+SH0ES_STAT+SYS.cov\\\"; "
        "COV_SHA=\\\"$COV_FILE.sha256\\\"; "
        "cleanup_pantheon_covariance() { rm -f \\\"$COV_FILE\\\" \\\"$COV_SHA\\\"; }; "
        "trap cleanup_pantheon_covariance EXIT; "
        f"mkdir -p artifacts/linear/current_run && "
        f"{py} scripts/fetch_pantheon_covariance.py "'''
if old not in s:
    raise SystemExit("Pantheon command prefix not found")
s = s.replace(old, new, 1)
runtime.write_text(s, encoding="utf-8")

t = tests.read_text(encoding="utf-8")
old_assert = '''    assert "pantheon_covariance_materialization.json" in joined
    assert "pantheon_fit_result.json" in joined
'''
new_assert = '''    assert "pantheon_covariance_materialization.json" in joined
    assert "pantheon_fit_result.json" in joined
    assert "trap cleanup_pantheon_covariance EXIT" in joined
    assert 'rm -f "$COV_FILE" "$COV_SHA"' in joined
'''
if old_assert not in t:
    raise SystemExit("Pantheon test assertion block not found")
t = t.replace(old_assert, new_assert, 1)
tests.write_text(t, encoding="utf-8")
print("Pantheon ephemeral cleanup patch applied")
