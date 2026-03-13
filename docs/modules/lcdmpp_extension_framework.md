# Extensão formal ΛCDM++ para o RLL (diagnóstico, implementação e operação)

## 1) Diagnóstico técnico do núcleo atual

O núcleo do pipeline já estava consistente com Friedmann no formato:

\[
H^2(z)=H_0^2[\Omega_m(1+z)^3+\Omega_r(1+z)^4+\Omega_\Lambda+\Omega_f(z)]
\]

No código, isso já existia em `H_of_z`, com termo adicional fenomenológico `Omega_f(z)` opcional. A arquitetura de comparação por χ²/AIC/BIC também já estava implementada no módulo de likelihood e nas rotinas de execução do pipeline.

---

## 2) Expansão matemática implementada (ΛCDM++)

Foi adicionada uma versão estendida de expansão cosmológica:

\[
H^2(z)=H_0^2[\Omega_m(1+z)^3+(\Omega_r+\Omega_\nu)(1+z)^4+\Omega_\Lambda+\Omega_{astro}(z)+\Omega_{fund}(z)+\Omega_q(z)]
\]

com separação explícita:

\[
\Omega_f(z)=\Omega_{astro}(z)+\Omega_{fund}(z)
\]

### 2.1 Bloco astrofísico

\[
\Omega_{astro}(z)=A(1+z)^n e^{-z/z_c}
\]

### 2.2 Bloco fundamental (componentes-base)

- EDE simplificada:

\[
\Omega_{EDE}(z)=\Omega_e(1+z)^m
\]

- Topológico:

\[
\Omega_{topo}(z)=\beta(1+z)^2
\]

- Correção quadrática tipo brana (toy):

\[
\Omega_{brane}(z)=\rho_{eff}(z)^2/\lambda_{brane}
\]

---

## 3) Crescimento estrutural

A ligação padrão de crescimento foi mantida no pipeline:

\[
f(z)\approx\Omega_m(z)^\gamma
\]

com `gamma=0.55` por padrão, que é o caso GR padrão para aproximação operacional em análises rápidas de `fσ8`.

---

## 4) Estatística de comparação de modelos

A estrutura de comparação estatística já atende o padrão moderno:

\[
AIC=\chi^2+2k
\]

\[
BIC=\chi^2+k\ln N
\]

e também inclui proxy de evidência Bayesiana baseada em BIC para triagem inicial de modelos.

---

## 5) Material técnico necessário para operação completa

Para elevar esta extensão ao nível de publicação/validação robusta, o conjunto mínimo recomendado é:

1. **Dados de expansão**: H(z), SN/μ(z), BAO (D_V/r_s ou equivalentes).
2. **Dados de crescimento**: fσ8(z) com covariância consistente.
3. **Set de neutrinos**: prior explícito em Σmν/Ων para análise de degenerescência com EDE e termos topológicos.
4. **Estudo de degenerescência**: matriz de correlação entre `{Ωe, m, β, λ_brane, Ων, A, n, zc}`.
5. **Critério de estabilidade física**: vetos adicionais para evitar regimes não físicos no espaço de parâmetros.
6. **Relatório de rastreabilidade**: tabela por parâmetro, hipótese física e impacto observável dominante.

---

## 6) Operações recomendadas (workflow objetivo)

1. Rodar `run_all.py` em baseline ΛCDM.
2. Rodar variante RLL-like padrão.
3. Rodar variante ΛCDM++ (novo bloco), com busca em grade inicial.
4. Comparar `χ², AIC, BIC, lnB`.
5. Auditar estabilidade e degenerescências.
6. Só então consolidar resultado em documento científico e release.

---

## 7) Escopo e limites atuais

A implementação introduzida é **formal e modular**, adequada para estudo comparativo e geração de hipóteses testáveis, mas ainda não substitui um solver completo Boltzmann/EFT para conclusões finais de precisão CMB de alto detalhe.

Em termos práticos: já permite uma trilha profissional de avaliação e documentação do teu “ΛCDM++” com separação física explícita de blocos, neutrinos e correções fundamentais.
