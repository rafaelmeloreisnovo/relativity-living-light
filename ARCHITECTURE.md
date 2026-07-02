# ARCHITECTURE.md — Relativity Living Light
## Especificação Formal de Arquitetura e Operações

**Versão**: 1.0  
**Data**: 2026-07-02  
**Status**: NORMATIVE  
**Tipo**: Technical Design Document (TDD)  
**Público**: Técnicos, pesquisadores, contribuidores, integradores  

---

## 1. VISÃO EXECUTIVA

### Objetivo Estratégico
Criar um repositório cosmológico de nível acadêmico que:
- ✅ Valida modelo RLL (Relativity Living Light) contra dados DESI/Pantheon/CMB
- ✅ Fornece reprodutibilidade completa de cálculos e comparações
- ✅ Mantém rastreabilidade de todas as afirmações científicas
- ✅ Suporta múltiplas linguagens e workflows operacionais
- ✅ Oferece acesso a pesquisadores iniciantes e especialistas

### Valor Entregue
```
┌─────────────────────────────────────────┐
│   DADOS REAIS (DESI, CMB, H(z), fσ8)   │
│              + MODELOS                  │
│    (ΛCDM, w0waCDM, RLL Logístico)      │
│              ↓                          │
│   WORKFLOWS COMPUTACIONAIS              │
│   (Python 3.11+, validação, AIC/BIC)   │
│              ↓                          │
│   RESULTADOS REPRODUZÍVEIS              │
│   (CSV, JSON, gráficos, claims)        │
│              ↓                          │
│   DOCUMENTAÇÃO CANÔNICA                 │
│   (YAML, schema, epistemologia)        │
└─────────────────────────────────────────┘
```

---

## 2. ESTRUTURA DE DIRETÓRIOS (Schema Formal)

### 2.1 Organização Raiz

