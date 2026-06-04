# 19 — Roadmap e Falsificadores RLL

**Status:** canônico complementar  
**Origem:** extraído de `docs/canonicos/BIBLIA_CONHECIMENTO_RAFAELIA_RLL.md`  
**Função:** transformar caminhos futuros em tarefas públicas verificáveis.

---

## 1. Regra central

Um caminho de validação só é forte se tiver:

```text
claim → dataset → métrica → baseline → falsificador → resultado versionado
```

## 2. Adversário principal

O adversário científico principal do RLL é **w0waCDM**, não apenas ΛCDM.

## 3. Caminhos prioritários

| ID | Domínio | Prioridade | Observável | Dataset/Fonte |
|---|---|---:|---|---|
| C01 | background cosmológico | pré-requisito | f(z) ↔ w(z) | DESI DR2 + Pantheon+ + Planck |
| C03 | matéria escura / estrutura | alta | core→cusp / halo | SIDM sims; DES Y6 |
| C05 | tensão H0 | alta | H0 local vs CMB | SH0ES + Planck + DESI |
| C07 | gravidade alternativa | alta | aceleração sem DE | H(z)+BAO+SNe |
| C09 | fóton/plasma | média | dispersão em plasma | CHIME/FRB |

## 4. Tarefas documentais

- dividir o documento-mãe em módulos canônicos;
- verificar identificadores bibliográficos;
- atualizar `docs/INDICE_MESTRE.md`;
- registrar pendências em checklist;
- manter `BIBLIA_CONHECIMENTO_RAFAELIA_RLL.md` como documento-mãe.

## 5. Tarefas computacionais

- verossimilhança conjunta H(z)+BAO+fσ8+CMB;
- covariância BAO 2×2 por tracer;
- r_d derivado dos parâmetros cosmológicos;
- mapeamento f(z) → w_eff(a) → comparação w0wa;
- relatório automático com hashes e commit.

## 6. Falsificadores mínimos

O RLL perde força se:

- w0waCDM explicar os mesmos resíduos com menor penalidade AIC/BIC;
- a assinatura magnética/plasmática não produzir diferença observável;
- parâmetros RLL exigirem ajuste fino sem ganho preditivo;
- resultados desaparecerem ao usar covariância correta;
- a anterioridade não for comprovável por commit, tag, DOI ou artefato datado.

## 7. Integridade

Resultado desfavorável deve ser preservado. Ciência legítima registra falha, limite e vazio.

---

*Falsificador é aliado: ele protege o que for real.*