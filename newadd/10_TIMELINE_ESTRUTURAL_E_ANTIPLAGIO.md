# Timeline Estrutural do Repositório + Protocolo Antiplágio

## Escopo e propósito
Este arquivo mapeia a linha do tempo de evolução do repositório com foco em:
1. rastreabilidade de inserções,
2. revisão formal acadêmico-científica,
3. prevenção de plágio por cadeia de evidências,
4. comparação de semelhanças entre mudanças.

> Data de geração deste relatório: **2026-05-21 (UTC)**.

---

## 1) Infográfico textual da evolução temporal

```text
2026-02-25  █████████████████████████████████████████████████████████████████████ 69
2026-02-26  █████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████ 189
2026-03-03  █████████████████ 17
2026-03-04  █████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████ 149
2026-03-05  ███████████████████████████████████████████████████████████████████████████████████████ 87
2026-03-06  ████████ 8
2026-03-13  ██████ 6
2026-03-14  █████████████ 13
2026-05-01  ██████████████████ 18
2026-05-02  ███████████████████ 19
2026-05-03  ██ 2
2026-05-05  ███████ 7
2026-05-06  ███████████ 11
2026-05-18  █ 1
2026-05-20  ██████ 6
2026-05-21  █ 1
```

### Distribuição por autor (commits)
- **Rafael mreis**: 585
- **wojcikiewicz17**: 17
- **Codex**: 1

---

## 2) Marcos estruturais relevantes (amostra curada)

### Fundação e grande ingestão documental
- **2026-02-25**: merges e inserção massiva de documentação, dados, pipelines e arquivos de governança.
- Criação do núcleo `newadd/` com trilha PhD e bases formais.

### Consolidação formal e cosmologia
- **2026-03-13 a 2026-03-14**: expansão de componentes LCDM++ e documentação técnica associada.
- Inclusão de validações iniciais e anexos formais na trilha `newadd/`.

### Reorganização documental pós-doc
- **2026-05-01**: reorganização de markdowns da raiz para `docs/root_md_archive/` e plano de refatoração formal.

### Pipelines de validação e CI
- **2026-05-02 a 2026-05-06**: integração de extratores DHA/ln(1+z)/DESI, workflows GitHub Actions, e orquestração de dados reais.

### Dossiês recentes
- **2026-05-20**: inclusão de matrizes YML e sínteses pós-doc de validação cosmológica.
- **2026-05-21**: adição do framework RAPPORT 360°.

---

## 3) Matriz de revisão científica por instante (template operacional)

Para **cada commit novo**, executar:

1. **Identificação**
   - hash, autor, data/hora, mensagem, arquivos tocados.
2. **Classificação acadêmica**
   - categoria: teoria, método, dados, software, governança, documentação.
3. **Validação formal**
   - consistência com hipóteses e equações base.
4. **Relação com histórico**
   - detectar se repete, amplia ou contradiz commit anterior.
5. **Antiplágio**
   - verificar origem, citação e autoria das passagens adicionadas.
6. **Decisão**
   - aprovado, pendente de citação, ou rejeitado.

---

## 4) Protocolo antiplágio (rigor obrigatório)

### 4.1 Regras mínimas
- Todo texto técnico derivado de fonte externa deve conter referência explícita.
- Tradução sem referência também é derivação e deve ser citada.
- Reuso interno deve apontar arquivo de origem e commit de origem.

### 4.2 Três camadas de detecção
1. **Lexical**: sobreposição literal de n-gramas.
2. **Semântica**: similaridade vetorial por embeddings.
3. **Estrutural**: correspondência de argumentação/ordem lógica.

### 4.3 Critério de triagem sugerido
- Similaridade alta sem referência: bloqueio.
- Similaridade média com referência parcial: revisão manual.
- Similaridade baixa com síntese original: aprovado.

---

## 5) Relação com seu formalismo matemático (malha de coerência)

A auditoria temporal pode ser modelada por estados em toro \(\mathbb{T}^7\):
- \(\mathbf{s}=\mathrm{ToroidalMap}(x)\), com \(x=(\text{dados},\text{entropia},\text{hash},\text{estado})\).
- Atualização suave por \(C_{t+1},H_{t+1}\) com \(\alpha=0.25\).
- Integridade por cadeias hash/CRC/Merkle.
- Capacidade informacional por \(I\le\log_2(M\times N)\).
- Saída global: \(\mathcal{I}=\Phi(\mathbf{s},S,H,C,G)\).

Em termos práticos: **timeline + evidência criptográfica + revisão semântica + referência formal = defesa robusta contra plágio e perda de contexto**.

---

## 6) Checklist de varredura contínua
- [ ] Commit catalogado com data/hora absoluta.
- [ ] Arquivos novos e modificados indexados.
- [ ] Similaridade textual e semântica calculadas.
- [ ] Referências bibliográficas verificadas.
- [ ] Rastreabilidade entre versões garantida.
- [ ] Registro de decisão de revisão armazenado.

