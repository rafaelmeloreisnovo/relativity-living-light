#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, math, hashlib, datetime as dt
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Any, Dict, List
ALPHA=0.25
@dataclass
class StepResult:
    t:int; C:float; H:float; phi:float; state:List[float]

def toroidal_map(x: Dict[str, Any]) -> List[float]:
    payload=json.dumps(x,sort_keys=True).encode(); d=hashlib.sha256(payload).digest(); return [int.from_bytes(d[i:i+4],'big')/2**32 for i in range(0,28,4)]

def entropy_milli(data: List[int])->float:
    if not data:return 0.0
    unique=len(set(data)); transitions=sum(1 for i in range(1,len(data)) if data[i]!=data[i-1])
    return unique*6000/256 + transitions*2000/max(1,len(data)-1)

def sha(path:Path)->str:
    h=hashlib.sha256(); h.update(path.read_bytes()); return h.hexdigest()

def run_sequence(inp:Dict[str,Any],steps:int)->Dict[str,Any]:
    data=inp.get('dados',[])
    H_in=min(1.0,entropy_milli(data)/8000.0); C_in=float(inp.get('coerencia_in',0.7)); C=float(inp.get('coerencia0',0.5)); H=float(inp.get('entropia0',0.5))
    series=[]; x_state={"dados":data,"entropia":H,"hash":hashlib.sha256(bytes([d%256 for d in data])).hexdigest(),"estado":inp.get('estado','ACTIVE')}
    for t in range(steps):
        C=(1-ALPHA)*C+ALPHA*C_in; H=(1-ALPHA)*H+ALPHA*H_in; phi=(1-H)*C; x_state['entropia']=H; series.append(StepResult(t+1,C,H,phi,toroidal_map(x_state)))
    last=series[-1]; x=0.314159; seq=[]
    for _ in range(84): x=(math.sqrt(3)/2)*x-math.pi*math.sin(math.radians(279)); seq.append(round(x%1.0,12))
    return {"alpha":ALPHA,"input_entropy":H_in,"input_coherence":C_in,"steps":[asdict(s) for s in series],"final":asdict(last),"falsifiability":{"attractor_cardinality_target":42,"cycle_42_verified":seq[:42]==seq[42:],"pi_max_constraint_ok":last.H<=0.9,"non_void_constraint_ok":x_state['estado']!='VOID'}}

def main()->None:
    p=argparse.ArgumentParser(); p.add_argument('--input',required=True); p.add_argument('--output',required=True); p.add_argument('--steps',type=int,default=42); p.add_argument('--pipeline-name',default='iml_pipeline'); p.add_argument('--version',default='1.0.0'); args=p.parse_args()
    inp=Path(args.input); out=Path(args.output); out.parent.mkdir(parents=True,exist_ok=True)
    result=run_sequence(json.loads(inp.read_text(encoding='utf-8')),args.steps)
    out.write_text(json.dumps(result,indent=2,ensure_ascii=False),encoding='utf-8')
    run_utc=dt.datetime.utcnow().isoformat()+'Z'; input_sha=sha(inp)
    (out.parent/'INPUT_SHA256.txt').write_text(f"{input_sha}  {inp}\n",encoding='utf-8')
    manifest={"run_utc":run_utc,"input_path":str(inp),"input_sha256":input_sha,"steps_requested":args.steps,"pipeline_name":args.pipeline_name,"version":args.version,"custody":{"method":"sha256 file custody","limitations":"integrity only; does not validate scientific adequacy"},"output_json":str(out)}
    (out.parent/'IML_MANIFEST.json').write_text(json.dumps(manifest,indent=2,ensure_ascii=False),encoding='utf-8')
    (out.parent/'IML_REPORT.md').write_text("\n".join(["# IML_REPORT",f"- run_utc: `{run_utc}`",f"- input_path: `{inp}`",f"- input_sha256: `{input_sha}`",f"- steps_requested: `{args.steps}`",f"- pipeline_name: `{args.pipeline_name}`",f"- version: `{args.version}`","- custody.method: `sha256 file custody`","- custody.limitations: `integrity only; no scientific endorsement`"]),encoding='utf-8')
if __name__=='__main__': main()