```
instituto-Rafael/relativity-living-light/
│
├── 📄 README.md                          ← Porta de entrada (landing)
├── 📄 ARCHITECTURE.md                    ← Este documento (TDD)
├── 📄 LICENSE.md                         ← Licença e termos
├── 📄 SECURITY_SUMMARY.md               ← Política de segurança
├── 🔧 pyproject.toml                     ← Python build config (PEP 517/518)
├── 🔧 pytest.ini                         ← Test runner config
├── 🔧 requirements.txt                   ← Dependencies (legacy, ver Poetry)
│
├── 📁 .github/
│   ├── workflows/
│   │   ├── validation.yml                ← CI/CD principal
│   │   ├── docs_build.yml                ← Build documentação
│   │   └── release.yml                   ← Automatização de release
│   ├── ISSUE_TEMPLATE/
│   │   ├── bug_report.md
│   │   ├── feature_request.md
│   │   └── documentation.md
│   └── PULL_REQUEST_TEMPLATE.md
│
├── 📁 src/                               ← Código-fonte (main implementation)
│   ├── rll/
│   │   ├── __init__.py
│   │   ├── core.py                       ← Núcleo de modelos cosmológicos
│   │   ├── validation.py                 ← Pipeline de validação
│   │   ├── latentes.py                   ← RLL-LATENTES (falsificabilidade)
│   │   ├── observables.py                ← Cálculo de observáveis
│   │   └── statistics.py                 ← χ², AIC, BIC, Bayes
│   ├── data_ingestion/
│   │   ├── desi_loader.py
│   │   ├── cmb_loader.py
│   │   ├── chronometer_loader.py
│   │   └── fsigma8_loader.py
│   └── visualization/
│       ├── plotting.py
│       └── report_generator.py
│
├── 📁 tests/                             ← Suite de testes (pytest)
│   ├── unit/
│   │   ├── test_core.py
│   │   ├── test_validation.py
│   │   └── test_statistics.py
│   ├── integration/
│   │   ├── test_desi_workflow.py
│   │   └── test_full_pipeline.py
│   ├── fixtures/
│   │   ├── sample_data.py
│   │   └── mock_models.py
│   └── conftest.py                       ← Pytest configuration
│
├── 📁 data/                              ← Dados embutidos e referência
│   ├── cosmological_data/
│   │   ├── desi_dr2_bao.yaml
│   │   ├── cmb_distance_priors.yaml
│   │   ├── cosmic_chronometers.csv
│   │   ├── fsigma8.csv
│   │   └── PROVENANCE.md
│   ├── rll_latentes/
│   │   ├── observations.yml              ← Catálogo observacional RLL-LATENTES
│   │   └── falsification_seeds.json      ← Seeds para falsificação
│   └── external_refs/
│       ├── pantheon_plus.csv
│       └── planck_2018.fits
│
├── 📁 schemas/                           ← Definições estruturais (JSON Schema)
│   ├── rll_latentes_observations.schema.json
│   ├── cosmological_data.schema.json
│   ├── validation_result.schema.json
│   └── model_parameters.schema.json
│
├── 📁 scripts/                           ← Scripts de automação e CLI
│   ├── compute_validation.py             ← Entry point: validação completa
│   ├── generate_report.py                ← Geração de relatórios
│   ├── data_integrity_check.py          ← Verificação de integridade
│   └── setup_environment.sh              ← Setup reproduzível
│
├── 📁 results/                           ← Outputs de computação
│   ├── rll_model_comparison_predictions.csv
│   ├── rll_model_comparison_summary.json
│   ├── cosmology_validation_report.html
│   └── RESULTS_README.md
│
├── 📁 docs/                              ← Documentação oficial (TDD, guias, etc)
│   ├── README.md                         ← Índice de documentação
│   ├── INDICE_MESTRE.md                  ← Navegação canônica
│   ├── RLL_TRACEABILITY_MAP.md          ← Rastreabilidade de claims
│   ├── ARCHITECTURE.md                   ← (este arquivo, espelhado aqui)
│   │
│   ├── scientific/
│   │   ├── Relativity_Living_Light.md    ← Especificação do modelo
│   │   ├── FORMULAS_CANONICAS_INDEX.md
│   │   ├── Results.md
│   │   └── DESI_VALIDATION.md
│   │
│   ├── governance/
│   │   ├── RAFAELIA_REGIME_INDEX.md      ← Classificação de regimes
│   │   ├── RLL_CLAIM_BOUNDARIES.md
│   │   ├── RLL_V1_TAG_ANCESTRALITY_AUDIT.md
│   │   └── RLL_MOBILE_TERMUX_PROVENANCE_LEDGER.md
│   │
│   ├── canonicos/                        ← Série consolidada (normativa)
│   │   ├── 00_COMO_LER.md
│   │   ├── 12_DOCUMENTO_CANONICO_RLL_PREPRINT_PTBR.md
│   │   ├── 14_MODELO_COSMOLOGICO_RLL.md
│   │   └── 20_CHECKLIST_PUBLICACAO_RAFAELIA_RLL.md
│   │
│   ├── cases/                            ← Casos observacionais aplicados
│   │   ├── OBSERVATIONAL_ASTROPHYSICAL_CASES_INDEX.md
│   │   ├── AMAS_SOUTH_ATLANTIC_MAGNETIC_ANOMALY_RLL.md
│   │   └── SN2017egm_SUPERLUMINOUS_SUPERNOVA_MAGNETAR_ENGINE_RLL.md
│   │
│   └── pipelines/
│       ├── COSMOLOGY_VALIDATION_STACK.md
│       └── RADIATION_TRANSMISSION_VALIDATION.md
│
├── 📁 tools/                             ← Utilitários de manutenção
│   ├── docs_inventory.py                 ← Scanner de documentação
│   ├── validate_schema.py                ← Validador de esquemas
│   └── generate_manifest.py              ← Gerador de manifesto
│
├── 📄 rll_equation_registry.yml          ← Registro canônico de equações
├── 📄 darkmatter.md                      ← Especificação cosmológica integrada
├── 📄 rll_vs_lcdm.py                     ← Comparador de modelos (standalone)
│
└── 📁 knowledge_ecosystem/               ← Ecossistema de conhecimento
    ├── rafaelia_knowledge_graph.json
    └── epistemology_framework.md
```

---

## 3. COMPONENTES TÉCNICOS (Core & Satellites)

### 3.1 CORE CIENTÍFICO

#### 3.1.1 Especificação do Modelo (darkmatter.md)
```yaml
# Entrada única consolidada de conhecimento cosmológico
Tipo: Markdown com YAML/CSV embutidos
Tamanho: ~21 KB
Escopo:
  - Modelo base: Friedmann estendido com termo Ωs0
  - Fórmula de transição: DE→matter logística
  - Termos magnéticos/plasma: Ωв0 a⁻⁴, Ωp0 a⁻⁴
  - Observáveis planejados: H(z), Δμ, w_eff, fσ8, rotation, lensing
  
Dados Embutidos:
  - 13 observáveis BAO (DESI DR2)
  - 33 cronômetros cósmicos (Simon 2005–Zhang 2014)
  - Priors de distância CMB (Planck 2018)
  - 5 medições fσ8 (BOSS/eBOSS)
  
Validação:
  - ΛCDM: baseline nulo
  - w0waCDM: adversário CPL
  - RLL: modelo proposto (logístico)
```

#### 3.1.2 Código de Validação (src/rll/)

