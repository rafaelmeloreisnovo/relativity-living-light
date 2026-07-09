from __future__ import annotations

import importlib.util
import json
from pathlib import Path

MODULE_PATH = Path(__file__).resolve().parents[1] / "scripts" / "import_raw_json_dataset.py"
SPEC = importlib.util.spec_from_file_location("import_raw_json_dataset", MODULE_PATH)
assert SPEC is not None and SPEC.loader is not None
importer = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(importer)


def test_reimport_keeps_rollback_backup(tmp_path: Path) -> None:
    source = tmp_path / "data.json"
    out = tmp_path / "out"
    source.write_text(json.dumps({"version": 1}), encoding="utf-8")
    importer.import_json(source, out, "stable")
    source.write_text(json.dumps({"version": 2}), encoding="utf-8")
    manifest = importer.import_json(source, out, "stable")
    assert manifest["failsafe"]["rollback_available"] is True
    backup = Path(manifest["failsafe"]["backup_path"])
    assert json.loads(backup.read_text(encoding="utf-8"))["version"] == 1
