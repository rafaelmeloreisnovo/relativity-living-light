#!/usr/bin/env python3
"""
Procura por arquivos que parecem conter dados sintéticos / mocks / sample.
- Estratégia:
  - busca por nomes (sample, synthetic, mock, fake, example)
  - busca por strings no conteúdo ('synthetic', 'mock', 'sample', 'simulated', 'faker', 'random.seed')
  - report-only: lista e sai com código 0
  - --replace: faz backup dos arquivos detectados para data/synthetic_backup/ e opcionalmente substitui
"""

import argparse
import os
import re
import shutil
from pathlib import Path

NAME_PATTERNS = re.compile(r'(sample|synthetic|mock|fake|example|demo)', re.I)
CONTENT_PATTERNS = re.compile(r'\b(synthetic|fake|mock|sample|simulated|faker|random\.seed|np\.random|make_classification)\b', re.I)

def find_files(root='.'):
    matches = []
    for p in Path(root).rglob('*'):
        if p.is_file():
            name = p.name
            if NAME_PATTERNS.search(name):
                matches.append(p)
                continue
            try:
                # only read small files or first portion for performance
                with p.open('r', encoding='utf-8', errors='ignore') as f:
                    head = f.read(8192)
                    if CONTENT_PATTERNS.search(head):
                        matches.append(p)
            except Exception:
                continue
    return matches

def backup_and_replace(files, replace_with_path=None):
    backup_dir = Path('data/synthetic_backup')
    backup_dir.mkdir(parents=True, exist_ok=True)
    for f in files:
        dest = backup_dir / f.name
        shutil.copy2(f, dest)
        print(f"Backup: {f} -> {dest}")
        if replace_with_path:
            shutil.copy2(replace_with_path, f)
            print(f"Substituído {f} com {replace_with_path}")

def main():
    p = argparse.ArgumentParser()
    p.add_argument('--root', default='.')
    p.add_argument('--report-only', action='store_true')
    p.add_argument('--replace-with', help='Caminho para arquivo que substituirá arquivos sintéticos (opcional)')
    args = p.parse_args()

    found = find_files(args.root)
    if not found:
        print("Nenhum arquivo sintético identificado.")
    else:
        print("Arquivos possivelmente sintéticos:")
        for f in found:
            print(" -", f)
    if args.report_only:
        return
    if found and (args.replace_with or input("Fazer backup e substituir arquivos detectados? (y/N): ").lower().startswith('y')):
        replace = args.replace_with
        backup_and_replace(found, replace)

if __name__ == '__main__':
    main()
