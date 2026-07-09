#!/usr/bin/env python3
"""
tools/bootstrap_failsafe.py
Inicialização de primeira execução do sistema de evolução RLL.

O que faz:
  1. Cria todos os diretórios necessários
  2. Tenta baixar e salvar snapshot congelado de cada fonte
  3. Calcula e salva fingerprint inicial de cada snapshot
  4. Inicializa EVOLUTION_TRAIL.jsonl com evento BOOTSTRAP
  5. Inicializa results/manifest.json com estado inicial
  6. Registra artefatos órfãos na trilha

Idempotente: pode ser chamado múltiplas vezes sem corrupção.
--force substitui snapshots existentes.

Uso:
  python tools/bootstrap_failsafe.py --config RLL_JSON_EVOLUTION_WATCHER.yml
  python tools/bootstrap_failsafe.py --config ... --force
  python tools/bootstrap_failsafe.py --config ... --source zenodo_doi_rll
"""

import argparse
import hashlib
import json
import os
import sys
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional

import yaml

# ---------------------------------------------------------------------------
# Fingerprint (mesma lógica do watcher)
# ---------------------------------------------------------------------------

def compute_fingerprint(data: Any, depth: int = 2) -> str:
    def extract_keys(obj, prefix="", d=0):
        keys = []
        if isinstance(obj, dict) and d < depth:
            for k, v in obj.items():
                full = f"{prefix}.{k}" if prefix else k
                keys.append(full)
                keys.extend(extract_keys(v, full, d + 1))
        return keys
    sorted_keys = sorted(set(extract_keys(data)))
    payload = "\n".join(sorted_keys).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


# ---------------------------------------------------------------------------
# Fetch simples para bootstrap
# ---------------------------------------------------------------------------

def fetch_url(url: str, timeout: int = 30) -> Optional[bytes]:
    url = url.replace("\n", "").replace(" ", "")
    try:
        with urllib.request.urlopen(url, timeout=timeout) as resp:
            return resp.read()
    except Exception as exc:
        print(f"    [WARN] fetch failed: {url[:60]}... → {exc}")
        return None


def try_parse_json(raw: bytes) -> Optional[Dict]:
    try:
        return json.loads(raw)
    except Exception:
        return None


# ---------------------------------------------------------------------------
# Bootstrap de uma fonte
# ---------------------------------------------------------------------------

def bootstrap_source(src: Dict[str, Any], force: bool = False) -> Dict:
    sid   = src["id"]
    label = src.get("label", sid)
    ep    = src.get("epistemic", "TOKEN_VAZIO")

    print(f"\n  [{sid}] {label}")

    fs = src.get("failsafe", {})
    snap_path = Path(fs.get("snapshot_path", f"data/failsafe/{sid}_FROZEN.json"))

    # --- Se já existe e não é força, apenas calcula fingerprint ---
    if snap_path.exists() and not force:
        print(f"    snapshot exists: {snap_path} (use --force to overwrite)")
        try:
            data = json.loads(snap_path.read_text(encoding="utf-8"))
            fp = compute_fingerprint(data)
            return {"source_id": sid, "action": "SKIP_EXISTING",
                    "fingerprint": fp, "epistemic": ep}
        except Exception:
            pass

    # --- Tentar baixar (primary → mirrors) ---
    data = None
    origin = None

    primary_url = src.get("primary", {}).get("url", "")
    raw = fetch_url(primary_url) if primary_url else None
    if raw:
        data   = try_parse_json(raw)
        origin = "primary"

    if data is None:
        for m in src.get("mirrors", []):
            raw = fetch_url(m.get("url", ""))
            if raw:
                data   = try_parse_json(raw)
                origin = f"mirror_p{m.get('priority',0)}"
                if data:
                    break

    # --- Fallback: stub mínimo ---
    if data is None:
        print(f"    [FAILSAFE-STUB] creating minimal stub for {sid}")
        data   = {"_bootstrap_stub": True, "source_id": sid,
                  "generated_utc": datetime.now(timezone.utc).isoformat()}
        origin = "stub"
        ep     = "TOKEN_VAZIO"

    # --- Salvar snapshot ---
    snap_path.parent.mkdir(parents=True, exist_ok=True)
    snap_path.write_text(json.dumps(data, indent=2, ensure_ascii=False),
                         encoding="utf-8")
    print(f"    saved snapshot ({origin}): {snap_path}")

    # --- Salvar fingerprint ---
    fp = compute_fingerprint(data)
    for t in src.get("tests", []):
        if t.get("check") == "fingerprint_match":
            ref = Path(t["ref_path"])
            ref.parent.mkdir(parents=True, exist_ok=True)
            if not ref.exists() or force:
                ref.write_text(fp + "\n", encoding="utf-8")
                print(f"    fingerprint saved: {ref}")

    return {"source_id": sid, "action": "BOOTSTRAP",
            "origin": origin, "fingerprint": fp, "epistemic": ep,
            "snapshot_path": str(snap_path)}


# ---------------------------------------------------------------------------
# Bootstrap de artefatos órfãos
# ---------------------------------------------------------------------------

def register_orphans(trail_cfg: Dict, trail_log: Path) -> List[Dict]:
    events = []
    ts = datetime.now(timezone.utc).isoformat()
    orphans = trail_cfg.get("registered_orphan_artifacts", [])

    for o in orphans:
        path   = Path(o["path"])
        exists = path.exists()
        ev = {
            "timestamp_utc":   ts,
            "source_id":       f"orphan:{o['path']}",
            "action":          "ORPHAN_REGISTERED",
            "schema_drift":    False,
            "epistemic_before": "TOKEN_VAZIO",
            "epistemic_after":  o.get("epistemic", "TOKEN_VAZIO"),
            "fingerprint_before": "",
            "fingerprint_after":  "",
            "artifact_path":   o["path"],
            "rll_paths_affected": [],
            "notes": (f"exists={exists} status={o.get('status','?')} "
                      f"promote_to={o.get('promote_to','?')}"),
        }
        events.append(ev)
        status_icon = "✓" if exists else "✗"
        print(f"    [{status_icon}] orphan: {o['path']}  status={o.get('status','?')}")

    return events


