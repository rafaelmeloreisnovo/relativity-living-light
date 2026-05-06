#!/usr/bin/env python3
"""RLL canonical book/data pipeline artifact generator."""
from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import subprocess
from pathlib import Path
from typing import Any

VALID_STATUS = [
    "reference_only",
    "metadata_ready",
    "dry_run",
    "fetched",
    "computed",
    "blocked",
]

STATUS_BY_MODE = {
    "metadata_only": "metadata_ready",
    "dry_run": "dry_run",
    "fetch": "fetched",
    "compute": "computed",
}

BOOK_SCOPE_MAP: dict[str, dict[str, Any]] = {
    "methodology": {
        "objective": "validar rota metodológica.",
        "chapters": [
            "book/11_metodologia_pipeline_validacao.md",
            "book/12_metodologia_dados_mock.md",
            "book/13_metodologia_dados_reais.md",
            "book/14_metodologia_notebooks_scripts.md",
        ],
        "documents": [],
    },
    "real_data": {
        "objective": "auditar dados reais e χ² inicial.",
        "chapters": ["book/13_metodologia_dados_reais.md"],
        "documents": [
            "data/real/Hz_data_real.csv",
            "data/real/BAO_data_real.csv",
            "results/RLL_chi2_results.csv",
        ],
    },
    "scripts": {
        "objective": "mapear execução reprodutível.",
        "chapters": ["book/14_metodologia_notebooks_scripts.md"],
        "documents": ["scripts/run_repro_all.sh", "scripts/run_desi_dha_pipeline.py"],
    },
    "observational_validation": {
        "objective": "gerar rota de validação observacional completa.",
        "chapters": [
            "book/15_validacao_expansao_hz.md",
            "book/16_validacao_supernovas_dmu.md",
            "book/17_validacao_fracoes_energia.md",
            "book/18_validacao_crescimento_fs8.md",
            "book/19_validacao_lentes_aglomerados.md",
            "book/20_validacao_rotacao_galaxias.md",
            "book/21_validacao_desi_boss.md",
            "book/22_validacao_jwst_agn_smbh.md",
            "book/23_resultados_estatisticos.md",
            "book/24_resultados_figuras_painel.md",
        ],
        "documents": [],
    },
    "desi_boss": {
        "objective": "gerar manifesto de validação DESI/BOSS/Planck.",
        "chapters": ["book/21_validacao_desi_boss.md"],
        "documents": ["DESI DR2", "BOSS DR12", "eBOSS DR16", "Planck 2018"],
    },
    "amas_mcrp": {
        "objective": "ligar AMAS/SAA ao MCRP sem afirmar validação total.",
        "chapters": [],
        "documents": [
            "docs/VALIDATION_DATA_MATRIX_RLL_MCRP.md",
            "docs/cases/AMAS_SOUTH_ATLANTIC_MAGNETIC_ANOMALY_RLL.md",
            "docs/pipelines/GEOMAGNETIC_VALIDATION_PIPELINE.md",
            "docs/pipelines/RADIATION_TRANSMISSION_VALIDATION.md",
        ],
    },
}

DATASET_GROUP_MAP: dict[str, dict[str, Any]] = {
    "geomagnetic": {
        "formula_targets": ["M(t)", "m(t)", "T_M"],
        "sources": [
            "NOAA/NCEI IGRF14",
            "NOAA/NCEI WMM2025",
            "ESA Swarm",
            "NASA South Atlantic Anomaly",
        ],
    },
    "heliophysics": {
        "formula_targets": ["Φ_ext", "SW", "T_M", "Φ_eff"],
        "sources": ["NASA OMNI/SPDF", "NMDB", "GOES energetic particles", "SPENVIS AE9/AP9"],
    },
    "cosmology": {
        "formula_targets": ["E²(a)", "f(z)", "w(z)", "comparação RLL vs ΛCDM/w0waCDM"],
        "sources": ["DESI DR2 BAO", "Pantheon+ SNe Ia", "Planck 2018 chains", "H(z)", "fσ8"],
    },
}


def git_sha() -> str:
    try:
        return subprocess.check_output(["git", "rev-parse", "HEAD"], text=True).strip()
    except Exception:
        return "unknown"


def resolve_scope(scope: str) -> dict[str, Any]:
    if scope == "all":
        chapters: list[str] = []
        documents: list[str] = []
        objectives: list[str] = []
        for key in BOOK_SCOPE_MAP:
            chapters.extend(BOOK_SCOPE_MAP[key]["chapters"])
            documents.extend(BOOK_SCOPE_MAP[key]["documents"])
            objectives.append(f"{key}: {BOOK_SCOPE_MAP[key]['objective']}")
        return {
            "scope": "all",
            "chapters": sorted(set(chapters)),
            "documents": sorted(set(documents)),
            "objective": " ; ".join(objectives),
        }
    payload = BOOK_SCOPE_MAP[scope]
    return {
        "scope": scope,
        "chapters": payload["chapters"],
        "documents": payload["documents"],
        "objective": payload["objective"],
    }