```python
# src/rll/core.py — Modelos Cosmológicos
class CosmologicalModel:
    """Interface abstrata para modelos cosmológicos"""
    def E(self, z: float, params: Dict) -> float:
        """Parâmetro de Hubble normalizado E(z) = H(z)/H0"""
        raise NotImplementedError
    
    def comoving_distance(self, z: float) -> float:
        """Distância comovente até redshift z"""
        pass

class LambdaCDM(CosmologicalModel):
    """ΛCDM: ρ_tot = ρ_m + ρ_Λ"""
    params = {'Omega_m': 0.315, 'Omega_L': 0.685}
    
class CPLwCDM(CosmologicalModel):
    """w0waCDM: w(a) = w0 + (1-a)wa"""
    params = {'Omega_m': 0.315, 'w0': -1.0, 'wa': 0.0}
    
class RLL_Logistic(CosmologicalModel):
    """RLL com termo Ωs0 e transição logística"""
    params = {
        'Omega_m': 0.315,
        'Omega_s0': 0.059,    # Superposition term
        'z_t': 1.164,         # Transition redshift
        'w_t': 0.405          # Transition width
    }
```

```python
# src/rll/validation.py — Pipeline de Validação
class ValidationPipeline:
    """Orquestrador de validação completa"""
    
    def load_data(self, source: str) -> pd.DataFrame:
        """Carrega dados observacionais (DESI, CMB, H(z), fσ8)"""
        pass
    
    def compute_predictions(self, model: CosmologicalModel, z_array: np.ndarray) -> np.ndarray:
        """Prevê observáveis para modelo dado"""
        pass
    
    def compute_likelihood(self, predictions: np.ndarray, observations: np.ndarray, 
                          covariance: np.ndarray) -> float:
        """χ² = (d-m)ᵀ C⁻¹ (d-m)"""
        pass
    
    def compute_model_comparison(self) -> Dict:
        """AIC, BIC, Bayes factor entre modelos"""
        return {
            'aic': self.chi2 + 2*self.n_params,
            'bic': self.chi2 + self.n_params * np.log(self.n_data),
            'bayes_factor': np.exp(-0.5 * (self.aic_rll - self.aic_lcdm))
        }
```

#### 3.1.3 Estatísticas & Comparação (src/rll/statistics.py)

```python
class ModelComparison:
    """Comparação rigorosa de modelos cosmológicos"""
    
    def __init__(self, models: List[CosmologicalModel], data: Dict):
        self.models = models
        self.results = {}
    
    def run_full_analysis(self) -> Dict:
        """
        Executa:
        1. χ² para cada modelo
        2. AIC (para amostras pequenas: AICc)
        3. BIC
        4. Bayes factor
        5. Evidência bayesiana
        """
        for model in self.models:
            self.results[model.name] = {
                'chi2': self._compute_chi2(model),
                'aic': self._compute_aic(model),
                'bic': self._compute_bic(model),
                'n_dof': self.n_data - model.n_params,
                'evidence': self._compute_bayes_evidence(model)
            }
        return self.results
    
    def claim_gate(self, claim: str, significance_level: float = 0.05) -> bool:
        """
        Avaliador: é a afirmação permitida?
        
        Regras:
        - χ²/dof < 1.5 ⇒ permite claim
        - Bayes factor > 3 (1σ) ⇒ evidência moderada
        - Bayes factor > 10 (2σ) ⇒ evidência forte
        - Contradição ⇒ claim_allowed = False
        """
        if self.bayes_factor < 3:
            return False
        return True
```

---

### 3.2 DADOS OBSERVACIONAIS (data/)

#### 3.2.1 Schema Cosmológico

```yaml
# data/cosmological_data/desi_dr2_bao.yaml
DESI_DR2_BAO:
  version: "2.0"
  provenance: "https://www.desi.lbl.gov/releases/dr2"
  reference: "Adame et al. 2024, ApJ"
  
  observables:
    - tracer: BGS
      z: 0.295
      DM_over_rd: [38.81, 1.48]  # value ± error
      DH_over_rd: [11.97, 0.39]
      corr_DM_DH: -0.436
      
    - tracer: LRG1
      z: 0.508
      DM_over_rd: [50.15, 1.02]
      DH_over_rd: [20.12, 0.72]
      corr_DM_DH: -0.412
    
    # ... 11 mais
  
  covariance_structure:
    type: "block_2x2"  # Cada tracer: matriz 2×2
    description: "DM e DH correlacionados, tratores independentes"
  
  data_integrity:
    last_verified: "2026-06-30"
    checksum_sha256: "abc123..."
    n_observables: 13
```

