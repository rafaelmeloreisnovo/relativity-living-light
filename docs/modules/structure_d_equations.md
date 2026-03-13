# Equações (Structure D — versão formal expandida)

## 1) Expansão de fundo (base)
Modelo base (ΛCDM + termo efetivo):
\[
H^2(z)=H_0^2\Big[\Omega_m(1+z)^3+\Omega_r(1+z)^4+\Omega_\Lambda+\Omega_f(z)\Big]
\]

com \(\Omega_f(z)\) fenomenológico para representar física não capturada no ΛCDM mínimo.

## 2) Decomposição física recomendada de \(\Omega_f\)
Para separar origem astrofísica de física fundamental:
\[
\Omega_f(z)=\Omega_{astro}(z)+\Omega_{fund}(z)
\]

### 2.1 Bloco astrofísico
\[
\Omega_{astro}(z)=A(1+z)^n\,e^{-z/z_c}
\]

Interpretação: feedback bariônico/AGN, reionização e efeitos dissipativos.

### 2.2 Bloco fundamental
Representação mínima sugerida:
\[
\Omega_{fund}(z)=\Omega_{EDE}(z)+\Omega_{topo}(z)
\]

com:
\[
\Omega_{EDE}(z)=\Omega_e(1+z)^m
\]
\[
\Omega_{topo}(z)=\beta/a^2=\beta(1+z)^2
\]

## 3) Extensão ΛCDM++ (operacional)
A forma operacional implementável para análise comparativa:
\[
H^2(z)=H_0^2\left[
\Omega_m(1+z)^3+
\Omega_r(1+z)^4+
\Omega_\Lambda+
\Omega_\nu(1+z)^3+
\Omega_{astro}(z)+
\Omega_{fund}(z)+
\Omega_q(z)
\right]
\]

onde \(\Omega_\nu\) é o setor efetivo de neutrinos massivos e \(\Omega_q\) um termo quântico efetivo de fechamento fenomenológico.

## 4) Crescimento estrutural (obrigatório para validação moderna)
Além de \(H(z)\), usar o crescimento linear:
\[
f(z)\equiv\frac{d\ln D}{d\ln a}\approx\Omega_m(z)^\gamma
\]

com \(\gamma\approx0.545\) em GR padrão e construção de \(f\sigma_8(z)\) para confronto com LSS (DES/BOSS/DESI).

## 5) Estatística de comparação de modelos
\[
\chi^2 = \sum_i \left(\frac{x_i^{obs}-x_i^{mod}}{\sigma_i}\right)^2
\]
\[
AIC = \chi^2 + 2k
\quad\quad
BIC = \chi^2 + k\ln N
\]

Uso conjunto de χ²+AIC+BIC é obrigatório para mitigar overfitting em extensões com muitos parâmetros.

## 6) Sequência prática de priorização (F_next)
Ordem sugerida para calibração incremental:
1. Early Dark Energy (\(\Omega_e,m\));
2. setor de neutrinos (\(\Omega_\nu\) efetivo);
3. termo topológico \(\beta/a^2\).

## Índice canônico de fórmulas
- Referência oficial: [`docs/FORMULAS_CANONICAS_INDEX.md`](../FORMULAS_CANONICAS_INDEX.md).
