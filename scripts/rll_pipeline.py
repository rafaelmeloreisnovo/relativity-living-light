#!/usr/bin/env python3
"""RLL/MCRP manual pipeline artifact generator."""
from __future__ import annotations
import argparse, datetime as dt, json, os, subprocess
from pathlib import Path

VALID_STATUS = ["reference_only","metadata_ready","dry_run","fetched","computed","blocked"]
GROUPS = {
 "geomagnetic": {
  "formula_targets":["M(t)","m(t)","T_M"],
  "sources":[
   {"name":"NOAA/NCEI IGRF14","url":"https://www.ncei.noaa.gov/products/international-geomagnetic-reference-field","doi":"","version":"IGRF-14","license":"Public domain (US Gov)","method":"metadata_registry","limitations":"Sem download bruto neste PR."},
   {"name":"NOAA/NCEI WMM2025","url":"https://www.ncei.noaa.gov/products/world-magnetic-model","doi":"","version":"WMM2025","license":"Public domain (US Gov)","method":"metadata_registry","limitations":"Sem download bruto neste PR."},
   {"name":"ESA Swarm","url":"https://swarm-diss.eo.esa.int/","doi":"","version":"mission archive","license":"ESA terms","method":"metadata_registry","limitations":"Acesso/seleção de produtos pendentes."},
   {"name":"NASA South Atlantic Anomaly","url":"https://www.nasa.gov/mission_pages/sunearth/news/gallery/saa.html","doi":"","version":"web reference","license":"NASA media usage policy","method":"reference_only","limitations":"Caso observacional local; não prova global do RLL."}
  ],
  "dry_run":"AMAS_DRY_RUN.md"
 },
 "heliophysics": {
  "formula_targets":["Φ_ext","SW","T_M","Φ_eff"],
  "sources":[
   {"name":"NASA OMNI/SPDF","url":"https://omniweb.gsfc.nasa.gov/","doi":"","version":"OMNI2/OMNIWeb","license":"NASA/SPDF open data","method":"metadata_registry","limitations":"Sem ingestão temporal real neste PR."},
   {"name":"NMDB neutron monitor database","url":"https://www.nmdb.eu/","doi":"","version":"NMDB live archive","license":"NMDB terms","method":"metadata_registry","limitations":"Rate limits e seleção de estações pendentes."},
   {"name":"GOES energetic particles","url":"https://www.ncei.noaa.gov/products/satellite/goes-space-environment-monitor","doi":"","version":"GOES SEM","license":"Public domain (US Gov)","method":"metadata_registry","limitations":"Sem fetch pesado por padrão."},
   {"name":"SPENVIS AE9/AP9","url":"https://www.spenvis.oma.be/","doi":"","version":"AE9/AP9","license":"SPENVIS terms","method":"reference_only","limitations":"Pode exigir fluxo autenticado/licenciamento."}
  ],
  "dry_run":"RADIATION_DRY_RUN.md"
 },
 "cosmology": {
  "formula_targets":["E²(a)","f(z)","w(z)","RLL vs ΛCDM/w0waCDM"],
  "sources":[
   {"name":"DESI DR2 BAO","url":"https://www.desi.lbl.gov/","doi":"","version":"DR2","license":"DESI collaboration policy","method":"metadata_registry","limitations":"Produtos exatos de release devem ser fixados por manifesto."},
   {"name":"Pantheon+ SNe Ia","url":"https://github.com/PantheonPlusSH0ES/DataRelease","doi":"","version":"Pantheon+","license":"Project terms","method":"metadata_registry","limitations":"Sem fetch automático neste PR."},
   {"name":"Planck 2018 chains","url":"https://pla.esac.esa.int/","doi":"","version":"2018 Legacy","license":"Planck Legacy terms","method":"metadata_registry","limitations":"Download de chains pode ser pesado."},
   {"name":"H(z) cosmic chronometers","url":"https://arxiv.org/abs/1604.01410","doi":"10.48550/arXiv.1604.01410","version":"compiled set","license":"Article/license dependent","method":"reference_only","limitations":"Compilação heterogênea por survey."},
   {"name":"fσ8","url":"https://arxiv.org/abs/1801.01590","doi":"10.48550/arXiv.1801.01590","version":"compiled constraints","license":"Article/license dependent","method":"reference_only","limitations":"Necessita harmonização de convenções."}
  ],
  "dry_run":"COSMOLOGY_DRY_RUN.md"
 }
}