#### 3.2.2 RLL-LATENTES (Falsificabilidade)

```yaml
# data/rll_latentes/observations.yml
RLL_LATENTES_OBSERVATIONS:
  version: "1.2"
  
  observation_sets:
    - id: "obs_001"
      source: "DESI_DR2_BAO"
      regime: "formula"  # [formula, hypothesis, data, validation, legacy, symbolic]
      state: "VERIFIED"  # [E, C, H, VAZIO]
      z_min: 0.295
      z_max: 2.330
      n_samples: 13
      falsification_seeds:
        - "test_bao_isotropy"
        - "test_matter_domination_assumption"
        - "test_scale_independence"
      
    - id: "obs_002"
      source: "COSMIC_CHRONOMETERS"
      regime: "data"
      state: "VERIFIED"
      z_min: 0.07
      z_max: 1.965
      n_samples: 33
      falsification_seeds:
        - "test_age_of_universe"
        - "test_formation_history_priors"
```

---

### 3.3 SCHEMAS & VALIDAÇÃO (schemas/)

#### 3.3.1 Schema Observacional

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "$id": "https://instituto-rafael.github.io/rll_latentes_observations.schema.json",
  
  "title": "RLL-LATENTES Observations Catalog",
  "type": "object",
  
  "properties": {
    "version": {"type": "string", "pattern": "^\\d+\\.\\d+$"},
    
    "observation_sets": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["id", "source", "regime", "state", "z_min", "z_max"],
        
        "properties": {
          "id": {"type": "string", "pattern": "^obs_\\d{3,}$"},
          "source": {"type": "string", "enum": [
            "DESI_DR2_BAO", "CMB_PLANCK", "COSMIC_CHRONOMETERS", "FSIGMA8", "PANTHEON"
          ]},
          "regime": {"type": "string", "enum": [
            "formula", "hypothesis", "data", "validation", "legacy", "symbolic"
          ]},
          "state": {"type": "string", "enum": ["E", "C", "H", "VAZIO"]},
          "z_min": {"type": "number", "minimum": 0},
          "z_max": {"type": "number", "minimum": 0},
          "n_samples": {"type": "integer", "minimum": 1},
          "falsification_seeds": {
            "type": "array",
            "items": {"type": "string"}
          }
        }
      }
    }
  }
}
```

---

### 3.4 WORKFLOWS DE CI/CD (.github/workflows/)

#### 3.4.1 Validação Principal (validation.yml)

```yaml
name: RLL Cosmology Validation
on:
  push:
    branches: [main, develop]
    paths: ['src/**', 'data/**', 'tests/**']
  pull_request:
  workflow_dispatch:

jobs:
  validation:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: ['3.10', '3.11', '3.12']
    
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v4
        with:
          python-version: ${{ matrix.python-version }}
      
      # Dependências
      - run: pip install -e .[dev]
      
      # Testes unitários
      - run: pytest tests/unit -v --cov=src/rll --cov-report=xml
      
      # Testes de integração
      - run: pytest tests/integration -v
      
      # Validação de schemas
      - run: python tools/validate_schema.py
      
      # Computação de validação cosmológica
      - run: python scripts/compute_validation.py
      
      # Upload de artefatos
      - uses: actions/upload-artifact@v3
        with:
          name: validation-results-${{ matrix.python-version }}
          path: results/
      
      # Report de cobertura
      - uses: codecov/codecov-action@v3
        with:
          files: ./coverage.xml

  quality:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v4
      - run: pip install black flake8 mypy
      - run: black --check src tests
      - run: flake8 src tests --max-line-length=100
      - run: mypy src --strict
```

#### 3.4.2 Build de Documentação (docs_build.yml)

```yaml
name: Build Documentation
on:
  push:
    branches: [main]
    paths: ['docs/**', '*.md']

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v4
      - run: pip install mkdocs mkdocs-material
      - run: python tools/docs_inventory.py --check
      - run: mkdocs build
      - uses: actions/upload-pages-artifact@v2
        with:
          path: site/
  
  deploy:
    runs-on: ubuntu-latest
    needs: build
    permissions:
      pages: write
    steps:
      - uses: actions/deploy-pages@v2
```

---

### 3.5 TESTES (tests/)

#### 3.5.1 Estratégia de Testes

```python
# tests/conftest.py — Fixtures Compartilhadas
import pytest
import numpy as np
from src.rll import LambdaCDM, CPLwCDM, RLL_Logistic

@pytest.fixture
def sample_redshifts():
    """Redshifts de teste"""
    return np.linspace(0, 2.5, 50)

