#!/usr/bin/env python3
from __future__ import annotations
import argparse,csv,json,re
from dataclasses import dataclass,asdict
from pathlib import Path
BLOCK_RE=re.compile(r"\\begin\{align\*?\}(.*?)\\end\{align\*?\}",re.S); INLINE_RE=re.compile(r"\$(.+?)\$",re.S); DISPLAY_RE=re.compile(r"\\\[(.+?)\\\]",re.S); EQ_RE=re.compile(r"^\s*(?:\d+\.\s*&\s*)?(.*?)\\\\\s*$")
@dataclass
class Formula: source:str; category:str; expression:str

def classify(expr:str)->str:
 l=expr.lower()
 if any(k in l for k in ["hz","bao","chi","aic","bic","e^2","f("]): return "cosmology_metrics"
 if any(k in l for k in ["crc","hash","merkle","xor","poly"]): return "integridade_e_criptografia"
 return "geral"

def extract(text:str,src:str)->list[Formula]:
 o=[]
 for b in BLOCK_RE.findall(text):
  for line in b.splitlines():
   m=EQ_RE.match(line)
   if m and m.group(1).strip(): o.append(Formula(src,classify(m.group(1))," ".join(m.group(1).split())))
 for pat in (DISPLAY_RE,INLINE_RE):
  for e in pat.findall(text):
   e=" ".join(e.split())
   if len(e)>5 and any(ch in e for ch in "=\\^_"): o.append(Formula(src,classify(e),e))
 s=set(); u=[]
 for f in o:
  k=(f.source,f.expression)
  if k not in s: s.add(k); u.append(f)
 return u

def main():
 p=argparse.ArgumentParser(); p.add_argument('--root',default='.'); p.add_argument('--outdir',default='artifacts/formulas'); a=p.parse_args()
 r=Path(a.root).resolve(); o=r/a.outdir; o.mkdir(parents=True,exist_ok=True)
 scopes=[r/'README.md',r/'README_MASTER.md',r/'book',r/'docs',r/'data/pipelines/structure_d',r/'RAFAELIA_COSMO_STRUCTURE_D',r/'RMR',r/'newadd']
 files=[]
 for s in scopes:
  if s.is_file(): files.append(s)
  elif s.exists(): files.extend(s.rglob('*.md'))
 formulas=[]
 for fp in sorted(set(files)):
  formulas.extend(extract(fp.read_text(encoding='utf-8',errors='ignore'),str(fp.relative_to(r))))
 (o/'formulas.json').write_text(json.dumps([asdict(x) for x in formulas],indent=2,ensure_ascii=False),encoding='utf-8')
 with (o/'formulas.csv').open('w',newline='',encoding='utf-8') as f:
  w=csv.writer(f); w.writerow(['source','category','expression']); [w.writerow([x.source,x.category,x.expression]) for x in formulas]
 (o/'FORMAL_ACADEMIC_REPORT.md').write_text(f"# FORMAL_ACADEMIC_REPORT\n\nTotal: **{len(formulas)}**\n",encoding='utf-8')
 by={}
 for x in formulas: by.setdefault(x.source,0); by[x.source]+=1
 (o/'FORMULAS_BY_SOURCE.md').write_text("# FORMULAS_BY_SOURCE\n\n"+"\n".join([f"- {k}: {v}" for k,v in sorted(by.items())]),encoding='utf-8')
 (o/'FORMULAS_CLAIM_MAP.md').write_text("# FORMULAS_CLAIM_MAP\n\n- Nenhuma claim é promovida automaticamente para validação real.\n",encoding='utf-8')
if __name__=='__main__': main()
