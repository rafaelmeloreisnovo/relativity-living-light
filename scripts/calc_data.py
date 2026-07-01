#!/usr/bin/env python3
"""
Carrega data/raw/data.json (ou CSV) e calcula estatísticas simples.
Gera data/processed/results.json com:
- n registros
- colunas numéricas: mean, median, std, min, max
- pequenas amostras (first/last 5)
"""

import argparse
import json
from pathlib import Path
import pandas as pd
import numpy as np

def load(path):
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(path)
    if p.suffix.lower() in ('.json',):
        # assume list of records
        with p.open('r', encoding='utf-8') as f:
            data = json.load(f)
        df = pd.DataFrame(data)
    else:
        df = pd.read_csv(p)
    return df

def summarize(df):
    numeric = df.select_dtypes(include=[np.number])
    stats = {}
    stats['n_records'] = int(len(df))
    stats['columns'] = {}
    for col in numeric.columns:
        s = numeric[col].dropna()
        stats['columns'][col] = {
            'mean': float(s.mean()) if len(s)>0 else None,
            'median': float(s.median()) if len(s)>0 else None,
            'std': float(s.std()) if len(s)>0 else None,
            'min': float(s.min()) if len(s)>0 else None,
            'max': float(s.max()) if len(s)>0 else None,
            'n_nonnull': int(s.count())
        }
    # samples
    stats['sample_head'] = df.head(5).to_dict(orient='records')
    stats['sample_tail'] = df.tail(5).to_dict(orient='records')
    return stats

def main():
    p = argparse.ArgumentParser()
    p.add_argument('--in', dest='infile', required=True)
    p.add_argument('--out', dest='outfile', required=True)
    args = p.parse_args()
    df = load(args.infile)
    res = summarize(df)
    Path(args.outfile).parent.mkdir(parents=True, exist_ok=True)
    with open(args.outfile, 'w', encoding='utf-8') as f:
        json.dump(res, f, ensure_ascii=False, indent=2)
    print(f"Resultados gravados em {args.outfile}")

if __name__ == '__main__':
    main()
