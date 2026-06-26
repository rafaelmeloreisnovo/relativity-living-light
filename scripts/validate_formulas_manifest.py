#!/usr/bin/env python3
import json
from pathlib import Path

p = Path('data/formulas/FORMULAS_ARTIFACTS_MANIFEST.json')
d = json.loads(p.read_text(encoding='utf-8'))
assert d['schema'] == 'rafaelia.formulas_artifacts_manifest.v1'
assert d['total_formulas'] == 486
assert d['source_count'] == 53
cats = d['category_counts']
assert cats['geral'] == 388
assert cats['cosmology_metrics'] == 91
assert cats['integridade_e_criptografia'] == 7
files = d['artifact_files']
for k in ['formulas.json', 'formulas.csv', 'FORMULAS_BY_SOURCE.md', 'FORMULAS_CLAIM_MAP.md', 'FORMAL_ACADEMIC_REPORT.md']:
    assert k in files
    assert files[k]['bytes'] > 0
    assert len(files[k]['sha256']) == 64
print('formulas manifest ok')