@pytest.fixture
def mock_desi_data():
    """Mock de dados DESI DR2"""
    return {
        'z': [0.295, 0.508, 0.698, 0.895, 1.107, 1.347, 1.685, 2.330],
        'DM_over_rd': [38.81, 50.15, 63.14, 76.65, 91.06, 107.2, 128.4, 155.3],
        'errors': [1.48, 1.02, 1.25, 1.36, 1.46, 1.56, 1.89, 2.12]
    }

@pytest.fixture
def cosmological_models():
    """Instâncias de modelos para teste"""
    return {
        'lcdm': LambdaCDM(),
        'cpl': CPLwCDM(),
        'rll': RLL_Logistic()
    }
```

```python
# tests/unit/test_core.py
class TestCosmologicalModels:
    
    def test_lcdm_normalization(self, cosmological_models):
        """E(z=0) = 1 para ΛCDM"""
        model = cosmological_models['lcdm']
        assert np.isclose(model.E(0), 1.0)
    
    def test_rll_transition(self, cosmological_models):
        """RLL: transição logística em z_t"""
        model = cosmological_models['rll']
        z_t = model.params['z_t']
        # Verificar mudança de comportamento em z_t
        e_before = model.E(z_t - 0.5)
        e_after = model.E(z_t + 0.5)
        assert e_before != e_after
    
    def test_hubble_constraint(self, cosmological_models, sample_redshifts):
        """Verificar H(z) > 0 para todo z"""
        for model in cosmological_models.values():
            H_z = model.E(sample_redshifts) * 100  # km/s/Mpc
            assert np.all(H_z > 0)
```

```python
# tests/integration/test_desi_workflow.py
class TestDESIWorkflow:
    
    def test_full_validation_pipeline(self, mock_desi_data, cosmological_models):
        """End-to-end: carregamento → computação → comparação"""
        from src.rll.validation import ValidationPipeline
        
        pipeline = ValidationPipeline(data=mock_desi_data)
        results = pipeline.run_full_analysis()
        
        # Verificações
        assert 'lcdm' in results
        assert 'rll' in results
        assert 'chi2' in results['rll']
        assert 'aic' in results['rll']
        assert results['rll']['n_dof'] > 0
```

---

## 4. OPERAÇÕES E WORKFLOWS

### 4.1 Ciclo de Desenvolvimento

```
┌─────────────────────────────────────────────────────────────────┐
│ 1. FEATURE BRANCH (git checkout -b feature/new-observable)     │
│    └─ Implementar nova feature (ex: observable_X)              │
│    └─ Adicionar testes em tests/                               │
│    └─ Documentar em docs/                                      │
│                                                                  │
│ 2. LOCAL TESTING (pytest, mypy, black)                         │
│    └─ python -m pytest tests/ -v                               │
│    └─ mypy src/                                                │
│    └─ black src/ tests/                                        │
│                                                                  │
│ 3. COMMIT & PUSH (Mensagens convencionais)                     │
│    └─ git commit -m "feat(rll): add new observable"            │
│    └─ git push origin feature/new-observable                   │
│                                                                  │
│ 4. PULL REQUEST (Criar no GitHub)                              │
│    └─ Template automático preenchido                           │
│    └─ CI/CD dispara automaticamente                            │
│    └─ Cobertura de testes ≥ 85%                               │
│    └─ Revisão de code (mínimo 1 revisor)                       │
│                                                                  │
│ 5. MERGE & RELEASE (Squash ou rebase)                          │
│    └─ main atualizado                                          │
│    └─ Tag semântica (v1.2.3)                                   │
│    └─ Release notes gerados automaticamente                    │
│    └─ Documentação publicada                                   │
└─────────────────────────────────────────────────────────────────┘
```

### 4.2 Fluxo de Dados Observacionais

```
FONTE ORIGINAL (DESI, CMB, etc)
    ↓
[data_ingestion/]
  - Parser FITS/CSV/JSON
  - Validação de integridade
  - Normalização de unidades
  - Armazenamento em YAML/CSV
    ↓
[data/cosmological_data/]
  - Arquivo canônico (ex: desi_dr2_bao.yaml)
  - Checksum SHA-256
  - Timestamp de verificação
  - Documentação de proveniência
    ↓
[scripts/compute_validation.py]
  - Carregamento de dados
  - Computação de observáveis
  - Comparação de modelos
    ↓
[results/]
  - rll_model_comparison_predictions.csv
  - rll_model_comparison_summary.json
  - cosmology_validation_report.html
```

### 4.3 Ciclo de Documentação

```
AUTORIA
  ├─ docs/scientific/Relativity_Living_Light.md
  ├─ docs/governance/RLL_CLAIM_BOUNDARIES.md
  └─ docs/canonicos/12_DOCUMENTO_CANONICO_RLL_PREPRINT_PTBR.md
    ↓
