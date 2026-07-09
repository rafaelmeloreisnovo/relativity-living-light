#!/usr/bin/env python3
"""
tools/promote_orphan.py
Promove um artefato órfão para a trilha canônica do repositório.

Operações:
  1. Lê o arquivo órfão
  2. Valida que existe e tem conteúdo
  3. Determina o próximo número canônico disponível
  4. Move/copia para docs/canonicos/ com nome sequencial
  5. Atualiza estado epistêmico (TOKEN_VAZIO → DECLARED_BY_AUTHOR ou VERIFIED)
  6. Emite evento ORPHAN_PROMOTED na trilha EVOLUTION_TRAIL.jsonl
  7. Atualiza results/manifest.json
  8. Remove da lista de órfãos no YAML (opcional, --update-config)

Uso:
  python tools/promote_orphan.py --file "Rafael te.md" --epistemic DECLARED_BY_AUTHOR
  python tools/promote_orphan.py --file "temp.md" --epistemic VERIFIED --update-config
  python tools/promote_orphan.py --list-orphans
"""

import argparse
import json
import re
import shutil
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Optional

import yaml

# ---------------------------------------------------------------------------
CONFIG_PATH = Path("RLL_JSON_EVOLUTION_WATCHER.yml")
TRAIL_LOG   = Path("artifacts/EVOLUTION_TRAIL.jsonl")
MANIFEST    = Path("results/manifest.json")
CANONICAL   = Path("docs/canonicos")

VALID_EPISTEMIC = ["VERIFIED", "DECLARED_BY_AUTHOR", "TOKEN_VAZIO", "CONTRADICTION"]


# ---------------------------------------------------------------------------
def load_config() -> Dict:
    with open(CONFIG_PATH, encoding="utf-8") as f:
        return yaml.safe_load(f)


def load_manifest() -> Dict:
    if MANIFEST.exists():
        try:
            return json.loads(MANIFEST.read_text(encoding="utf-8"))
        except Exception:
            pass
    return {"version": "1.0", "artifacts": {}, "generated_utc": ""}


def save_manifest(m: Dict) -> None:
    m["generated_utc"] = datetime.now(timezone.utc).isoformat()
    MANIFEST.parent.mkdir(parents=True, exist_ok=True)
    MANIFEST.write_text(json.dumps(m, indent=2, ensure_ascii=False), encoding="utf-8")


def emit_event(event: Dict) -> None:
    TRAIL_LOG.parent.mkdir(parents=True, exist_ok=True)
    with open(TRAIL_LOG, "a", encoding="utf-8") as f:
        f.write(json.dumps(event, ensure_ascii=False) + "\n")


# ---------------------------------------------------------------------------
def list_orphans(cfg: Dict) -> List[Dict]:
    trail_cfg = cfg.get("artifact_evolution_trail", {})
    return trail_cfg.get("registered_orphan_artifacts", [])


def find_orphan(cfg: Dict, file_path: str) -> Optional[Dict]:
    for o in list_orphans(cfg):
        if Path(o["path"]) == Path(file_path):
            return o
    return None


def next_canonical_number() -> int:
    CANONICAL.mkdir(parents=True, exist_ok=True)
    existing = list(CANONICAL.glob("*.md")) + list(CANONICAL.glob("*.txt"))
    nums = []
    for f in existing:
        m = re.match(r"^(\d+)", f.name)
        if m:
            nums.append(int(m.group(1)))
    return (max(nums) + 1) if nums else 1


def canonical_filename(n: int, original: str) -> str:
    stem = Path(original).stem
    ext  = Path(original).suffix or ".md"
    safe = re.sub(r"[^a-zA-Z0-9_]", "_", stem).strip("_")
    return f"{n:02d}_{safe}{ext}"


