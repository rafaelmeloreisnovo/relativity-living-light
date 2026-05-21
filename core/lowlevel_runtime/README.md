# lowlevel_runtime (Java → C → ASM)

Base autoral mínima para evolução de runtime determinístico sem GC.

## Estrutura
- `java/KernelBridge.java` — casca Java para chamada nativa.
- `include/kernel_bridge.h` — cabeçalho C da ponte.
- `c/kernel_bridge.c` — implementação C mínima sem libs externas do projeto.
- `asm/arch_detect_x86_64.S` — detecção de arquitetura via CPUID (x86_64).

## Objetivo
- ponto único de entrada para rotinas low-level;
- detecção de arquitetura em ASM;
- evolução para biblioteca autoral de runtime/JNI.

## Build de referência (local)
```bash
gcc -c core/lowlevel_runtime/asm/arch_detect_x86_64.S -o core/lowlevel_runtime/asm/arch_detect_x86_64.o
gcc -c core/lowlevel_runtime/c/kernel_bridge.c -Icore/lowlevel_runtime/include -o core/lowlevel_runtime/c/kernel_bridge.o
```


## Pantheon autoral freestanding (C)
- `include/pantheon_freestanding.h` — API mínima sem stdlib.
- `c/pantheon_freestanding.c` — hash FNV-1a, CRC32 bitwise e syscall write branchless (x86_64).

### Build de referência (freestanding, objeto)
```bash
gcc -ffreestanding -fno-builtin -nostdlib -c core/lowlevel_runtime/c/pantheon_freestanding.c -Icore/lowlevel_runtime/include -o core/lowlevel_runtime/c/pantheon_freestanding.o
```
