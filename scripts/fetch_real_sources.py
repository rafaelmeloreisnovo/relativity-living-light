#!/usr/bin/env python3
from __future__ import annotations
import argparse, datetime as dt, hashlib, json
from pathlib import Path
import requests

SOURCES = {
"igrf14": {"group":"geomagnetic","url":"https://www.ncei.noaa.gov/products/international-geomagnetic-reference-field","license":"NOAA public data","version":"IGRF14","heavy":False},
"wmm2025": {"group":"geomagnetic","url":"https://www.ncei.noaa.gov/index.php/products/world-magnetic-model/wmm-coefficients","license":"NOAA public data","version":"WMM2025","heavy":False},
"omni": {"group":"heliophysics","url":"https://omniweb.gsfc.nasa.gov/","license":"NASA open data","version":"OMNI/SPDF","heavy":False},
"nmdb": {"group":"heliophysics","url":"https://www.nmdb.eu/","license":"NMDB terms","version":"current","heavy":False},
"desi": {"group":"cosmology","url":"https://data.desi.lbl.gov/","license":"DESI data policy","version":"DR2","heavy":True},
"pantheon": {"group":"cosmology","url":"https://raw.githubusercontent.com/PantheonPlusSH0ES/DataRelease/main/README.md","license":"repository license","version":"DataRelease","heavy":False},
"planck": {"group":"cosmology","url":"https://pla.esac.esa.int/","license":"ESA PLA terms","version":"Planck Legacy","heavy":True},
"spenvis_reference": {"group":"heliophysics","url":"https://www.spenvis.oma.be/","license":"SPENVIS terms","version":"reference","heavy":True},
}

def sha256_file(p: Path)->str:
 h=hashlib.sha256(); h.update(p.read_bytes()); return h.hexdigest()

def fetch_text(url:str, out:Path)->tuple[str,str|None]:
 try:
  r=requests.get(url,timeout=30)
  r.raise_for_status()
  out.write_bytes(r.content)
  return "fetched", None
 except Exception as e:
  return "fetch_failed", str(e)

def fetch_csv(url: str, out: Path) -> tuple[str, str | None]:
 try:
  r = requests.get(url, timeout=60)
  r.raise_for_status()
  out.write_bytes(r.content)
  # sanity check
  with out.open("r", encoding="utf-8", errors="replace") as fh:
   sample = fh.read(2048)
  if "," not in sample and "\t" not in sample:
   return "fetch_failed", "downloaded file is not a recognizable table"
  return "fetched", None
 except Exception as e:
  return "fetch_failed", str(e)

def main()->int:
 ap=argparse.ArgumentParser()
 ap.add_argument("--dataset-group",default="all",choices=["geomagnetic","heliophysics","cosmology","all"])
 ap.add_argument("--mode",default="full",choices=["metadata_only","fetch","compute","plots","full"])
 ap.add_argument("--output-dir",default="artifacts/rll-real-run")
 for k in ["igrf14","wmm2025","omni","nmdb","desi","pantheon","planck","spenvis_reference"]:
  ap.add_argument(f"--fetch-{k.replace('_','-')}",action="store_true")
  ap.add_argument(f"--no-fetch-{k.replace('_','-')}",dest=f"fetch_{k}",action="store_false")
  ap.set_defaults(**{f"fetch_{k}":True if k in ["igrf14","wmm2025","omni","desi","pantheon"] else False})
 a=ap.parse_args()
 root=Path(a.output_dir); raw=root/"raw"; raw.mkdir(parents=True,exist_ok=True)
 groups=[a.dataset_group] if a.dataset_group!="all" else ["geomagnetic","heliophysics","cosmology"]
 results=[]; failed=[]
 for name,cfg in SOURCES.items():
  if cfg["group"] not in groups: continue
  if not getattr(a,f"fetch_{name}"): continue
  rec={"source":name,**cfg,"run_utc":dt.datetime.now(dt.timezone.utc).isoformat()}
  d=raw/name; d.mkdir(parents=True,exist_ok=True)
  if a.mode=="metadata_only":
   rec["status"]="metadata_only"
  elif cfg["heavy"]:
   rec["status"]="pending_manual_or_large_download"
  else:
   out=d/"payload.bin"
   st,err=fetch_text(cfg["url"],out)
   rec["status"]=st
   if st=="fetched": rec["files"]= [{"path":str(out.relative_to(root)),"sha256":sha256_file(out)}]
   else: rec["error"]=err; failed.append(name)
  results.append(rec)

 # Cosmology lightweight curated pulls for direct pipeline use
 curated = []
 if "cosmology" in groups and a.mode in ("fetch", "full", "compute"):
  curated_dir = raw / "cosmology_curated"
  curated_dir.mkdir(parents=True, exist_ok=True)
  curated_urls = {
   "pantheon_readme.md": "https://raw.githubusercontent.com/PantheonPlusSH0ES/DataRelease/main/README.md",
   "desi_homepage.html": "https://www.desi.lbl.gov/",
  }
  for fname, url in curated_urls.items():
   target = curated_dir / fname
   status, err = fetch_text(url, target)
   item = {"name": fname, "url": url, "status": status}
   if status == "fetched":
    item["sha256"] = sha256_file(target)
   else:
    item["error"] = err
   curated.append(item)

  # mirror current repo-ready real data into artifact to unify YAML outputs
  local_real = {
   "Hz_data_real.csv": Path("data/real/Hz_data_real.csv"),
   "BAO_data_real.csv": Path("data/real/BAO_data_real.csv"),
   "CMB_shift_real.json": Path("data/real/CMB_shift_real.json"),
  }
  for fname, src in local_real.items():
   if src.exists():
    dst = curated_dir / fname
    dst.write_bytes(src.read_bytes())
    curated.append({"name": fname, "source": str(src), "status": "copied_from_repo", "sha256": sha256_file(dst)})
   else:
    curated.append({"name": fname, "source": str(src), "status": "missing_in_repo"})

  with (curated_dir / "CURATED_SOURCES.json").open("w", encoding="utf-8") as fh:
   json.dump(curated, fh, indent=2, ensure_ascii=False)

  with (curated_dir / "CURATED_SOURCES.md").open("w", encoding="utf-8") as fh:
   fh.write("# CURATED_SOURCES\n\n")
   fh.write("|name|status|origin|\n|---|---|---|\n")
   for item in curated:
    origin = item.get("url") or item.get("source", "-")
    fh.write(f"|{item['name']}|{item['status']}|{origin}|\n")
 (raw/"SOURCES.json").write_text(json.dumps(results,indent=2,ensure_ascii=False),encoding="utf-8")
 ds=["# DATA_SOURCES","", "|source|group|version|status|url|","|---|---|---|---|---|"]
 fr=["# FETCH_REPORT","",f"mode: `{a.mode}`"]
 for r in results:
  ds.append(f"|{r['source']}|{r['group']}|{r['version']}|{r['status']}|{r['url']}|")
  fr.append(f"- {r['source']}: {r['status']}")
 (root/"DATA_SOURCES.md").write_text("\n".join(ds),encoding="utf-8")
 (root/"FETCH_REPORT.md").write_text("\n".join(fr),encoding="utf-8")
 if a.mode=="compute" and any(x in failed for x in ["omni","pantheon"]):
  raise SystemExit("Essential data missing for compute mode: omni/pantheon")
 return 0

if __name__=='__main__': raise SystemExit(main())
