# RLL — CI Dependency Failure

**Status:** diagnóstico e correção de falha de coleta de testes no GitHub Actions.  
**Escopo:** ambiente CI; não altera dados reais, fórmulas, resultados canônicos ou claim policy.

---

## 1. Sintoma observado

O workflow falhou durante a coleta do `pytest` com erros como:

```text
ModuleNotFoundError: No module named 'yaml'
ModuleNotFoundError: No module named 'numpy'
ModuleNotFoundError: No module named 'pandas'
```

O log também indicou ambiente Python:

```text
/opt/hostedtoolcache/Python/3.14.5/x64
```

---

## 2. Causa-raiz

O arquivo:

```text
.github/workflows/claim-boundary-quality-gates.yml
```

usava:

```yaml
python-version: "3.x"
```

Isso permitiu que o GitHub Actions escolhesse Python 3.14.x. Além disso, o workflow instalava apenas:

```bash
python -m pip install pytest
```

mas não instalava o pacote do repositório nem suas dependências declaradas em `pyproject.toml`, como:

- `numpy`;
- `pandas`;
- `PyYAML`;
- `scipy`;
- `matplotlib`;
- `jsonschema`;
- `astropy`.

---

## 3. Correção aplicada

O workflow foi ajustado para:

```yaml
python-version: "3.11"
```

e agora instala:

```bash
python -m pip install --upgrade pip
python -m pip install -e .
python -m pip install pytest
```

Isso instala as dependências do projeto antes de rodar:

```bash
python -m pytest -q tests
```

---

## 4. Por que Python 3.11

O workflow `python-tests.yml` já usa Python 3.11. Fixar o claim-boundary gate em 3.11 reduz divergência entre workflows e evita que `3.x` avance para uma versão recém-lançada antes de todos os pacotes científicos estarem garantidos no ambiente.

---

## 5. Boundary preservado

Esta correção:

- não altera `data/real/**`;
- não altera fórmulas cosmológicas;
- não altera parâmetros;
- não altera `results/**`;
- não altera `claim_allowed=false`;
- apenas corrige instalação de dependências no CI.

---

## 6. Estado

```text
F_ok   = workflow corrigido para instalar dependências do projeto e usar Python 3.11.
F_gap  = o novo run do GitHub Actions ainda precisa confirmar PASS.
F_next = se o próximo erro aparecer, classificar se é erro real de teste ou nova lacuna de ambiente.
```
