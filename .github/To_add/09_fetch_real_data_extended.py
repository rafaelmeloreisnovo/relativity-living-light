#!/usr/bin/env python3
"""
fetch_real_data_extended.py
Gerado: 2026-06-27 | ∆RafaelVerboΩ | RAFCODE-Φ

Extensão do validacao_real/fetch_real_data.py para incluir:
- Hypervelocity stars (Vizier CDS)
- CHIME/FRB Catalog 1
- DESI DR2 BAO (já existe, verifica integridade)
- Moresco et al. H(z) compilação 2023

Compatível com: Termux ARM32 sem root
Dependências: urllib (stdlib), yaml (pyyaml)
"""
from __future__ import annotations

import hashlib
import json
import sys
import urllib.request
import urllib.error
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA = HERE / "data" / "real"
OUT = HERE / "data" / "real" / "fetched_extended"
TIMEOUT = 30


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def try_download(url: str, dest: Path, label: str) -> dict:
    print(f"  [{label}] tentando: {url[:80]}...")
    try:
        req = urllib.request.Request(
            url, headers={"User-Agent": "RLL-real-fetch/2.0"}
        )
        with urllib.request.urlopen(req, timeout=TIMEOUT) as r:
            data = r.read()
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_bytes(data)
        chk = sha256_file(dest)
        print(f"  -> OK {len(data)} bytes  sha256={chk[:16]}...")
        return {
            "status": "downloaded",
            "bytes": len(data),
            "sha256": chk,
            "local_path": str(dest),
            "fetched_utc": utc_now(),
        }
    except (urllib.error.URLError, TimeoutError, OSError) as e:
        print(f"  -> FALHOU: {e.__class__.__name__}: {e}")
        return {
            "status": "failed",
            "error": str(e),
            "local_path": str(dest),
            "fallback_action": "preencher manualmente",
        }


SOURCES = [
    # ── Cosmologia ──────────────────────────────────────────────────────────
    {
        "id": "moresco_2023_hz_compilation",
        "label": "H(z) Moresco 2023 compilação",
        "url": (
            "https://raw.githubusercontent.com/CosmoStatGW/"
            "MontePython-Cosmostat/master/data/Hz_Moresco_compilation.txt"
        ),
        "dest": DATA / "cosmology" / "moresco_2023_hz_compilation.txt",
        "falsifier": "H_RLL(z) vs H_LCDM(z) dentro das barras Moresco 2023",
        "domain": "cosmology_expansion",
    },
    {
        "id": "pantheon_plus_summary",
        "label": "Pantheon+ SH0ES README",
        "url": (
            "https://raw.githubusercontent.com/PantheonPlusSH0ES/"
            "DataRelease/main/README.md"
        ),
        "dest": DATA / "cosmology" / "pantheon_plus_sh0es_readme_latest.md",
        "falsifier": "dL_RLL(z) vs dL_LCDM(z) em SNe Ia — chi2 < chi2_LCDM",
        "domain": "cosmology_sne",
    },
    # ── Objetos compactos / cinemática ─────────────────────────────────────
    {
        "id": "brown_2014_hvs_vizier",
        "label": "MMT HVS Survey Brown 2014 (Vizier)",
        "url": (
            "https://vizier.cds.unistra.fr/viz-bin/asu-tsv"
            "?-source=J/ApJ/787/89/table1&-out.max=100"
        ),
        "dest": DATA / "kinematics" / "brown_2014_hvs_vizier.tsv",
        "falsifier": "v_gal HVS distribuição vs potencial RLL vs LCDM",
        "domain": "kinematics_hvs",
    },
    {
        "id": "marchetti_2022_gaia_hvs",
        "label": "Gaia DR3 HVS Marchetti 2022 (Vizier)",
        "url": (
            "https://vizier.cds.unistra.fr/viz-bin/asu-tsv"
            "?-source=J/MNRAS/515/767/table1&-out.max=200"
        ),
        "dest": DATA / "kinematics" / "marchetti_2022_gaia_hvs.tsv",
        "falsifier": "Distribuição v_total 156 HVS vs potencial RLL",
        "domain": "kinematics_hvs",
    },
    # ── FRB / plasma ────────────────────────────────────────────────────────
    {
        "id": "chime_frb_catalog1_readme",
        "label": "CHIME/FRB Catalog 1 README",
        "url": "https://www.chime-frb.ca/static/data/catalog1_readme.txt",
        "dest": DATA / "plasma" / "chime_frb_catalog1_readme.txt",
        "falsifier": "DM_cosmic_obs vs DM_pred_RLL(ΩP0>0) chi2",
        "domain": "frb_plasma",
        "note": "Catalog completo requer download separado (tarball ~50MB)",
    },
    # ── Lensing ─────────────────────────────────────────────────────────────
    {
        "id": "ogle_blg_0462_paper_arxiv",
        "label": "OGLE-2011-BLG-0462 Sahu 2022 (arxiv abstract)",
        "url": "https://arxiv.org/abs/2201.13296",
        "dest": DATA / "lensing" / "ogle_2011_blg_0462_sahu_2022_abstract.html",
        "falsifier": "M_lens_RLL vs M_lens_LCDM para microlensing stellar BH",
        "domain": "lensing_microlensing",
        "note": "Dados fotométricos requerem acesso HST MAST",
    },
]


def main() -> int:
    OUT.mkdir(parents=True, exist_ok=True)
    manifest = {
        "generated_utc": utc_now(),
        "generator": "fetch_real_data_extended.py",
        "schema": "rll.fetch_manifest.extended.v1",
        "sources": [],
    }

    for src in SOURCES:
        print(f"\n=== {src['id']} ===")
        result = try_download(src["url"], Path(src["dest"]), src["label"])
        manifest["sources"].append(
            {
                "id": src["id"],
                "label": src["label"],
                "domain": src.get("domain", "unknown"),
                "falsifier": src.get("falsifier", ""),
                "note": src.get("note", ""),
                **result,
            }
        )

    out_manifest = OUT / "fetch_extended_manifest.json"
    out_manifest.write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8"
    )
    print(f"\n=== MANIFESTO: {out_manifest} ===")

    ok = sum(1 for s in manifest["sources"] if s.get("status") == "downloaded")
    fail = len(manifest["sources"]) - ok
    print(f"OK: {ok}  FALHOU: {fail}")

    if fail > 0:
        print("\nACOES NECESSARIAS para fontes que falharam:")
        for s in manifest["sources"]:
            if s.get("status") == "failed":
                print(f"  [{s['id']}] {s.get('fallback_action', 'manual')}")

    return 0 if fail == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
