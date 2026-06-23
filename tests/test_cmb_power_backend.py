from __future__ import annotations

import argparse
import importlib.util
import sys
from pathlib import Path


def load_module():
    path = Path(__file__).resolve().parents[1] / "scripts" / "run_cmb_power_backend.py"
    spec = importlib.util.spec_from_file_location("cmb_backend_under_test", path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def test_rll_stock_backend_is_marked_not_exact():
    m = load_module()
    args = argparse.Namespace(model="rll")
    result = m.try_classy(args)
    if result.get("available"):
        assert result["status"] == "TOKEN_VAZIO"
    else:
        assert result["available"] is False


def test_parser_defaults_to_lcdm_auto():
    m = load_module()
    parser = m.build_parser()
    args = parser.parse_args([])
    assert args.engine == "auto"
    assert args.model == "lcdm"
    assert args.lmax == 2500