# ---------------------------------------------------------------------------
# Emitir na trilha
# ---------------------------------------------------------------------------

def emit_events(trail_log: Path, events: List[Dict]) -> None:
    trail_log.parent.mkdir(parents=True, exist_ok=True)
    with open(trail_log, "a", encoding="utf-8") as f:
        for ev in events:
            f.write(json.dumps(ev, ensure_ascii=False) + "\n")


# ---------------------------------------------------------------------------
# Inicializar manifest
# ---------------------------------------------------------------------------

def init_manifest(manifest_path: Path, source_results: List[Dict]) -> None:
    if manifest_path.exists():
        try:
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        except Exception:
            manifest = {}
    else:
        manifest = {}

    manifest.setdefault("version", "1.0")
    manifest.setdefault("artifacts", {})
    manifest["generated_utc"] = datetime.now(timezone.utc).isoformat()
    manifest["bootstrap_run"] = True

    for r in source_results:
        sid = r.get("source_id", "unknown")
        if not sid.startswith("orphan:"):
            manifest["artifacts"][sid] = {
                "last_updated": datetime.now(timezone.utc).isoformat(),
                "action":       r.get("action", "BOOTSTRAP"),
                "epistemic":    r.get("epistemic", "TOKEN_VAZIO"),
                "schema_drift": False,
                "artifact_path": r.get("snapshot_path", ""),
            }

    manifest_path.parent.mkdir(parents=True, exist_ok=True)
    manifest_path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False),
                             encoding="utf-8")
    print(f"\n  manifest updated: {manifest_path}")


# ---------------------------------------------------------------------------
# Criar diretórios obrigatórios
# ---------------------------------------------------------------------------

REQUIRED_DIRS = [
    "data/failsafe",
    "data/rollback",
    "schemas/fingerprints",
    "artifacts",
    "docs/audit",
    "tools",
    "scripts",
]

def ensure_dirs() -> None:
    print("\n[1] Ensuring directory structure...")
    for d in REQUIRED_DIRS:
        Path(d).mkdir(parents=True, exist_ok=True)
        print(f"  ✓ {d}/")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Bootstrap RLL JSON Evolution Watcher")
    parser.add_argument("--config", default="RLL_JSON_EVOLUTION_WATCHER.yml")
    parser.add_argument("--force",  action="store_true",
                        help="Overwrite existing snapshots and fingerprints")
    parser.add_argument("--source", default=None,
                        help="Bootstrap only this source ID")
    args = parser.parse_args()

    print("=" * 60)
    print("  RLL JSON Evolution Watcher — Bootstrap")
    print("=" * 60)

    # Carregar config
    cfg_path = Path(args.config)
    if not cfg_path.exists():
        print(f"[ERROR] config not found: {cfg_path}")
        sys.exit(1)
    with open(cfg_path, encoding="utf-8") as f:
        cfg = yaml.safe_load(f)

    # 1. Diretórios
    ensure_dirs()

    # 2. Fontes
    sources = cfg.get("sources", [])
    if args.source:
        sources = [s for s in sources if s["id"] == args.source]
        if not sources:
            print(f"[ERROR] source '{args.source}' not found")
            sys.exit(1)

    print(f"\n[2] Bootstrapping {len(sources)} source(s)...")
    source_results = []
    trail_events   = []
    ts = datetime.now(timezone.utc).isoformat()

    for src in sources:
        r = bootstrap_source(src, force=args.force)
        source_results.append(r)
        trail_events.append({
            "timestamp_utc":      ts,
            "source_id":          r["source_id"],
            "action":             r["action"],
            "schema_drift":       False,
            "epistemic_before":   "TOKEN_VAZIO",
            "epistemic_after":    r["epistemic"],
            "fingerprint_before": "",
            "fingerprint_after":  r.get("fingerprint", ""),
            "artifact_path":      r.get("snapshot_path", ""),
            "rll_paths_affected": src.get("rll_paths", []),
            "notes":              f"bootstrap origin={r.get('origin','?')}",
        })

    # 3. Artefatos órfãos
    trail_cfg  = cfg.get("artifact_evolution_trail", {})
    trail_log  = Path(trail_cfg.get("trail_log", "artifacts/EVOLUTION_TRAIL.jsonl"))
    print(f"\n[3] Registering orphan artifacts...")
    orphan_events = register_orphans(trail_cfg, trail_log)
    trail_events.extend(orphan_events)

    # 4. Trilha
    print(f"\n[4] Writing to trail: {trail_log}")
    emit_events(trail_log, trail_events)
    print(f"  {len(trail_events)} event(s) written")

    # 5. Manifest
    print("\n[5] Updating manifest...")
    init_manifest(Path("results/manifest.json"), source_results)

    # 6. Resumo
    print("\n" + "=" * 60)
    print("  BOOTSTRAP COMPLETE")
    print("=" * 60)
    for r in source_results:
        icon = "✅" if r["epistemic"] == "VERIFIED" else "⚠️"
        print(f"  {icon} {r['source_id']:<30} {r['epistemic']}  ({r['action']})")
    print(f"\n  Orphans registered: {len(orphan_events)}")
    print(f"  Trail:              {trail_log}")
    print(f"  Manifest:           results/manifest.json")
    print()


if __name__ == "__main__":
    main()
