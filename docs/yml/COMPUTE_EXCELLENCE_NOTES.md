# COMPUTE EXCELLENCE NOTES — perfil real e mapa de otimização

Análise técnica honesta (sem hype) do custo computacional **real** da
validação cosmológica deste repositório e de onde técnicas de baixo nível
(ARM64/NEON/SIMD, cache-blocking, branchless, freestanding/no-malloc) **pagam**
ou **não pagam**. Grounded em medição, não em inferência.

## 1. Perfil real do workload medido

Execução real de `validacao_real/compute_validation.py` (exit 0):

| Grandeza | Valor medido |
|---|---|
| n_obs | 45 (13 DESI DR2 BAO + 32 cronômetros cósmicos H(z)) |
| k_params | LCDM ~3, RLL ~5–8 |
| Álgebra | resolução de χ² com covariância densa pequena (≤ 32×32) |
| Custo dominante | **I/O de rede** (`fetch`: 84.766 B + ~45.045 B) + startup do Python/scipy |
| Custo aritmético | desprezível: alguns kFLOPs por avaliação de modelo |

**Conclusão honesta (FATO_VERIFICADO):** neste regime (n=45), o gargalo **não é
aritmético**. Vetorização NEON/SIMD, cache-blocking L1/L2 e branchless dariam
ganho **irrelevante** sobre o tempo total, que é dominado por rede e
interpretador. Otimizar o solver aqui seria micro-otimização prematura —
exatamente o oposto de excelência computacional. A ação de maior valor é
**determinismo e checksum**, não FLOPs.

## 2. Onde as técnicas de baixo nível PAGAM (mapa)

O custo escala se/quando a validação migrar de "ajuste pontual" para
**MCMC/Fisher sobre catálogos grandes** (Pantheon+ ~1700 SNe, chains DESI,
varreduras de grade w0–wa). Aí o perfil muda e as técnicas abaixo passam a ter
ROI real:

| Camada | Quando vale | Técnica |
|---|---|---|
| Integridade de artefatos | **já agora** | CRC32C/sha256 vetorizado sobre os YAML/CSV baixados |
| Likelihood densa N×N | N ≳ 10³ (Pantheon+ full cov) | GEMV/GEMM com NEON FMA, cache-blocking por linha de cache |
| MCMC / grade de parâmetros | varreduras grandes | paralelismo por 8 cores, layout SoA, branchless nos limites |
| Bootstrap/jackknife | reamostragem massiva | XOR-rotate hashing, RNG inline sem malloc |

## 3. Padrão de reuso já existente (Vectras-VM-Android)

O repositório do mesmo autor `rafaelmeloreisnovo/vectras-vm-android` **já
implementa** o padrão estado-da-arte que deveria ser reusado em vez de
reinventado — referências reais verificadas:

- `app/src/main/cpp/vectra_lowlevel_backend_arm64.c` — `arm_neon.h` + `arm_acle.h`,
  CRC32C por hardware (`__crc32cd`/`__crc32cb`, 8 bytes/iteração) e **fallback
  branchless** (`mask = -(crc & 1)`), sem ramo no laço quente.
- Despacho por **vtable em runtime** (`vectra_lowlevel_backend_vtable_t`,
  `vectra_backend_bind_arm64`) selecionando o backend por
  `simd_mask & VECTRA_SIMD_NEON` — zero overhead de abstração no hot path.
- Backends por arquitetura: `…_arm64.c`, `…_armv7.c`, `…_riscv64.c`,
  `…_x86_64.c`, `…_x86.c`, `…_fallback.c` — degradação graciosa.
- `vectra_core_accel.c` / `hardware_profile_bridge.c` — perfilamento real de
  `cache_line_bytes`, `page_bytes`, `pointer_bits` (layout consciente de cache).
- Assembly inline/freestanding em `engine/rmr/interop/rmr_lowlevel_x86_64.S`.

Esse desenho (detecção de capacidade → vtable → kernel SIMD com fallback
branchless, sem GC, sem malloc no hot path) é o caminho correto para a camada
de integridade/aceleração **se** a validação cosmológica escalar.

## 4. Ação recomendada (sem overclaim)

1. **Agora:** manter sha256 determinístico nos artefatos (já feito nos
   workflows via `CHECKSUMS.sha256`). Opcional: bridge para o CRC32C NEON do
   Vectras para verificação rápida de grandes downloads.
2. **Quando escalar a likelihood:** portar o kernel χ²/GEMV para um backend com
   detecção de NEON/SIMD em runtime + fallback escalar, reusando a vtable do
   Vectras. Não antes — em n=45 não há o que acelerar.
3. **Invariante:** nenhuma dessas otimizações pode alterar os números
   científicos. Otimização válida = **mesmo resultado, menos ciclos**; deve ser
   provada por igualdade bit-a-bit (ou dentro de tolerância documentada) contra
   o caminho de referência em Python.

**Declaração:** otimização de hardware melhora throughput e custo, **não**
melhora a evidência científica. Com os dados reais atuais, ΛCDM continua
favorecido por AIC/BIC independentemente da camada de compute.