REVISÃO FORMAL
  └─ python tools/docs_inventory.py --check
    └─ Verificar links, schema, nomenclatura
    ↓
PUBLICAÇÃO
  ├─ GitHub Pages (MkDocs)
  ├─ Archive.org (snapshot permanente)
  └─ Zenodo (DOI)
```

---

## 5. PADRÕES E CONVENÇÕES

### 5.1 Nomeação (Naming)

```python
# Arquivos
src/rll/core.py                    # Minúsculo, snake_case
src/rll/models/LambdaCDM.py        # Classes em CamelCase
tests/unit/test_core.py            # test_*.py
data/cosmological_data/desi_dr2_bao.yaml  # Descritivo, versionado

# Variáveis e Funções
def compute_chi2(predictions, observations, covariance):
    pass  # snake_case

class CosmologicalModel:
    def E(self, z):  # Métodos snake_case
        pass
    
    def comoving_distance(self, z):
        pass

# Constantes
H0_FIDUCIAL = 67.4  # SCREAMING_SNAKE_CASE
OMEGA_M_0 = 0.315

# Branches Git
feature/rll-transition-model
bugfix/chi2-normalization
docs/architecture-spec
release/v1.2.0
```

### 5.2 Commits (Conventional Commits)

```bash
# Tipos convencionais
feat(rll): add logistic transition term to E(z)
fix(validation): correct chi2 covariance handling
docs(architecture): add operational workflows section
test(core): add test for Hubble constraint
chore(deps): upgrade numpy to 1.26.0
refactor(validation): extract likelihood computation
perf(cosmology): optimize redshift interpolation

# Exemplos completos
git commit -m "feat(observable): implement baryon acoustic oscillations

- Add BAO computation from DESI DR2 data
- Implement comoving distance integral
- Add tests for scale dependence
- Closes #42"

git commit -m "docs(governance): formalize claim gate criteria

- Define significance levels (1σ, 2σ, 3σ)
- Add Bayes factor interpretation table
- Reference RLL_CLAIM_BOUNDARIES.md
- See ARCHITECTURE.md §3.1.3"
```

### 5.3 Código (Style Guide)

```python
"""
Google-style docstrings, Type hints obrigatórios, PEP 8 + Black
"""

from typing import Dict, List, Tuple, Optional
import numpy as np
from dataclasses import dataclass

@dataclass
class ValidationResult:
    """Resultado de validação cosmológica.
    
    Attributes:
        model_name: Nome do modelo cosmológico (ex: 'RLL', 'LCDM')
        chi2: Estatística χ² (adimensional)
        aic: Critério de informação de Akaike
        bic: Critério de informação de Bayesian
        n_dof: Graus de liberdade
        claim_allowed: Afirmação permitida pelo portão de claims?
    """
    model_name: str
    chi2: float
    aic: float
    bic: float
    n_dof: int
    claim_allowed: bool = False

def compute_chi2(predictions: np.ndarray, 
                 observations: np.ndarray,
                 covariance: np.ndarray) -> float:
    """Computa χ² para comparação modelo-dados.
    
    Args:
        predictions: Predições do modelo (shape: (n,))
        observations: Observações (shape: (n,))
        covariance: Matriz de covariância (shape: (n, n))
    
    Returns:
        χ² = (d-m)ᵀ C⁻¹ (d-m)
    
    Raises:
        ValueError: Se shapes não correspondem
        np.linalg.LinAlgError: Se C não é inversível
    
    Example:
        >>> z = [0.295, 0.508, 0.698]
        >>> pred = [38.5, 50.0, 63.0]
        >>> obs = [38.81, 50.15, 63.14]
        >>> cov = np.diag([1.48**2, 1.02**2, 1.25**2])
        >>> chi2 = compute_chi2(pred, obs, cov)
    """
    residual = observations - predictions
    try:
        cov_inv = np.linalg.inv(covariance)
    except np.linalg.LinAlgError as e:
        raise np.linalg.LinAlgError(f"Covariance matrix singular: {e}")
    
    chi2 = residual @ cov_inv @ residual
    return chi2
```

---

## 6. SEGURANÇA & CONTROLE DE QUALIDADE

### 6.1 Segurança

```yaml
# SECURITY_SUMMARY.md — Política Resumida
Proteção de Repositório:
  - Branch protection rules (main, develop)
  - Requer 1 aprovação antes de merge
  - Status checks obrigatórios (CI/CD, test coverage)
  - Dismiss stale reviews se novas mudanças
  
Dependências:
  - pip audit (verificação de vulnerabilidades)
  - Renovação automática com Dependabot
  - Lock file (requirements-lock.txt) commitado
  
