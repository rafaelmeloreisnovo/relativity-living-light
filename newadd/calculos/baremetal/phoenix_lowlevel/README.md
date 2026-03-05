# phoenix_lowlevel

Núcleo autoral em C/ASM (sem classes OO) para execução determinística de kernels.

## Objetivo
- detectar arquitetura/CPU em runtime;
- expor rotinas de baixo overhead para integração futura Java→C→ASM;
- manter base mínima sem dependências externas além da libc padrão de compilação.

## Arquivos
- `cpu_detect.c`: detecção de arquitetura e flags SIMD relevantes.
- `simd_probe_x86_64.S`: probe ASM para x86_64.
- `simd_probe_aarch64.S`: probe ASM para AArch64.
- `TMKernelBridge.java`: ponte Java fina para chamada nativa.

## Build (preview)

```bash
gcc -O3 -c cpu_detect.c -o cpu_detect.o
```

(ASMs são stubs iniciais para evolução bare-metal completa.)