# ---------------------------------------------------------------------------
def promote(file_path: str, epistemic: str,
            note: str = "", update_config: bool = False,
            dry_run: bool = False) -> None:

    src = Path(file_path)
    if not src.exists():
        print(f"[ERROR] file not found: {src}")
        return

    cfg     = load_config()
    orphan  = find_orphan(cfg, file_path)
    ep_before = (orphan.get("epistemic", "TOKEN_VAZIO")
                 if orphan else "TOKEN_VAZIO")

    if epistemic not in VALID_EPISTEMIC:
        print(f"[ERROR] invalid epistemic state: {epistemic}")
        print(f"  valid: {VALID_EPISTEMIC}")
        return

    # Próximo número canônico
    n      = next_canonical_number()
    dest_name = canonical_filename(n, file_path)
    dest   = CANONICAL / dest_name

    print(f"\n=== ORPHAN PROMOTION ===")
    print(f"  source      : {src}")
    print(f"  destination : {dest}")
    print(f"  epistemic   : {ep_before} → {epistemic}")
    print(f"  dry_run     : {dry_run}")

    if dry_run:
        print("\n[DRY-RUN] no files modified")
        return

    # Criar diretório e copiar
    CANONICAL.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dest)
    print(f"\n  [OK] copied to: {dest}")

    ts = datetime.now(timezone.utc).isoformat()

    # Emitir evento na trilha
    event = {
        "timestamp_utc":      ts,
        "source_id":          f"orphan:{file_path}",
        "action":             "ORPHAN_PROMOTED",
        "schema_drift":       False,
        "epistemic_before":   ep_before,
        "epistemic_after":    epistemic,
        "fingerprint_before": "",
        "fingerprint_after":  "",
        "artifact_path":      str(dest),
        "rll_paths_affected": [],
        "notes": (f"promoted to canonical #{n}: {dest_name}. {note}").strip(),
    }
    emit_event(event)
    print(f"  [OK] event emitted to trail: {TRAIL_LOG}")

    # Atualizar manifest
    manifest = load_manifest()
    manifest["artifacts"][f"canonical:{dest_name}"] = {
        "last_updated":  ts,
        "action":        "ORPHAN_PROMOTED",
        "epistemic":     epistemic,
        "schema_drift":  False,
        "artifact_path": str(dest),
        "promoted_from": str(src),
    }
    save_manifest(manifest)
    print(f"  [OK] manifest updated: {MANIFEST}")

    # Remover do YAML de órfãos (opcional)
    if update_config:
        _remove_from_orphans(cfg, file_path)
        print(f"  [OK] removed from orphan registry in {CONFIG_PATH}")

    print(f"\n  DONE: {src} → {dest} [{epistemic}]")


def _remove_from_orphans(cfg: Dict, file_path: str) -> None:
    """Remove o artefato da lista de órfãos e regrava o YAML."""
    trail_cfg = cfg.get("artifact_evolution_trail", {})
    orphans   = trail_cfg.get("registered_orphan_artifacts", [])
    updated   = [o for o in orphans if Path(o["path"]) != Path(file_path)]
    trail_cfg["registered_orphan_artifacts"] = updated
    cfg["artifact_evolution_trail"] = trail_cfg

    with open(CONFIG_PATH, "w", encoding="utf-8") as f:
        yaml.dump(cfg, f, allow_unicode=True,
                  default_flow_style=False, sort_keys=False)


# ---------------------------------------------------------------------------
def cmd_list(cfg: Dict) -> None:
    orphans = list_orphans(cfg)
    if not orphans:
        print("No orphan artifacts registered.")
        return

    print(f"\n=== ORPHAN ARTIFACTS ({len(orphans)}) ===\n")
    for o in orphans:
        p      = Path(o["path"])
        exists = "✓" if p.exists() else "✗"
        print(f"  [{exists}] {o['path']}")
        print(f"       epistemic : {o.get('epistemic','?')}")
        print(f"       status    : {o.get('status','?')}")
        if o.get("promote_to"):
            print(f"       promote → : {o['promote_to']}")
        if o.get("condition"):
            print(f"       condition : {o['condition']}")
        if o.get("action"):
            print(f"       action    : {o['action']}")
        print()


# ---------------------------------------------------------------------------
def main():
    parser = argparse.ArgumentParser(
        description="Promote orphan artifact to canonical track")
    sub = parser.add_subparsers(dest="cmd")

    # promote
    p_promote = sub.add_parser("promote", help="Promote a specific orphan")
    p_promote.add_argument("--file",      required=True, help="Path of orphan file")
    p_promote.add_argument("--epistemic", required=True,
                           choices=VALID_EPISTEMIC)
    p_promote.add_argument("--note",      default="", help="Free-text note")
    p_promote.add_argument("--update-config", action="store_true",
                           help="Remove from YAML orphan registry after promotion")
    p_promote.add_argument("--dry-run",   action="store_true")

    # list
    sub.add_parser("list", help="List all registered orphans")

    # Compat: flags diretos (sem subcomando)
    parser.add_argument("--file",      default=None)
    parser.add_argument("--epistemic", default=None, choices=VALID_EPISTEMIC)
    parser.add_argument("--note",      default="")
    parser.add_argument("--update-config", action="store_true")
    parser.add_argument("--dry-run",   action="store_true")
    parser.add_argument("--list-orphans", action="store_true")

    args = parser.parse_args()
    cfg  = load_config()

    if getattr(args, "list_orphans", False) or args.cmd == "list":
        cmd_list(cfg)
        return

    f  = getattr(args, "file", None)
    ep = getattr(args, "epistemic", None)

    if not f or not ep:
        parser.print_help()
        return

    promote(
        file_path=f,
        epistemic=ep,
        note=args.note,
        update_config=args.update_config,
        dry_run=args.dry_run,
    )


if __name__ == "__main__":
    main()
