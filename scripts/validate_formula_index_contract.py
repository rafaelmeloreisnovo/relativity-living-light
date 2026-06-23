#!/usr/bin/env python3
import json
from pathlib import Path

d = json.loads(Path('data/formulas/FORMULA_INDEX_CONTRACT.json').read_text(encoding='utf-8'))
assert d['schema'] == 'rafaelia.formula_index_contract.v1'
assert d['status'] == 'contract_ready'
assert d['expected_verified_counts']['total_formulas'] == 486
assert d['expected_verified_counts']['source_count'] == 53
cats = d['expected_verified_counts']['categories']
assert cats['geral'] == 388
assert cats['cosmology_metrics'] == 91
assert cats['integridade_e_criptografia'] == 7
assert d['category_prefix']['cosmology_metrics'] == 'COS'
assert d['claim_gates']['cosmology_metrics'] == 'GATE_COSMOLOGY_DATA_LOADER_COVARIANCE_CI'
print('formula index contract ok')
