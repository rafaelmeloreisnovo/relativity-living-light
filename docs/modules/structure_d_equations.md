# Equações (esqueleto formal ΛCDM++)

## 1) Expansão de fundo (forma estendida)
Modelo base compatível com Friedmann:
\[
H^2(z)=H_0^2\Big[\Omega_m(1+z)^3+\Omega_r(1+z)^4+\Omega_\Lambda+\Omega_f(z)\Big]
\]

Extensão recomendada para diagnóstico físico identificável:
\[
\Omega_f(z)=\Omega_{astro}(z)+\Omega_{fund}(z)
\]

e
\[
H^2(z)=H_0^2\Big[
\Omega_m(1+z)^3+
\Omega_r(1+z)^4+
\Omega_\Lambda+
\Omega_{astro}(z)+
\Omega_{fund}(z)+
\Omega_\nu(z)+
\Omega_q(z)
\Big]
\]

### 1.1 Bloco astrofísico
\[
\Omega_{astro}(z)=A(1+z)^n\exp(-z/z_c)
\]

Interpretação: proxy para feedback bariônico/AGN, reionização e dissipação de gás.

### 1.2 Bloco fundamental (primeira camada)
Implementado no pipeline com dois subtermos:
\[
\Omega_{fund}(z)=\Omega_e(1+z)^m+\beta_{topo}(1+z)^2
\]

- \(\Omega_e,m\): componente tipo *Early Dark Energy* (fenomenológica).
- \(\beta_{topo}(1+z)^2\): contribuição topológica efetiva equivalente a termo \(\propto a^{-2}\).

### 1.3 Neutrinos e setor quântico efetivo
No estado atual do pipeline:
\[
\Omega_\nu(z)=\Omega_{\nu,0}(1+z)^3
\]
\[
\Omega_q(z)=\Omega_{q,0}(1+z)^{q_{power}}
\]

Observação: ambos são parametrizações fenomenológicas para separar hipóteses e testar sensibilidade.

---

## 2) Crescimento estrutural
Aproximação operacional adotada:
\[
f(z) \equiv \frac{d\ln D}{d\ln a} \approx \Omega_m(z)^\gamma,
\quad \gamma\approx0.545\;\text{(GR padrão)}
\]

Construção usada na prática:
\[
f\sigma_8(z)\approx \Omega_m(z)^\gamma\,\sigma_{8,0}\,S(z)
\]

onde \(S(z)\) representa supressão fenomenológica opcional associada a feedback.

---

## 3) Estatística mínima obrigatória
Além de \(\chi^2\), usar métricas penalizadas de complexidade:
\[
\chi^2 = \sum_i \left(\frac{x_i^{obs}-x_i^{mod}}{\sigma_i}\right)^2
\]
\[
AIC = \chi^2 + 2k
\]
\[
BIC = \chi^2 + k\ln N
\]

- \(k\): número de parâmetros livres.
- \(N\): número de observações efetivas.

---

## 4) Material mínimo para validação profissional
Para cada extensão, manter:

1. **Definição matemática explícita** da componente no relatório.
2. **Faixas de prior físicas** para cada parâmetro.
3. **Tabela de identificabilidade** (quais dados constrangem cada termo).
4. **Comparação de modelos** via \(\Delta\chi^2\), \(\Delta AIC\), \(\Delta BIC\), fator de Bayes.
5. **Teste de robustez** com desligamento seletivo de componentes.
6. **Rastreabilidade** de versão (configuração, hash de outputs e contrato de reprodução).

---

## 5) Prioridade de execução (F_next)
Ordem recomendada de campanha computacional:

1. Early Dark Energy (\(\Omega_e,m\));
2. massa efetiva de neutrinos (\(\Omega_\nu\));
3. termo topológico (\(\beta_{topo}/a^2\)).

Essa ordem maximiza utilidade prática para tensões observacionais atuais sem inflar complexidade logo no início.

## Índice canônico de fórmulas
- Referência oficial: [`docs/FORMULAS_CANONICAS_INDEX.md`](../FORMULAS_CANONICAS_INDEX.md).
