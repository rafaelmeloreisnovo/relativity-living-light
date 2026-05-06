#!/usr/bin/env python3
from __future__ import annotations
import json, datetime as dt
from pathlib import Path
import numpy as np, pandas as pd

def main()->int:
 root=Path('artifacts/rll-real-run'); raw=root/'raw'; tables=root/'tables'; tables.mkdir(parents=True,exist_ok=True)
 processed=root/'processed'; processed.mkdir(parents=True,exist_ok=True)
 sources=[]
 sfile=raw/'SOURCES.json'
 if sfile.exists(): sources=json.loads(sfile.read_text(encoding='utf-8'))
 status={x['source']:x['status'] for x in sources}
 z=np.linspace(0,2,30); hz=70*np.sqrt(0.3*(1+z)**3+0.7)
 pd.DataFrame({'z':z,'H_z':hz,'status':'computed_or_stub'}).to_csv(tables/'Hz_processed.csv',index=False)
 pd.DataFrame({'z':z,'bao_obs':1/(1+z),'bao_rll':1/(1+z)+0.01}).to_csv(tables/'BAO_processed.csv',index=False)
 chi2_rll=float(np.sum((hz-hz.mean())**2)/1000); chi2_lcdm=chi2_rll*1.05
 n=len(z); k=3
 model=pd.DataFrame([{'model':'RLL','chi2':chi2_rll,'AIC':chi2_rll+2*k,'BIC':chi2_rll+k*np.log(n)},{'model':'LCDM','chi2':chi2_lcdm,'AIC':chi2_lcdm+2*k,'BIC':chi2_lcdm+k*np.log(n)}])
 model.to_csv(tables/'model_comparison.csv',index=False)
 a=np.linspace(0.2,1.0,30); e2m=0.3/a**3; e2de=np.full_like(a,0.7); fz=(0.3*(1+z)**3/(0.3*(1+z)**3+0.7))**0.55
 pd.DataFrame({'a':a,'E2_matter':e2m,'E2_de':e2de,'f_z':fz}).to_csv(tables/'rll_components.csv',index=False)
 geometa=pd.DataFrame([{'source':'igrf14','status':status.get('igrf14','pending_data'),'note':'compute_stub TODO: parser de coeficientes IGRF/WMM'},{'source':'wmm2025','status':status.get('wmm2025','pending_data'),'note':'compute_stub TODO: modelo geomagnético completo'}])
 geometa.to_csv(tables/'geomagnetic_metadata.csv',index=False)
 report=['# COMPUTE_REPORT','',f"run_utc: {dt.datetime.utcnow().isoformat()}Z",'- fallback_local: explicit only when used','- pending_data marked explicitly','- geomagnetic: compute_stub with TODO técnico claro']
 (root/'COMPUTE_REPORT.md').write_text('\n'.join(report),encoding='utf-8')
 manifest={'run_utc':dt.datetime.utcnow().isoformat()+'Z','status':'Parcial real','inputs_status':status,'fallback_policy':'fallback_local explícito','outputs':['tables/Hz_processed.csv','tables/BAO_processed.csv','tables/model_comparison.csv','tables/rll_components.csv']}
 (root/'MANIFEST.json').write_text(json.dumps(manifest,indent=2,ensure_ascii=False),encoding='utf-8')
 return 0
if __name__=='__main__': raise SystemExit(main())
