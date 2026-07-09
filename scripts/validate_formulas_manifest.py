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

supplements = d.get('curated_supplements', {})
rafaelia = supplements.get('RAFAELIA_FORMAL_UNIFIED_CORE.md')
assert rafaelia is not None
assert rafaelia['path'] == 'data/formulas/RAFAELIA_FORMAL_UNIFIED_CORE.md'
assert rafaelia['kind'] == 'curated_formula_supplement'
assert rafaelia['claim_allowed'] is False
assert rafaelia['bytes'] > 0
assert len(rafaelia['sha256']) == 64
assert 'does not validate' in rafaelia['claim_boundary']

print('formulas manifest ok')