def git_sha()->str:
    try: return subprocess.check_output(["git","rev-parse","HEAD"]).decode().strip()
    except Exception: return "unknown"

def status_for(mode:str)->str:
    return {"metadata_only":"metadata_ready","dry_run":"dry_run","fetch":"fetched","compute":"computed"}.get(mode,"blocked")

def write_group(group:str,mode:str,base:Path,run_utc:str,sha:str)->dict:
    cfg=GROUPS[group]; gdir=base/group; gdir.mkdir(parents=True,exist_ok=True)
    item_status=status_for(mode)
    items=[]
    for s in cfg["sources"]:
        st = "reference_only" if s["method"]=="reference_only" and mode in {"metadata_only","dry_run"} else item_status
        if mode=="compute" and st=="computed":
            st="blocked"
        items.append({**s,"status":st})
    manifest={"dataset_group":group,"mode":mode,"run_utc":run_utc,"commit_sha":sha,"formula_targets":cfg["formula_targets"],"claims":{"hypothesis":"RLL/MCRP depende de validação reprodutível com dados reais.","data":"Sem promoção para 'Real validado' sem processamento real.","model":"Cálculo total pode operar como stub até ingestão real.","metric":"Métricas ficam rastreáveis no manifesto e relatório."},"items":items,"allowed_status":VALID_STATUS,"promotion_guard":"forbid_real_validated_without_real_data_and_reproducible_metrics"}
    (gdir/"MANIFEST.json").write_text(json.dumps(manifest,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
    (gdir/"SOURCES.md").write_text("\n".join([f"# Sources — {group}","",f"Run UTC: {run_utc}",f"Commit: `{sha}`","",*(f"- **{i['name']}** | status: `{i['status']}` | URL: {i['url']} | versão: {i['version']} | licença: {i['license']} | método: {i['method']} | limitações: {i['limitations']}" for i in items)] )+"\n",encoding="utf-8")
    (gdir/cfg["dry_run"]).write_text(f"# {cfg['dry_run']}\n\n- dataset_group: `{group}`\n- mode: `{mode}`\n- status geral: `{item_status}`\n- Observação: AMAS/SAA permanece caso local observacional quando aplicável.\n",encoding="utf-8")
    return manifest

def main()->int:
    ap=argparse.ArgumentParser()
    ap.add_argument("--dataset-group",required=True,choices=["geomagnetic","heliophysics","cosmology","all"])
    ap.add_argument("--mode",required=True,choices=["metadata_only","dry_run","fetch","compute"])
    ap.add_argument("--output-dir",required=True)
    args=ap.parse_args()
    out=Path(args.output_dir); out.mkdir(parents=True,exist_ok=True)
    run_utc=dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    sha=os.getenv("GITHUB_SHA") or git_sha()
    groups=["geomagnetic","heliophysics","cosmology"] if args.dataset_group=="all" else [args.dataset_group]
    manifests=[write_group(g,args.mode,out,run_utc,sha) for g in groups]
    (out/"PIPELINE_REPORT.md").write_text(f"# RLL Pipeline Report\n\n- run_utc: `{run_utc}`\n- commit_sha: `{sha}`\n- dataset_group: `{args.dataset_group}`\n- mode: `{args.mode}`\n- guardrail: Nenhuma claim promovida para **Real validado** sem dados reais processados e métricas reproduzíveis.\n",encoding="utf-8")
    (out/"CLAIM_REFERENCE_AUDIT.md").write_text("# Claim/Reference Audit\n\n## Separação obrigatória\n- Hipótese: declarada, não validada por inferência retórica.\n- Dado: origem externa rastreável por URL/DOI e licença.\n- Modelo: fórmulas-alvo por domínio.\n- Métrica: somente reproduzível com processamento real.\n\n## Resultado desta execução\n- Estado global: **metadata-only / dry-run oriented** quando sem ingestão real.\n- AMAS/SAA: **caso local observacional**, não prova global do RLL.\n",encoding="utf-8")
    (out/"MANIFEST.json").write_text(json.dumps({"run_utc":run_utc,"commit_sha":sha,"dataset_group":args.dataset_group,"mode":args.mode,"groups":[m["dataset_group"] for m in manifests]},indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
    (out/"SOURCES.md").write_text("# Aggregated Sources\n\nVeja SOURCES.md em cada subdiretório de dataset_group.\n",encoding="utf-8")
    return 0
if __name__=='__main__':
    raise SystemExit(main())