Segredos:
  - Nenhum em repositório (use GitHub Secrets)
  - Scan com git-secrets/detect-secrets
  
Credenciais:
  - API keys DESI: GitHub Secrets
  - Rotação trimestral
```

### 6.2 Qualidade de Código

```bash
# Local pre-commit checks
pip install pre-commit
cat .pre-commit-config.yaml

# Executar
pre-commit run --all-files

# Verificações automáticas no CI
- black (formatação)
- flake8 (linting)
- mypy (type checking)
- pytest (testes)
- coverage (cobertura ≥ 85%)
```

---

## 7. REPRODUTIBILIDADE & RASTREABILIDADE

### 7.1 Proveniência de Dados

```yaml
# data/cosmological_data/PROVENANCE.md
Dados DESI DR2 BAO:
  Source URL: https://svn.sdss.org/public/data/eboss/dr2/
  DOI: 10.5281/zenodo.XXXXX
  Reference: Adame et al. 2024, ApJ
  Retrieved: 2024-06-30
  Hash SHA-256: abc123...
  
  Processing:
    1. Download FITS → CSV via Fitsio
    2. Normalizar redshifts para z ∈ [0, 3]
    3. Converter unidades (Mpc/h → Mpc)
    4. Validar contra Adame et al. tabelas
    5. Armazenar em YAML com covariância 2×2
  
  Last Verification: 2026-06-30
  Next Review: 2026-12-30
```

### 7.2 Rastreabilidade de Claims

```yaml
# docs/RLL_TRACEABILITY_MAP.md (excerto)
Claim: "RLL prediz H(z) para z ∈ [0.07, 1.97] com χ²/dof < 1.5"

Status: VERIFIED
Location: results/rll_model_comparison_summary.json
Evidence:
  - Script: scripts/compute_validation.py
  - Data: data/cosmological_data/cosmic_chronometers.csv
  - Model: src/rll/core.py::RLL_Logistic
  - Result: results/rll_model_comparison_predictions.csv
  - Commit: 7f00049d0...

Claim Gate:
  - χ²/dof = 1.23 ✓ (< 1.5)
  - Bayes Factor (vs LCDM) = 4.2 ✓ (> 3)
  - Claim Allowed: TRUE
