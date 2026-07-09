from __future__ import annotations

import importlib.util
from pathlib import Path

import pytest

MODULE_PATH = Path(__file__).resolve().parents[1] / "scripts" / "import_raw_json_dataset.py"
SPEC = importlib.util.spec_from_file_location("import_raw_json_dataset", MODULE_PATH)
assert SPEC is not None and SPEC.loader is not None
importer = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(importer)


def test_invalid_json_blocks_write(tmp_path: Path) -> None:
    source = tmp_path / "bad.json"
    source.write_text("{bad json", encoding="utf-8")
    out = tmp_path / "out"

    with pytest.raises(SystemExit, match="invalid JSON input"):
        importer.import_json(source, out, "bad")

    assert not (out / "bad.raw.json").exists()
    assert not (out / "bad.MANIFEST.json").exists()
