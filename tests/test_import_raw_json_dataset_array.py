from __future__ import annotations

import importlib.util
from pathlib import Path

MODULE_PATH = Path(__file__).resolve().parents[1] / "scripts" / "import_raw_json_dataset.py"
SPEC = importlib.util.spec_from_file_location("import_raw_json_dataset", MODULE_PATH)
assert SPEC is not None and SPEC.loader is not None
importer = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(importer)


def test_array_json_autodetects_row_count(tmp_path: Path) -> None:
    source = tmp_path / "rows.json"
    source.write_text('[{"z": 1}, {"z": 2}]', encoding="utf-8")
    manifest = importer.import_json(source, tmp_path / "out", "rows")
    assert manifest["autodetected_shape"]["json_type"] == "array"
    assert manifest["autodetected_shape"]["row_count"] == 2