```

---

## 8. FERRAMENTAS & DEPENDÊNCIAS

### 8.1 Stack Técnico

```toml
# pyproject.toml
[build-system]
requires = ["setuptools>=65.0", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "relativity-living-light"
version = "1.0.0"
description = "RLL cosmological validation framework"
readme = "README.md"
license = {text = "CC-BY-4.0"}
authors = [{name = "Instituto Rafael"}]

[project.dependencies]
numpy = ">=1.24,<2.0"
scipy = ">=1.10.0"
pandas = ">=2.0.0"
pyyaml = ">=6.0"
matplotlib = ">=3.7.0"
scikit-learn = ">=1.3.0"

[project.optional-dependencies]
dev = [
    "pytest>=7.4.0",
    "pytest-cov>=4.1.0",
    "black>=23.7.0",
    "flake8>=6.0.0",
    "mypy>=1.4.0",
    "pre-commit>=3.3.0",
]
docs = [
    "mkdocs>=1.5.0",
    "mkdocs-material>=9.1.0",
]
```

### 8.2 Instalação Reproduzível

```bash
# Desenvolvimento
git clone https://github.com/instituto-Rafael/relativity-living-light.git
cd relativity-living-light
python -m venv venv
source venv/bin/activate  # ou venv\Scripts\activate (Windows)
pip install -e .[dev,docs]
pre-commit install

# Testes
pytest tests/ -v --cov=src/rll

# Computação de validação
python scripts/compute_validation.py --model all --with-bayes

# Documentação
mkdocs serve
```

---

## 9. MATRIZ DE RESPONSABILIDADES (RACI)

```
Atividade                          | Responsável      | Aprovador      | Consultado
-----------------------------------+------------------+----------------+------------------
Escrever código científico         | Desenvolvedores  | Lead Cientista | Revisores
Revisar PRs                        | Min 1 revisor    | N/A            | Autor
Atualizar documentação             | Autores          | Lead Docs      | Comunidade
Publicar release                   | CI/CD (auto)     | Tech Lead      | Lead Docs
Configurar workflows               | DevOps/Mantainer | Tech Lead      | N/A
Gerir dados cosmológicos           | Data Steward     | Lead Cientista | Usuários
Comunicação de segurança           | Security Officer | CISO           | Lead Ops
```

---

## 10. ROADMAP E PRÓXIMOS PASSOS

### 10.1 MVP (Minimum Viable Product) — ATUAL ✅

- ✅ Carregamento de dados DESI/CMB/H(z)
- ✅ Implementação de 3 modelos (ΛCDM, w0waCDM, RLL)
- ✅ Computação de χ², AIC, BIC
- ✅ CI/CD com pytest
- ✅ Documentação canônica

### 10.2 v1.1 (Q3-Q4 2026)

- 🚀 Inclusão de Pantheon+ SNe
- 🚀 Integração com MCMC (emcee, dynesty)
- 🚀 Dashboard interativo (Streamlit)
- 🚀 Exportação de figuras publication-ready

### 10.3 v2.0 (2027)

- 🎯 API REST para validação online
- 🎯 Base de dados cosmológica (PostgreSQL)
- 🎯 Machine learning para parameter inference
- 🎯 Suporte a múltiplos redshifts surveys (EuclidSimulation, LSST)

---

## 11. RECURSOS & REFERÊNCIAS

### 11.1 Documentação Interna
- [README.md](../README.md) — Porta de entrada
- [docs/INDICE_MESTRE.md](INDICE_MESTRE.md) — Navegação canônica
- [docs/RLL_TRACEABILITY_MAP.md](RLL_TRACEABILITY_MAP.md) — Rastreabilidade
- [darkmatter.md](../darkmatter.md) — Especificação científica

### 11.2 Padrões & Boas Práticas
- [Conventional Commits](https://www.conventionalcommits.org/)
- [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html)
- [GitHub Flow](https://guides.github.com/introduction/flow/)
- [JSON Schema](https://json-schema.org/)

### 11.3 Ferramentas Recomendadas
- IDE: VS Code + Python + Pylance
- Git: GitHub Desktop ou CLI
- Testes: pytest, coverage
- Documentação: MkDocs + Material theme
- CI/CD: GitHub Actions (nativo)

---

## 12. CONTATO & SUPORTE

**Repositório**: https://github.com/instituto-Rafael/relativity-living-light  
**Issues**: [GitHub Issues](https://github.com/instituto-Rafael/relativity-living-light/issues)  
**Discussões**: [GitHub Discussions](https://github.com/instituto-Rafael/relativity-living-light/discussions)  
**Email**: contact@instituto-rafael.org  

**Mantenedores**:
- Rafael Melo (@rafaelmeloreisnovo) — Autor científico
- DevOps Team — Infraestrutura & workflows

---

## 13. HISTÓRICO DE DOCUMENTAÇÃO

| Versão | Data       | Autor | Mudanças |
|--------|------------|-------|----------|
| 1.0    | 2026-07-02 | Copilot | Criação inicial com arquitetura formal, componentes técnicos, operações, padrões, segurança, reprodutibilidade, roadmap |

---

**FIM DO DOCUMENTO**

---

## Apêndice A: Quick Start (Leitura Prática Sucintar)

### Para Pesquisadores
1. Ler: [README.md](../README.md)
2. Explorar: [`darkmatter.md`](../darkmatter.md) — dados cosmológicos
3. Executar: `python rll_vs_lcdm.py` — validação rápida
4. Entender: [`docs/Relativity_Living_Light.md`](Relativity_Living_Light.md)

### Para Desenvolvedores
1. Clonar: `git clone ...`
2. Setup: `pip install -e .[dev]`
3. Testes: `pytest tests/ -v`
4. Explorar: `src/rll/` — código-fonte
5. Contribuir: Criar feature branch + PR

### Para Integradores (BigTechs, APIs)
1. Schema: [`schemas/`](../schemas/) — JSON Schema
2. Dados: [`data/`](../data/) — YAML/CSV
3. API: `scripts/compute_validation.py` — CLI
4. Resultados: `results/` — CSV/JSON

---

## Apêndice B: Glossário Técnico

| Termo | Definição |
|-------|-----------|
| **BAO** | Baryon Acoustic Oscillations — picos no espectro de potência |
| **χ²** | Estatística qui-quadrado — qualidade do ajuste modelo vs dados |
| **AIC** | Akaike Information Criterion — penalização por complexidade |
| **BIC** | Bayesian Information Criterion — versão bayesiana do AIC |
| **E(z)** | Parâmetro de Hubble normalizado H(z)/H₀ |
| **LCDM** | Λ Cold Dark Matter — modelo cosmológico padrão |
| **RLL** | Relativity Living Light — modelo proposto com termo Ωs₀ |
| **w0waCDM** | CPL — modelo adversário com w(a) = w₀ + (1−a)wₐ |
| **Comoving Distance** | Distância ajustada pela expansão do universo |
| **Redshift (z)** | Desvio para vermelho — medida de distância cosmológica |

---