def resolve_groups(group: str) -> list[str]:
    return list(DATASET_GROUP_MAP.keys()) if group == "all" else [group]


def status_for(mode: str) -> str:
    status = STATUS_BY_MODE[mode]
    return "blocked" if mode == "compute" else status


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--book-scope", required=True, choices=[*BOOK_SCOPE_MAP.keys(), "all"])
    parser.add_argument("--dataset-group", required=True, choices=[*DATASET_GROUP_MAP.keys(), "all"])
    parser.add_argument("--mode", required=True, choices=list(STATUS_BY_MODE.keys()))
    parser.add_argument("--output-dir", required=True)
    args = parser.parse_args()

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "book").mkdir(parents=True, exist_ok=True)

    run_utc = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    commit_sha = os.getenv("GITHUB_SHA") or git_sha()

    scope = resolve_scope(args.book_scope)
    groups = resolve_groups(args.dataset_group)
    global_status = status_for(args.mode)

    sections = []
    source_lines = ["# SOURCES", ""]
    claims_lines = [
        "# CLAIM_REFERENCE_AUDIT",
        "",
        "Status global da execução: `Parcial real em preparação`.",
        "",
        "| Hipótese | Dado | Modelo | Métrica | Referência | Status |",
        "|---|---|---|---|---|---|",
    ]

    for group in groups:
        group_cfg = DATASET_GROUP_MAP[group]
        hypothesis = "Validação depende de dados reais, métricas reproduzíveis e trilha canônica do livro."
        data = f"Grupo {group} selecionado via dataset_group."
        model = ", ".join(group_cfg["formula_targets"])
        metric = "Comparação RLL vs referências externas com rastreabilidade."
        reference = "; ".join(group_cfg["sources"])
        row = {
            "group": group,
            "Hipótese": hypothesis,
            "Dado": data,
            "Modelo": model,
            "Métrica": metric,
            "Referência": reference,
            "Status": global_status,
        }
        sections.append(row)
        source_lines.extend([f"## {group}", *(f"- {src}" for src in group_cfg["sources"]), ""])
        claims_lines.append(
            f"| {hypothesis} | {data} | {model} | {metric} | {reference} | {global_status} |"
        )

    manifest = {
        "run_utc": run_utc,
        "commit_sha": commit_sha,
        "book_scope": args.book_scope,
        "dataset_group": args.dataset_group,
        "mode": args.mode,
        "status": "Parcial real em preparação",
        "scope_objective": scope["objective"],
        "chapters_used": scope["chapters"],
        "scientific_inputs": ["docs/", "data/", "data/pipelines/structure_d/"],
        "results_outputs": ["results/"],
        "ingestion_history_only": ["to_Add/"],
        "records": sections,
        "allowed_status": VALID_STATUS,
        "promotion_guard": "pipeline não promove status para Real validado sem execução real com dados, métricas e reprodutibilidade",
    }

    report = [
        "# PIPELINE_REPORT",
        "",
        f"- run_utc: `{run_utc}`",
        f"- commit_sha: `{commit_sha}`",
        f"- book_scope: `{args.book_scope}`",
        f"- dataset_group: `{args.dataset_group}`",
        f"- mode: `{args.mode}`",
        f"- status editorial: `Parcial real em preparação`",
        f"- objetivo: {scope['objective']}",
        "",
        "## Separação obrigatória",
        "- Hipótese",
        "- Dado",
        "- Modelo",
        "- Métrica",
        "- Referência",
        f"- Status: `{global_status}`",
    ]

    book_route = [
        "# BOOK_ROUTE",
        "",
        "Ordem editorial guiada por `book/README.md`.",
        "",
        f"Escopo selecionado: `{args.book_scope}`.",
        "",
        "## Capítulos priorizados",
        *(f"- {chapter}" for chapter in scope["chapters"]),
        "",
        "## Documentos e ativos relacionados",
        *(f"- {doc}" for doc in scope["documents"]),
    ]

    chapters_used = ["# CHAPTERS_USED", "", *(f"- {chapter}" for chapter in scope["chapters"])]

    (output_dir / "MANIFEST.json").write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    (output_dir / "SOURCES.md").write_text("\n".join(source_lines) + "\n", encoding="utf-8")
    (output_dir / "PIPELINE_REPORT.md").write_text("\n".join(report) + "\n", encoding="utf-8")
    (output_dir / "CLAIM_REFERENCE_AUDIT.md").write_text("\n".join(claims_lines) + "\n", encoding="utf-8")
    (output_dir / "book" / "BOOK_ROUTE.md").write_text("\n".join(book_route) + "\n", encoding="utf-8")
    (output_dir / "book" / "CHAPTERS_USED.md").write_text("\n".join(chapters_used) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
