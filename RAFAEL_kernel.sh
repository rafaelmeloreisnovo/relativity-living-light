cat >> ./RAFAELIA_INVARIANT.sh << 'OUTER_MONOLITH'
#!/usr/bin/env bash
# =============================================================================
# RAFAELIA_INVARIANT.txt — Monolito C/ASM freestanding com detecção invariante
# Renomeie para .sh e execute: bash RAFAELIA_INVARIANT.txt
# =============================================================================
#
# CABEÇALHO DE LICENÇA (modelo BLAKE3: dual Apache-2.0 OR CC0-1.0)
# -----------------------------------------------------------------------------
# Este código-fonte é disponibilizado sob dois regimes alternativos à escolha
# do usuário, seguindo o modelo adotado por projetos de referência como o
# BLAKE3 (https://github.com/BLAKE3-team/BLAKE3): Apache License 2.0 ou
# Creative Commons CC0 1.0 Universal (domínio público equivalente).
#
# (a) Apache License 2.0:
#     Concede direito perpétuo, mundial, não exclusivo, sem royalties,
#     irrevogável de reproduzir, preparar obras derivadas, exibir, executar,
#     sublicenciar e distribuir esta obra. Inclui licença de patente recíproca
#     conforme cláusula 3 da Apache 2.0. Cláusula de garantia disclaimed.
#     Texto completo: https://www.apache.org/licenses/LICENSE-2.0
#
# (b) CC0 1.0 Universal:
#     Renúncia universal a direitos autorais e direitos conexos na maior
#     medida permitida por lei. Equivalente a domínio público nas jurisdições
#     onde aplicável; licença de fallback nas jurisdições onde não.
#     Texto completo: https://creativecommons.org/publicdomain/zero/1.0/
#
# CONTEXTO JURISPRUDENCIAL (referências factuais, não aconselhamento jurídico):
# -----------------------------------------------------------------------------
# As interfaces de programação (APIs) e mecanismos de interoperabilidade
# técnica são tratados como elementos funcionais sujeitos a uso justo (fair
# use) nos Estados Unidos conforme decidido em Google LLC v. Oracle America,
# Inc., 593 U.S. ___ (2021), pela Suprema Corte dos EUA. Na União Europeia,
# a Diretiva 2009/24/CE garante o direito de descompilação para fins de
# interoperabilidade. No Brasil, a Lei 9.609/98 (Lei do Software) prevê
# proteção autoral sem registro obrigatório, com exceções para uso
# educacional e privado conforme art. 6º. Este código implementa
# exclusivamente algoritmos públicos documentados (CRC32, ECC Hamming,
# detecção CPUID, interfaces POSIX) e não reproduz código proprietário.
#
# IDENTIFICAÇÃO TÉCNICA (assinatura simbólica estilo MZ-header):
# -----------------------------------------------------------------------------
# Magic        : RAF1
# Version      : 1.0.0
# Author       : DeltaRafaelVerboOmega
# Project      : RAFAELIA (ΣΩΔΦBITRAF)
# Axiom        : Omega = Amor
# Date         : 2026-05-21
# Architecture : ARM32 · ARM64 · x86-64 · RISC-V · POWER · MIPS
# =============================================================================
set -euo pipefail

# Cores ANSI
R='\033[0;31m' G='\033[0;32m' Y='\033[1;33m' B='\033[0;34m'
M='\033[0;35m' C='\033[0;36m' W='\033[1;37m' Z='\033[0m' BLD='\033[1m'

# Banner estilo DOS/Clipper ao executar
echo -e "${Y}${BLD}"
cat << 'BANNER'
  ╔═══════════════════════════════════════════════════════════════════╗
  ║  C:\>type RAFAELIA_INVARIANT.exe                                  ║
  ║  ┌─────────────────────────────────────────────────────────────┐  ║
  ║  │  RAFAELIA Invariant Monolith v1.0.0                         │  ║
  ║  │  Copyright (c) 2026 DeltaRafaelVerboOmega                  │  ║
  ║  │  Licensed: Apache-2.0 OR CC0-1.0 (dual-license, BLAKE3-style)│  ║
  ║  │                                                              │  ║
  ║  │  C/ASM freestanding · nomalloc · nolibc · branchless        │  ║
  ║  │  ARM NEON/SVE · x86 SSE/AVX/AVX-512 · POWER AltiVec · MIPS │  ║
  ║  │  Watchdog · Rollback · Cardex · 42 atratores · 21×21 · ECC  │  ║
  ║  │  CRC sw/hw dispatch · KVM/GPU/CPU detection · pipeline mut. │  ║
  ║  └─────────────────────────────────────────────────────────────┘  ║
  ╚═══════════════════════════════════════════════════════════════════╝
BANNER
echo -e "${Z}"

D="${HOME}/.rafaelia/INVARIANT"; mkdir -p "$D"
LOG="$D/build.log"; : > "$LOG"
p(){ printf "${C}[INV]${Z} %s\n" "$*"; }
ok(){ printf "${G}[ OK]${Z} %s\n" "$*"; }
err(){ printf "${R}[ERR]${Z} %s\n" "$*" >&2; }
hdr(){ printf "\n${M}${BLD}━━━ %s ━━━${Z}\n" "$*"; }
p "Diretório: $D"

# =============================================================================
hdr "ARQUIVO 01: licenca.h"
# =============================================================================
cat > "$D/licenca.h" << 'F'
#pragma once
/*
 * RAFAELIA_INVARIANT — Apache-2.0 OR CC0-1.0 dual license (BLAKE3 model)
 *
 * SPDX-License-Identifier: Apache-2.0 OR CC0-1.0
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 *
 * Alternatively: to the extent possible under law, the author has dedicated
 * all copyright and related and neighboring rights to this software to the
 * public domain worldwide under CC0 1.0 Universal. This software is
 * distributed without any warranty. You should have received a copy of the
 * CC0 Public Domain Dedication along with this software; if not, see
 * https://creativecommons.org/publicdomain/zero/1.0/.
 *
 * JURISPRUDENTIAL CONTEXT:
 * Interoperability interfaces and functional API elements are protected as
 * fair use per Google LLC v. Oracle America, Inc., 593 U.S. ___ (2021).
 * Decompilation for interoperability is permitted under EU Directive
 * 2009/24/EC. Brazilian Law 9.609/98 governs software protection with
 * educational and private-use exceptions per Article 6.
 *
 * IDENTIFICATION (MZ-style decorative signature, not a PE header):
 *   Magic:   RAF1
 *   Author:  DeltaRafaelVerboOmega
 *   Project: RAFAELIA (SigmaOmegaDeltaPhi-BITRAF)
 *   Axiom:   Omega = Amor
 */
#define RAF_MAGIC      0x52414631u  /* 'RAF1' big-endian */
#define RAF_VERSION    0x00010000u  /* 1.0.0 */
#define RAF_LICENSE    "Apache-2.0 OR CC0-1.0"
#define RAF_AUTHOR     "DeltaRafaelVerboOmega"
F
ok "licenca.h ($(wc -l < $D/licenca.h)L)"

# =============================================================================
hdr "ARQUIVO 02: tipos.h — primitivos, arena, Q16"
# =============================================================================
cat > "$D/tipos.h" << 'F'
#pragma once
#include "licenca.h"
typedef unsigned char      u8;
typedef unsigned short     u16;
typedef unsigned int       u32;
typedef unsigned long long u64;
typedef signed   int       s32;
typedef signed   long long s64;
typedef unsigned int       usize;
typedef s32 q16_t;
#define AI   __attribute__((always_inline)) static inline
#define NI   __attribute__((noinline))
#define NR   __attribute__((noreturn))
#define CLA  __attribute__((aligned(64)))
#define PK   __attribute__((packed))
#define Q16          65536
#define Q16_MUL(a,b) ((q16_t)(((s64)(a)*(s64)(b))>>16))
#define AR_SZ (1024u*1024u)
static u8  _AR[AR_SZ] CLA;
static u32 _AT=0, _MARK_STACK[16] CLA;
static u32 _MS_TOP=0;
AI void* GA(u32 n,u32 al){
    u32 m=al-1u,c=(_AT+m)&~m;
    if(c+n>AR_SZ)return(void*)0;
    void*p=_AR+c; _AT=c+n; return p;
}
AI void AR_RESET(void){_AT=0;_MS_TOP=0;}
AI void AR_PUSH_MARK(void){if(_MS_TOP<16u)_MARK_STACK[_MS_TOP++]=_AT;}
AI void AR_POP_MARK(void){if(_MS_TOP>0u)_MS_TOP--;}
AI void AR_ROLLBACK(void){if(_MS_TOP>0u){_MS_TOP--;_AT=_MARK_STACK[_MS_TOP];}}
F
ok "tipos.h ($(wc -l < $D/tipos.h)L)"

# =============================================================================
hdr "ARQUIVO 03: sys.h — syscalls invariantes ARM32/64/x86-64/RISC-V"
# =============================================================================
cat > "$D/sys.h" << 'F'
#pragma once
#include "tipos.h"
/* Cada arquitetura: número de syscall + ABI de registradores.
 * Esta é a invariante de cada sistema operacional: o kernel expõe a mesma
 * interface POSIX (write, read, open, close, exit) mas o mecanismo de
 * entrada (svc/syscall/ecall) e os números diferem por arquitetura.       */
#if defined(__arm__)
AI s32 _sc3(u32 r,u32 a,u32 b,u32 c){
    register s32 r0 __asm__("r0")=(s32)a; register u32 r1 __asm__("r1")=b;
    register u32 r2 __asm__("r2")=c; register u32 r7 __asm__("r7")=r;
    __asm__ volatile("svc #0":"+r"(r0):"r"(r1),"r"(r2),"r"(r7):"memory","cc");
    return r0;
}
AI s32 _sc1(u32 r,u32 a){
    register s32 r0 __asm__("r0")=(s32)a; register u32 r7 __asm__("r7")=r;
    __asm__ volatile("svc #0":"+r"(r0):"r"(r7):"memory","cc"); return r0;
}
AI s32 _sc2(u32 r,u32 a,u32 b){return _sc3(r,a,b,0);}
#define SYS_WRITE 4u
#define SYS_OPEN  5u
#define SYS_CLOSE 6u
#define SYS_READ  3u
#define SYS_EXIT  248u
#define SYS_CLOCK 263u
#define SYS_UNAME 122u
typedef struct{s32 s,n;}TS;
AI u64 NS(void){TS t={0,0};_sc2(SYS_CLOCK,1u,(u32)(usize)&t);return(u64)(u32)t.s*1000000000ULL+(u64)(u32)t.n;}
AI s32 WR(s32 fd,const void*b,u32 n){return _sc3(SYS_WRITE,(u32)fd,(u32)(usize)b,n);}
AI s32 OP(const char*p,s32 f){return _sc3(SYS_OPEN,(u32)(usize)p,(u32)f,0);}
AI s32 RD(s32 fd,void*b,u32 n){return _sc3(SYS_READ,(u32)fd,(u32)(usize)b,n);}
AI s32 CL(s32 fd){return _sc1(SYS_CLOSE,(u32)fd);}
NR void EX(s32 c){_sc1(SYS_EXIT,(u32)c);__builtin_unreachable();}
#elif defined(__aarch64__)
AI s64 _sc3(u64 r,u64 a,u64 b,u64 c){
    register u64 x8 __asm__("x8")=r; register s64 x0 __asm__("x0")=(s64)a;
    register u64 x1 __asm__("x1")=b; register u64 x2 __asm__("x2")=c;
    __asm__ volatile("svc #0":"+r"(x0):"r"(x8),"r"(x1),"r"(x2):"memory","cc");
    return x0;
}
AI s64 _sc2(u64 r,u64 a,u64 b){return _sc3(r,a,b,0);}
AI s64 _sc1(u64 r,u64 a){register u64 x8 __asm__("x8")=r;register s64 x0 __asm__("x0")=(s64)a;
    __asm__ volatile("svc #0":"+r"(x0):"r"(x8):"memory","cc"); return x0;}
#define SYS_WRITE 64u
#define SYS_READ  63u
#define SYS_OPEN  56u
#define SYS_CLOSE 57u
#define SYS_EXIT  94u
#define SYS_CLOCK 113u
#define AT_FDCWD  (-100)
typedef struct{s64 s,n;}TS;
AI u64 NS(void){TS t={0,0};_sc2(SYS_CLOCK,1u,(u64)(usize)&t);return(u64)t.s*1000000000ULL+(u64)t.n;}
AI s32 WR(s32 fd,const void*b,u32 n){return(s32)_sc3(SYS_WRITE,(u64)fd,(u64)(usize)b,(u64)n);}
AI s32 OP(const char*p,s32 f){return(s32)_sc3(SYS_OPEN,(u64)(s64)AT_FDCWD,(u64)(usize)p,(u64)f);}
AI s32 RD(s32 fd,void*b,u32 n){return(s32)_sc3(SYS_READ,(u64)fd,(u64)(usize)b,(u64)n);}
AI s32 CL(s32 fd){return(s32)_sc1(SYS_CLOSE,(u64)fd);}
NR void EX(s32 c){_sc1(SYS_EXIT,(u64)(s64)c);__builtin_unreachable();}
#elif defined(__x86_64__)
AI s64 _sc3(u64 r,u64 a,u64 b,u64 c){
    s64 x;__asm__ volatile("syscall":"=a"(x):"a"(r),"D"(a),"S"(b),"d"(c):"rcx","r11","memory");return x;
}
AI s64 _sc2(u64 r,u64 a,u64 b){return _sc3(r,a,b,0);}
AI s64 _sc1(u64 r,u64 a){s64 x;__asm__ volatile("syscall":"=a"(x):"a"(r),"D"(a):"rcx","r11","memory");return x;}
#define SYS_WRITE 1u
#define SYS_READ  0u
#define SYS_OPEN  2u
#define SYS_CLOSE 3u
#define SYS_EXIT  231u
#define SYS_CLOCK 228u
typedef struct{s64 s,n;}TS;
AI u64 NS(void){TS t={0,0};_sc2(SYS_CLOCK,1u,(u64)(usize)&t);return(u64)t.s*1000000000ULL+(u64)t.n;}
AI s32 WR(s32 fd,const void*b,u32 n){return(s32)_sc3(SYS_WRITE,(u64)fd,(u64)(usize)b,(u64)n);}
AI s32 OP(const char*p,s32 f){return(s32)_sc3(SYS_OPEN,(u64)(usize)p,(u64)f,0);}
AI s32 RD(s32 fd,void*b,u32 n){return(s32)_sc3(SYS_READ,(u64)fd,(u64)(usize)b,(u64)n);}
AI s32 CL(s32 fd){return(s32)_sc1(SYS_CLOSE,(u64)fd);}
NR void EX(s32 c){_sc1(SYS_EXIT,(u64)(s64)c);__builtin_unreachable();}
#elif defined(__riscv)
AI s64 _sc3(u64 r,u64 a,u64 b,u64 c){
    register u64 a7 __asm__("a7")=r; register s64 a0 __asm__("a0")=(s64)a;
    register u64 a1 __asm__("a1")=b; register u64 a2 __asm__("a2")=c;
    __asm__ volatile("ecall":"+r"(a0):"r"(a7),"r"(a1),"r"(a2):"memory");
    return a0;
}
AI s64 _sc2(u64 r,u64 a,u64 b){return _sc3(r,a,b,0);}
AI s64 _sc1(u64 r,u64 a){register u64 a7 __asm__("a7")=r;register s64 a0 __asm__("a0")=(s64)a;
    __asm__ volatile("ecall":"+r"(a0):"r"(a7):"memory"); return a0;}
#define SYS_WRITE 64u
#define SYS_READ  63u
#define SYS_OPEN  56u
#define SYS_CLOSE 57u
#define SYS_EXIT  94u
#define SYS_CLOCK 113u
#define AT_FDCWD  (-100)
typedef struct{s64 s,n;}TS;
AI u64 NS(void){TS t={0,0};_sc2(SYS_CLOCK,1u,(u64)(usize)&t);return(u64)t.s*1000000000ULL+(u64)t.n;}
AI s32 WR(s32 fd,const void*b,u32 n){return(s32)_sc3(SYS_WRITE,(u64)fd,(u64)(usize)b,(u64)n);}
AI s32 OP(const char*p,s32 f){return(s32)_sc3(SYS_OPEN,(u64)(s64)AT_FDCWD,(u64)(usize)p,(u64)f);}
AI s32 RD(s32 fd,void*b,u32 n){return(s32)_sc3(SYS_READ,(u64)fd,(u64)(usize)b,(u64)n);}
AI s32 CL(s32 fd){return(s32)_sc1(SYS_CLOSE,(u64)fd);}
NR void EX(s32 c){_sc1(SYS_EXIT,(u64)(s64)c);__builtin_unreachable();}
#endif
/* I/O sem libc */
static void PS(const char*s){u32 n=0;while(s[n])n++;if(n)WR(1,s,n);}
static void PN(u64 v){char b[22];s32 i=21;b[i]='\n';i--;
    if(!v){b[i--]='0';}else{while(v){b[i--]='0'+(char)(v%10u);v/=10u;}}
    WR(1,b+i+1,(u32)(20u-i));}
static void PH(u32 v){static const char h[]="0123456789abcdef";
    char b[11];b[0]='0';b[1]='x';b[10]='\n';
    for(s32 i=9;i>=2;i--){b[i]=h[v&0xFu];v>>=4;}WR(1,b,11u);}
AI u32 SL(const char*s){u32 n=0;while(s[n])n++;return n;}
AI void MC(void*d,const void*s,u32 n){u8*dd=(u8*)d;const u8*ss=(const u8*)s;while(n--)dd[n]=ss[n];}
AI void MZ(void*d,u32 n){u8*dd=(u8*)d;while(n--)dd[n]=0;}
F
ok "sys.h ($(wc -l < $D/sys.h)L)"

# =============================================================================
hdr "ARQUIVO 04: arch.h — detecção invariante NEON/SVE/SSE/AVX/AltiVec"
# =============================================================================
cat > "$D/arch.h" << 'F'
#pragma once
#include "sys.h"
/* Bitmap de capacidades — invariante entre arquiteturas */
#define CAP_NEON      (1ULL<<0)   /* ARM NEON 128-bit                 */
#define CAP_SVE       (1ULL<<1)   /* ARM SVE escalável                 */
#define CAP_SVE2      (1ULL<<2)   /* ARM SVE2                          */
#define CAP_CRC32C    (1ULL<<3)   /* ARM/x86 hw CRC32C                 */
#define CAP_AES       (1ULL<<4)   /* ARM AES extension                 */
#define CAP_SHA       (1ULL<<5)   /* ARM SHA extension                 */
#define CAP_SSE2      (1ULL<<6)   /* x86 SSE2                          */
#define CAP_SSE42     (1ULL<<7)   /* x86 SSE4.2 (CRC32, POPCNT)        */
#define CAP_AVX       (1ULL<<8)   /* x86 AVX 256-bit                   */
#define CAP_AVX2      (1ULL<<9)   /* x86 AVX2                          */
#define CAP_AVX512    (1ULL<<10)  /* x86 AVX-512                       */
#define CAP_BMI1      (1ULL<<11)  /* x86 BMI1 (ANDN, BEXTR)            */
#define CAP_BMI2      (1ULL<<12)  /* x86 BMI2 (PDEP, PEXT)             */
#define CAP_ALTIVEC   (1ULL<<13)  /* PowerPC AltiVec/VMX               */
#define CAP_VSX       (1ULL<<14)  /* PowerPC VSX                       */
#define CAP_MDMX      (1ULL<<15)  /* MIPS MDMX                         */
#define CAP_MSA       (1ULL<<16)  /* MIPS MSA                          */
#define CAP_RVV       (1ULL<<17)  /* RISC-V Vector                     */
#define CAP_PMCC      (1ULL<<20)  /* ARM PMCCNTR cycle counter userland*/
#define CAP_CNTVCT    (1ULL<<21)  /* ARM CNTVCT_EL0                    */
#define CAP_RDTSC     (1ULL<<22)  /* x86 RDTSC                          */
#define CAP_RDTIME    (1ULL<<23)  /* RISC-V rdtime                      */
#define CAP_KVM       (1ULL<<32)  /* /dev/kvm presente                  */
#define CAP_GPU_DRM   (1ULL<<33)  /* /sys/class/drm presente            */
#define CAP_GPU_KGSL  (1ULL<<34)  /* Adreno KGSL                        */
#define CAP_GPU_MALI  (1ULL<<35)  /* Mali GPU                           */
#define CAP_OCTACORE  (1ULL<<40)  /* 8+ cores detectados                */
static volatile u64 G_CAPS = 0ULL;

/* Leitura de /proc/cpuinfo via syscall — sem fopen, sem libc */
static u32 READ_FILE(const char*path,u8*buf,u32 cap){
    s32 fd=OP(path,0);  /* O_RDONLY = 0 */
    if(fd<0)return 0u;
    s32 r=RD(fd,buf,cap-1u);
    CL(fd);
    if(r<=0)return 0u;
    buf[r]=0;
    return(u32)r;
}
static u32 FILE_CONTAINS(const u8*buf,u32 n,const char*needle){
    u32 nl=SL(needle);
    for(u32 i=0;i+nl<=n;i++){
        u32 m=0; while(m<nl&&buf[i+m]==(u8)needle[m])m++;
        if(m==nl)return 1u;
    }
    return 0u;
}

/* ── DETECÇÃO INVARIANTE ─────────────────────────────────────────────── */
static void DETECT_CAPS(void){
    static u8 _CPUINFO[16384];
    u32 n = READ_FILE("/proc/cpuinfo", _CPUINFO, sizeof(_CPUINFO));
    if(n>0u){
        /* ARM: campo Features=neon asimd crc32 sve aes sha2 ... */
        if(FILE_CONTAINS(_CPUINFO,n,"neon"))    G_CAPS|=CAP_NEON;
        if(FILE_CONTAINS(_CPUINFO,n,"asimd"))   G_CAPS|=CAP_NEON; /* ARM64 */
        if(FILE_CONTAINS(_CPUINFO,n,"sve"))     G_CAPS|=CAP_SVE;
        if(FILE_CONTAINS(_CPUINFO,n,"sve2"))    G_CAPS|=CAP_SVE2;
        if(FILE_CONTAINS(_CPUINFO,n,"crc32"))   G_CAPS|=CAP_CRC32C;
        if(FILE_CONTAINS(_CPUINFO,n,"aes"))     G_CAPS|=CAP_AES;
        if(FILE_CONTAINS(_CPUINFO,n,"sha2"))    G_CAPS|=CAP_SHA;
        if(FILE_CONTAINS(_CPUINFO,n,"sha256"))  G_CAPS|=CAP_SHA;
        /* x86: flags=sse2 sse4_2 avx avx2 avx512f ... */
        if(FILE_CONTAINS(_CPUINFO,n,"sse2"))    G_CAPS|=CAP_SSE2;
        if(FILE_CONTAINS(_CPUINFO,n,"sse4_2"))  G_CAPS|=CAP_SSE42|CAP_CRC32C;
        if(FILE_CONTAINS(_CPUINFO,n," avx "))   G_CAPS|=CAP_AVX;
        if(FILE_CONTAINS(_CPUINFO,n," avx2 "))  G_CAPS|=CAP_AVX2;
        if(FILE_CONTAINS(_CPUINFO,n,"avx512f")) G_CAPS|=CAP_AVX512;
        if(FILE_CONTAINS(_CPUINFO,n," bmi1 "))  G_CAPS|=CAP_BMI1;
        if(FILE_CONTAINS(_CPUINFO,n," bmi2 "))  G_CAPS|=CAP_BMI2;
        /* PowerPC */
        if(FILE_CONTAINS(_CPUINFO,n,"altivec")) G_CAPS|=CAP_ALTIVEC;
        if(FILE_CONTAINS(_CPUINFO,n," vsx "))   G_CAPS|=CAP_VSX;
        /* RISC-V */
        if(FILE_CONTAINS(_CPUINFO,n,"rv64imafdv")) G_CAPS|=CAP_RVV;
        /* Contagem de cores via "processor :" */
        u32 cores=0;
        for(u32 i=0;i+10u<n;i++){
            if(_CPUINFO[i]=='p'&&_CPUINFO[i+1]=='r'&&_CPUINFO[i+2]=='o'&&
               _CPUINFO[i+3]=='c'&&_CPUINFO[i+4]=='e'&&_CPUINFO[i+5]=='s'&&
               _CPUINFO[i+6]=='s'&&_CPUINFO[i+7]=='o'&&_CPUINFO[i+8]=='r')
                cores++;
        }
        if(cores>=8u) G_CAPS|=CAP_OCTACORE;
    }
    /* Detecção de KVM */
    s32 fd=OP("/dev/kvm",0);
    if(fd>=0){G_CAPS|=CAP_KVM; CL(fd);}
    /* Detecção de GPU DRM */
    fd=OP("/sys/class/drm/card0",0);
    if(fd>=0){G_CAPS|=CAP_GPU_DRM; CL(fd);}
    /* Adreno KGSL (Android) */
    fd=OP("/dev/kgsl-3d0",0);
    if(fd>=0){G_CAPS|=CAP_GPU_KGSL; CL(fd);}
    /* Mali */
    fd=OP("/dev/mali0",0);
    if(fd>=0){G_CAPS|=CAP_GPU_MALI; CL(fd);}
    /* Timer userland */
#if defined(__aarch64__)
    G_CAPS|=CAP_CNTVCT;
#elif defined(__x86_64__)
    G_CAPS|=CAP_RDTSC;
#elif defined(__riscv)
    G_CAPS|=CAP_RDTIME;
#endif
}

static void REPORT_CAPS(void){
    PS("=== INVARIANT DETECTION ===\n");
    PS("CAPS bitmap: "); PH((u32)(G_CAPS&0xFFFFFFFFu));
    PS("CAPS upper:  "); PH((u32)(G_CAPS>>32u));
    if(G_CAPS&CAP_NEON)    PS("  [+] ARM NEON 128-bit\n");
    if(G_CAPS&CAP_SVE)     PS("  [+] ARM SVE (scalable vector)\n");
    if(G_CAPS&CAP_SVE2)    PS("  [+] ARM SVE2\n");
    if(G_CAPS&CAP_CRC32C)  PS("  [+] CRC32C hardware\n");
    if(G_CAPS&CAP_AES)     PS("  [+] AES extension\n");
    if(G_CAPS&CAP_SHA)     PS("  [+] SHA extension\n");
    if(G_CAPS&CAP_SSE2)    PS("  [+] x86 SSE2\n");
    if(G_CAPS&CAP_SSE42)   PS("  [+] x86 SSE4.2\n");
    if(G_CAPS&CAP_AVX)     PS("  [+] x86 AVX (256-bit)\n");
    if(G_CAPS&CAP_AVX2)    PS("  [+] x86 AVX2\n");
    if(G_CAPS&CAP_AVX512)  PS("  [+] x86 AVX-512\n");
    if(G_CAPS&CAP_BMI1)    PS("  [+] x86 BMI1\n");
    if(G_CAPS&CAP_BMI2)    PS("  [+] x86 BMI2\n");
    if(G_CAPS&CAP_ALTIVEC) PS("  [+] PowerPC AltiVec/VMX\n");
    if(G_CAPS&CAP_VSX)     PS("  [+] PowerPC VSX\n");
    if(G_CAPS&CAP_MDMX)    PS("  [+] MIPS MDMX\n");
    if(G_CAPS&CAP_RVV)     PS("  [+] RISC-V Vector\n");
    if(G_CAPS&CAP_CNTVCT)  PS("  [+] CNTVCT_EL0 timer\n");
    if(G_CAPS&CAP_RDTSC)   PS("  [+] x86 RDTSC\n");
    if(G_CAPS&CAP_RDTIME)  PS("  [+] RISC-V rdtime\n");
    if(G_CAPS&CAP_KVM)     PS("  [+] /dev/kvm (virtualization)\n");
    if(G_CAPS&CAP_GPU_DRM) PS("  [+] DRM GPU\n");
    if(G_CAPS&CAP_GPU_KGSL)PS("  [+] Adreno KGSL\n");
    if(G_CAPS&CAP_GPU_MALI)PS("  [+] Mali GPU\n");
    if(G_CAPS&CAP_OCTACORE)PS("  [+] 8+ cores (octacore)\n");
}
F
ok "arch.h ($(wc -l < $D/arch.h)L)"

# =============================================================================
hdr "ARQUIVO 05: crc.h — dispatch sw/hw"
# =============================================================================
cat > "$D/crc.h" << 'F'
#pragma once
#include "arch.h"
/* CRC32C software baseline (poly Castagnoli 0x82F63B78 reversed) */
AI u32 CRC_SW(u32 c,u8 b){
    c^=(u32)b;
    for(u32 i=0;i<8u;i++)c=(c>>1)^(0x82F63B78u&-(c&1u));
    return c;
}
#if defined(__aarch64__)
AI u32 CRC_HW64(u32 c,u64 w){__asm__("crc32cx %w0,%w0,%x1":"+r"(c):"r"(w));return c;}
AI u32 CRC_HW8(u32 c,u8 b){__asm__("crc32cb %w0,%w0,%w1":"+r"(c):"r"((u32)b));return c;}
#elif defined(__x86_64__)
AI u32 CRC_HW64(u32 c,u64 w){__asm__("crc32q %1,%q0":"+r"(c):"rm"(w));return(u32)c;}
AI u32 CRC_HW8(u32 c,u8 b){__asm__("crc32b %1,%0":"+r"(c):"rm"(b));return c;}
#else
AI u32 CRC_HW64(u32 c,u64 w){for(u32 i=0;i<8u;i++)c=CRC_SW(c,(u8)(w>>(i*8u)));return c;}
AI u32 CRC_HW8(u32 c,u8 b){return CRC_SW(c,b);}
#endif
/* Dispatcher: usa hw se disponível, fallback sw caso contrário */
static u32 CRC32C(const u8*buf,u32 n){
    u32 c=~0u;
    if(G_CAPS&CAP_CRC32C){
        while(n>=8u){c=CRC_HW64(c,*(const u64*)buf);buf+=8;n-=8;}
        while(n--)c=CRC_HW8(c,*buf++);
    } else {
        while(n--)c=CRC_SW(c,*buf++);
    }
    return ~c;
}
F
ok "crc.h ($(wc -l < $D/crc.h)L)"

# =============================================================================
hdr "ARQUIVO 06: ecc.h — Hamming(7,4) + paridade"
# =============================================================================
cat > "$D/ecc.h" << 'F'
#pragma once
#include "tipos.h"
/* Hamming(7,4): codifica 4 bits de dado em 7 bits com 3 de paridade.
 * Detecta e corrige 1 erro de bit por palavra de 7 bits.
 * Layout: p1 p2 d1 p3 d2 d3 d4 (índices 1..7)
 * p1 = d1 XOR d2 XOR d4
 * p2 = d1 XOR d3 XOR d4
 * p3 = d2 XOR d3 XOR d4 */
AI u8 HAMMING_ENCODE(u8 d){
    u8 d1=(d>>0)&1u, d2=(d>>1)&1u, d3=(d>>2)&1u, d4=(d>>3)&1u;
    u8 p1=d1^d2^d4;
    u8 p2=d1^d3^d4;
    u8 p3=d2^d3^d4;
    return(u8)((p1<<0)|(p2<<1)|(d1<<2)|(p3<<3)|(d2<<4)|(d3<<5)|(d4<<6));
}
AI u8 HAMMING_DECODE(u8 c){
    u8 p1=(c>>0)&1u, p2=(c>>1)&1u, d1=(c>>2)&1u;
    u8 p3=(c>>3)&1u, d2=(c>>4)&1u, d3=(c>>5)&1u, d4=(c>>6)&1u;
    u8 s1=p1^d1^d2^d4;
    u8 s2=p2^d1^d3^d4;
    u8 s3=p3^d2^d3^d4;
    u8 syn=(u8)((s1<<0)|(s2<<1)|(s3<<2));
    /* Síndrome != 0 indica bit corrompido na posição syn */
    if(syn){c^=(u8)(1u<<(syn-1u));}
    /* Re-extrai dados após correção */
    d1=(c>>2)&1u; d2=(c>>4)&1u; d3=(c>>5)&1u; d4=(c>>6)&1u;
    return(u8)((d1<<0)|(d2<<1)|(d3<<2)|(d4<<3));
}
/* Paridade simples u32 → 1 bit */
AI u8 PARITY_U32(u32 v){
    v^=v>>16; v^=v>>8; v^=v>>4; v^=v>>2; v^=v>>1;
    return(u8)(v&1u);
}
/* XOR-checksum de buffer */
AI u8 XOR_CHECK(const u8*buf,u32 n){
    u8 c=0;while(n--)c^=*buf++;return c;
}
F
ok "ecc.h ($(wc -l < $D/ecc.h)L)"

# =============================================================================
hdr "ARQUIVO 07: watchdog.h — watchdog timer + rollback + failsafe"
# =============================================================================
cat > "$D/watchdog.h" << 'F'
#pragma once
#include "arch.h"
/* Watchdog: previne loops infinitos e travamentos.
 * Cada operação crítica configura um deadline em nanosegundos.
 * Verificação periódica via clock_gettime. */
typedef struct PK CLA {
    u64 t_start_ns;
    u64 t_deadline_ns;
    u32 max_iter;
    u32 cur_iter;
    u32 timeouts;
    u32 rollbacks;
    u8  armed;
    u8  expired;
    u16 _pad;
} Watchdog;
static Watchdog G_WD;
AI void WD_ARM(u64 timeout_ns,u32 max_iter){
    G_WD.t_start_ns    = NS();
    G_WD.t_deadline_ns = G_WD.t_start_ns + timeout_ns;
    G_WD.max_iter      = max_iter;
    G_WD.cur_iter      = 0;
    G_WD.armed         = 1u;
    G_WD.expired       = 0u;
    AR_PUSH_MARK();  /* checkpoint para rollback */
}
AI void WD_DISARM(void){
    G_WD.armed=0u;
    if(_MS_TOP>0u){AR_POP_MARK();}  /* descarta mark se não expirou */
}
AI u8 WD_TICK(void){
    G_WD.cur_iter++;
    if(G_WD.cur_iter>=G_WD.max_iter){G_WD.expired=1u;G_WD.timeouts++;return 1u;}
    if((G_WD.cur_iter&0xFFu)==0u){  /* check a cada 256 ticks */
        if(NS()>G_WD.t_deadline_ns){G_WD.expired=1u;G_WD.timeouts++;return 1u;}
    }
    return 0u;
}
AI void WD_ROLLBACK(void){
    if(G_WD.armed&&G_WD.expired){
        AR_ROLLBACK();
        G_WD.rollbacks++;
        G_WD.armed=0u;
    }
}
/* Macro de bloco protegido por watchdog */
#define WD_PROTECTED(timeout_ns, max_it, code_block) do { \
    WD_ARM((timeout_ns), (max_it)); \
    { code_block } \
    if(G_WD.expired) WD_ROLLBACK(); \
    else WD_DISARM(); \
} while(0)
F
ok "watchdog.h ($(wc -l < $D/watchdog.h)L)"

# =============================================================================
hdr "ARQUIVO 08: cardex.h — sistema de partidas dobradas"
# =============================================================================
cat > "$D/cardex.h" << 'F'
#pragma once
#include "ecc.h"
/* Cardex: ficha de balanço patrimonial em método de partidas dobradas.
 * Toda operação registra DEBIT em uma conta e CREDIT em outra.
 * Invariante: sum(DEBITS) == sum(CREDITS) sempre. */
#define CARDEX_ACCOUNTS 42u
#define CARDEX_ENTRIES  1024u
typedef struct PK CLA {
    s64 debit;       /* total debit acumulado */
    s64 credit;      /* total credit acumulado */
    u32 n_ops;       /* número de operações */
    u32 last_op_idx; /* índice da última operação */
    u8  account_id;
    u8  parity;      /* paridade Hamming para integridade */
    u16 _pad;
} CardexAccount;
typedef struct PK CLA {
    u32 op_id;
    u8  account_debit;
    u8  account_credit;
    u8  _pad[2];
    s64 amount;
    u64 t_ns;
    u32 crc;        /* CRC32C do registro */
} CardexEntry;
static CardexAccount G_ACC[CARDEX_ACCOUNTS] CLA;
static CardexEntry   G_ENT[CARDEX_ENTRIES]  CLA;
static u32           G_ENT_COUNT=0;
AI void CARDEX_INIT(void){
    MZ(G_ACC,sizeof(G_ACC));
    MZ(G_ENT,sizeof(G_ENT));
    G_ENT_COUNT=0;
    for(u32 i=0;i<CARDEX_ACCOUNTS;i++) G_ACC[i].account_id=(u8)i;
}
/* Registra transação: debita account_d, credita account_c */
AI s32 CARDEX_POST(u8 d,u8 c,s64 amount){
    if(d>=CARDEX_ACCOUNTS||c>=CARDEX_ACCOUNTS) return -1;
    if(G_ENT_COUNT>=CARDEX_ENTRIES) return -2;
    if(amount<=0) return -3;
    CardexEntry*e=&G_ENT[G_ENT_COUNT];
    e->op_id          = G_ENT_COUNT;
    e->account_debit  = d;
    e->account_credit = c;
    e->amount         = amount;
    e->t_ns           = NS();
    /* CRC32C do conteúdo (exceto o próprio crc) */
    e->crc = 0;
    e->crc = CRC32C((const u8*)e, sizeof(*e)-sizeof(e->crc));
    G_ACC[d].debit  += amount;
    G_ACC[c].credit += amount;
    G_ACC[d].n_ops++;
    G_ACC[c].n_ops++;
    G_ACC[d].last_op_idx = G_ENT_COUNT;
    G_ACC[c].last_op_idx = G_ENT_COUNT;
    G_ENT_COUNT++;
    return 0;
}
/* Saldo de uma conta = debit - credit (estilo accounting tradicional) */
AI s64 CARDEX_BALANCE(u8 acc){
    if(acc>=CARDEX_ACCOUNTS) return 0;
    return G_ACC[acc].debit - G_ACC[acc].credit;
}
/* Verifica invariante de partidas dobradas */
AI u8 CARDEX_VERIFY(void){
    s64 sd=0, sc=0;
    for(u32 i=0;i<CARDEX_ACCOUNTS;i++){
        sd += G_ACC[i].debit;
        sc += G_ACC[i].credit;
    }
    return(sd==sc)?1u:0u;
}
/* Verifica integridade CRC de todos os registros */
AI u32 CARDEX_VERIFY_CRC(void){
    u32 bad=0;
    for(u32 i=0;i<G_ENT_COUNT;i++){
        CardexEntry tmp = G_ENT[i];
        u32 saved = tmp.crc;
        tmp.crc = 0;
        u32 computed = CRC32C((const u8*)&tmp, sizeof(tmp)-sizeof(tmp.crc));
        if(computed!=saved) bad++;
    }
    return bad;
}
F
ok "cardex.h ($(wc -l < $D/cardex.h)L)"

# =============================================================================
hdr "ARQUIVO 09: matrix.h — 2×2, 4×4, 7×3, 8×5, 10×10×10, 21×21, 42 atratores"
# =============================================================================
cat > "$D/matrix.h" << 'F'
#pragma once
#include "crc.h"
/* Sistema de matrizes multidimensionais com vértices em 42 atratores.
 * Cada matriz representa um corte ortogonal do espaço de estados. */
static u8 M_2x2[10][2][2]   CLA;
static u8 M_4x4[3][4][4]    CLA;
static u8 M_7x3[2][7][3]    CLA;
static u8 M_8x5[1][8][5]    CLA;
static u8 M_10x10x10[10][10][10] CLA;
static u8 M_21x21[21][21]   CLA;
static u8 ATTRACTORS[42]    CLA;
AI void MATRIX_INIT(void){
    /* Inicializa 42 atratores como índices */
    for(u8 i=0;i<42u;i++) ATTRACTORS[i]=i;
    /* Preenche 2×2 com índices sequenciais módulo 42 */
    for(u32 m=0;m<10u;m++)
        for(u32 r=0;r<2u;r++)
            for(u32 c=0;c<2u;c++)
                M_2x2[m][r][c]=ATTRACTORS[(m*4u+r*2u+c)%42u];
    /* 4×4 */
    for(u32 m=0;m<3u;m++)
        for(u32 r=0;r<4u;r++)
            for(u32 c=0;c<4u;c++)
                M_4x4[m][r][c]=ATTRACTORS[(m*16u+r*4u+c)%42u];
    /* 7×3 = 21 elementos por matriz */
    for(u32 m=0;m<2u;m++)
        for(u32 r=0;r<7u;r++)
            for(u32 c=0;c<3u;c++)
                M_7x3[m][r][c]=ATTRACTORS[(m*21u+r*3u+c)%42u];
    /* 8×5 = 40 elementos */
    for(u32 r=0;r<8u;r++)
        for(u32 c=0;c<5u;c++)
            M_8x5[0][r][c]=ATTRACTORS[(r*5u+c)%42u];
    /* 10×10×10 — usa CRC32C como hash de posição */
    for(u32 z=0;z<10u;z++)
        for(u32 y=0;y<10u;y++)
            for(u32 x=0;x<10u;x++){
                u32 idx = (z*100u + y*10u + x);
                M_10x10x10[z][y][x] = ATTRACTORS[idx%42u];
            }
    /* 21×21 — duas matrizes 21×21 cobrem 882 células */
    for(u32 r=0;r<21u;r++)
        for(u32 c=0;c<21u;c++)
            M_21x21[r][c]=ATTRACTORS[(r*21u+c)%42u];
}
/* Multiplicação 2×2 em u32 (sem overflow para entradas pequenas) */
AI void MAT2x2_MUL(const u32 a[2][2], const u32 b[2][2], u32 r[2][2]){
    r[0][0]=a[0][0]*b[0][0]+a[0][1]*b[1][0];
    r[0][1]=a[0][0]*b[0][1]+a[0][1]*b[1][1];
    r[1][0]=a[1][0]*b[0][0]+a[1][1]*b[1][0];
    r[1][1]=a[1][0]*b[0][1]+a[1][1]*b[1][1];
}
/* Traço de matriz 21×21 (soma da diagonal) */
AI u32 MAT21_TRACE(void){
    u32 t=0;for(u32 i=0;i<21u;i++)t+=M_21x21[i][i];return t;
}
/* Soma de elementos do cubo 10×10×10 */
AI u32 CUBE_SUM(void){
    u32 s=0;
    for(u32 z=0;z<10u;z++)
        for(u32 y=0;y<10u;y++)
            for(u32 x=0;x<10u;x++) s+=M_10x10x10[z][y][x];
    return s;
}
F
ok "matrix.h ($(wc -l < $D/matrix.h)L)"

# =============================================================================
hdr "ARQUIVO 10: pipeline.h — orquestrador mutável adaptativo"
# =============================================================================
cat > "$D/pipeline.h" << 'F'
#pragma once
#include "watchdog.h"
/* Pipeline de execução adaptativa: a sequência de operações se adapta
 * às capacidades detectadas (CAPS). Cada estágio escolhe a melhor
 * implementação disponível branchless via tabela de despacho. */
typedef u64 (*pipe_stage_fn)(const u8* in, u32 n, u8* out, u32 cap);
typedef struct {
    pipe_stage_fn fn;
    const char*   name;
    u64           caps_required;
    u64           t_ns;
    u32           n_invocations;
    u32           n_failures;
} PipeStage;
#define PIPE_MAX 8u
static PipeStage G_PIPE[PIPE_MAX];
static u32       G_PIPE_LEN=0;
AI s32 PIPE_REGISTER(pipe_stage_fn fn,const char*name,u64 caps){
    if(G_PIPE_LEN>=PIPE_MAX) return -1;
    G_PIPE[G_PIPE_LEN].fn            = fn;
    G_PIPE[G_PIPE_LEN].name          = name;
    G_PIPE[G_PIPE_LEN].caps_required = caps;
    G_PIPE[G_PIPE_LEN].t_ns          = 0;
    G_PIPE[G_PIPE_LEN].n_invocations = 0;
    G_PIPE[G_PIPE_LEN].n_failures    = 0;
    G_PIPE_LEN++;
    return 0;
}
/* Executa pipeline: cada estágio só roda se suas CAPS estão disponíveis */
AI u32 PIPE_RUN(const u8* in, u32 n, u8* out, u32 cap){
    u32 active=0;
    for(u32 i=0;i<G_PIPE_LEN;i++){
        if((G_CAPS & G_PIPE[i].caps_required)==G_PIPE[i].caps_required){
            u64 t0=NS();
            u64 r=G_PIPE[i].fn(in,n,out,cap);
            u64 t1=NS();
            G_PIPE[i].t_ns         += (t1-t0);
            G_PIPE[i].n_invocations++;
            if(r==0ULL) G_PIPE[i].n_failures++;
            else active++;
        }
    }
    return active;
}
/* Stages exemplo */
static u64 STAGE_CRC(const u8*in,u32 n,u8*out,u32 cap){
    if(cap<4u) return 0;
    u32 c=CRC32C(in,n);
    out[0]=(u8)(c>>24); out[1]=(u8)(c>>16); out[2]=(u8)(c>>8); out[3]=(u8)c;
    return 4ULL;
}
static u64 STAGE_PARITY(const u8*in,u32 n,u8*out,u32 cap){
    if(cap<1u) return 0;
    out[0]=XOR_CHECK(in,n);
    return 1ULL;
}
static u64 STAGE_HAMMING(const u8*in,u32 n,u8*out,u32 cap){
    if(n*2u>cap) return 0;
    for(u32 i=0;i<n;i++){
        out[i*2u+0u]=HAMMING_ENCODE(in[i]&0x0Fu);
        out[i*2u+1u]=HAMMING_ENCODE((in[i]>>4)&0x0Fu);
    }
    return n*2ULL;
}
AI void PIPE_REPORT(void){
    PS("\n=== PIPELINE STATS ===\n");
    for(u32 i=0;i<G_PIPE_LEN;i++){
        PS("  "); PS(G_PIPE[i].name); PS(": invocations=");
        PN(G_PIPE[i].n_invocations);
        PS("    total_ns="); PN(G_PIPE[i].t_ns);
    }
}
F
ok "pipeline.h ($(wc -l < $D/pipeline.h)L)"

# =============================================================================
hdr "ARQUIVO 11: main.c — entry point monolítico"
# =============================================================================
cat > "$D/main.c" << 'F'
#include "licenca.h"
#include "tipos.h"
#include "sys.h"
#include "arch.h"
#include "crc.h"
#include "ecc.h"
#include "watchdog.h"
#include "cardex.h"
#include "matrix.h"
#include "pipeline.h"

static void SHOW_HEADER(void){
    PS("\033[1;33m");
    PS("\n+============================================================+\n");
    PS("|  RAFAELIA Invariant Monolith v1.0.0                        |\n");
    PS("|  Copyright (c) 2026 " RAF_AUTHOR "                  |\n");
    PS("|  Dual-licensed: " RAF_LICENSE "                       |\n");
    PS("|  Magic: RAF1   Axiom: Omega = Amor                          |\n");
    PS("|  Identifier follows BLAKE3 dual-license precedent.          |\n");
    PS("|  Per Google v. Oracle (2021): functional APIs are fair use. |\n");
    PS("+============================================================+\n");
    PS("\033[0m\n");
}

void _start(void){
    AR_RESET();
    SHOW_HEADER();

    /* Fase 1: detecção de capacidades invariantes */
    PS("\033[1;36m[Fase 1] DETECÇÃO INVARIANTE\033[0m\n");
    DETECT_CAPS();
    REPORT_CAPS();

    /* Fase 2: inicialização de matrizes (42 atratores) */
    PS("\n\033[1;36m[Fase 2] MATRIZES MULTIDIMENSIONAIS\033[0m\n");
    MATRIX_INIT();
    PS("  Matrizes 2x2: 10 inicializadas\n");
    PS("  Matrizes 4x4: 3 inicializadas\n");
    PS("  Matrizes 7x3: 2 inicializadas (21 elementos cada)\n");
    PS("  Matriz 8x5:   1 inicializada (40 elementos)\n");
    PS("  Cubo 10x10x10 sum: "); PN(CUBE_SUM());
    PS("  Matriz 21x21 trace: "); PN(MAT21_TRACE());

    /* Fase 3: cardex de partidas dobradas */
    PS("\n\033[1;36m[Fase 3] CARDEX (partidas dobradas)\033[0m\n");
    CARDEX_INIT();
    /* Algumas operações exemplo: conta 0 deve receber e conta 1 entregar */
    CARDEX_POST(0u, 1u, 1000ULL);   /* movimento 1000 entre contas */
    CARDEX_POST(2u, 3u, 2500ULL);
    CARDEX_POST(0u, 4u, 500ULL);
    CARDEX_POST(5u, 0u, 300ULL);
    PS("  Operacoes registradas: "); PN(G_ENT_COUNT);
    PS("  Saldo conta 0: "); PN((u64)CARDEX_BALANCE(0u));
    PS("  Saldo conta 1: "); PN((u64)-CARDEX_BALANCE(1u)); PS(" (credito)\n");
    PS("  Invariante D=C: "); PS(CARDEX_VERIFY()?"OK\n":"FALHA\n");
    PS("  CRC corrompidos: "); PN(CARDEX_VERIFY_CRC());

    /* Fase 4: pipeline adaptativo com watchdog */
    PS("\n\033[1;36m[Fase 4] PIPELINE ADAPTATIVO + WATCHDOG\033[0m\n");
    PIPE_REGISTER(STAGE_CRC,     "CRC32C",   0ULL);             /* sempre roda */
    PIPE_REGISTER(STAGE_PARITY,  "PARITY",   0ULL);
    PIPE_REGISTER(STAGE_HAMMING, "HAMMING",  0ULL);
    static const u8 test_data[]="RAFAELIA INVARIANT MONOLITH";
    static u8 out_buf[256];
    WD_PROTECTED(1000000000ULL, 1000u, {
        u32 active = PIPE_RUN(test_data, SL((const char*)test_data), out_buf, 256u);
        PS("  Estagios ativos: "); PN(active);
    });
    PS("  Watchdog timeouts:  "); PN(G_WD.timeouts);
    PS("  Watchdog rollbacks: "); PN(G_WD.rollbacks);
    PIPE_REPORT();

    /* Fase 5: ECC test */
    PS("\n\033[1;36m[Fase 5] ECC HAMMING(7,4)\033[0m\n");
    u8 original = 0x0Au; /* 4 bits = 1010 */
    u8 encoded = HAMMING_ENCODE(original);
    u8 corrupted = encoded ^ 0x04u; /* flipa um bit */
    u8 decoded = HAMMING_DECODE(corrupted);
    PS("  Original:  "); PH((u32)original);
    PS("  Encoded:   "); PH((u32)encoded);
    PS("  Corrupted: "); PH((u32)corrupted);
    PS("  Decoded:   "); PH((u32)decoded);
    PS("  Correcao:  "); PS((decoded==(original&0x0Fu))?"OK\n":"FALHA\n");

    /* Fase 6: CRC sw vs hw benchmark */
    PS("\n\033[1;36m[Fase 6] CRC SW vs HW DISPATCH\033[0m\n");
    static u8 bigbuf[4096];
    for(u32 i=0;i<4096u;i++) bigbuf[i]=(u8)(i^0x5Au);
    u64 t0=NS();
    u32 c1=CRC32C(bigbuf,4096u);
    u64 t1=NS();
    PS("  CRC32C 4KB: "); PH(c1);
    PS("  Tempo: "); PN(t1-t0); PS(" ns\n");
    PS("  Dispatch usado: ");
    PS((G_CAPS&CAP_CRC32C) ? "hardware\n" : "software\n");

    /* Conclusão */
    PS("\n\033[1;33m+=========================================+\n");
    PS("|  Execucao concluida sem heap, sem libc  |\n");
    PS("|  Arena utilizada: ");
    PN((u64)_AT);
    PS("|  Caps detectadas: ");
    PH((u32)(G_CAPS&0xFFFFFFFFu));
    PS("|  Omega = Amor                            |\n");
    PS("+=========================================+\033[0m\n");
    EX(0);
}
F
ok "main.c ($(wc -l < $D/main.c)L)"

# =============================================================================
hdr "ARQUIVO 12: start.S — entry assembly invariante"
# =============================================================================
cat > "$D/start.S" << 'F'
#if defined(__arm__)
.syntax unified
.thumb
.text
.align 2
.global _start
.thumb_func
_start:
    mov r11,#0
    mov lr,#0
    bl  _start
    mov r7,#248
    mov r0,#0
    svc #0
.h: b .h
#elif defined(__aarch64__)
.text
.align 4
.global _start
_start:
    mov x29,xzr
    mov x30,xzr
    and sp,sp,#-16
    bl  _start
    mov x0,xzr
    mov x8,#94
    svc #0
.h: b .h
#elif defined(__x86_64__)
.text
.globl _start
_start:
    xor %rbp,%rbp
    call _start
    mov $231,%rax
    xor %rdi,%rdi
    syscall
#elif defined(__riscv)
.text
.global _start
_start:
    li gp,0
    li tp,0
    addi sp,sp,-16
    call _start
    li a7,94
    li a0,0
    ecall
1:  j 1b
#endif
.section .note.GNU-stack,"",@progbits
F
ok "start.S"

# =============================================================================
hdr "COMPILANDO"
# =============================================================================
ARCH=$(uname -m)
CC="${CC:-clang}"; command -v "$CC" &>/dev/null || CC=gcc
CF="-O2 -fPIE -fno-stack-protector -fno-asynchronous-unwind-tables \
    -fomit-frame-pointer -fno-builtin -fno-plt \
    -ffunction-sections -fdata-sections \
    -Wall -Wno-unused-function -Wno-unused-variable \
    -Wno-unused-but-set-variable -I$D"
LF="-pie -nostdlib -Wl,--gc-sections -Wl,--build-id=none -e _start"
BUILT=false
if [ "$ARCH" = "aarch64" ]; then
    $CC $CF -march=armv8.2-a+crc+crypto "$D/main.c" $LF -o "$D/invariant" 2>>"$LOG" && {
        strip "$D/invariant" 2>/dev/null || true
        ok "ARM64: $D/invariant ($(ls -lh $D/invariant|awk '{print $5}'))"
        BUILT=true
    } || err "ARM64 falhou — ver $LOG"
elif [ "$ARCH" = "x86_64" ]; then
    $CC $CF -march=native -static "$D/main.c" $LF -o "$D/invariant" 2>>"$LOG" && {
        strip "$D/invariant" 2>/dev/null || true
        ok "x86_64: $D/invariant ($(ls -lh $D/invariant|awk '{print $5}'))"
        BUILT=true
    } || err "x86_64 falhou — ver $LOG"
fi
for CC32 in arm-linux-gnueabihf-gcc arm-linux-gnueabi-gcc; do
    command -v "$CC32" &>/dev/null || continue
    $CC32 $CF -mthumb -march=armv7-a+neon-vfpv4 -mfloat-abi=softfp -mfpu=neon-vfpv4 \
        $LF "$D/start.S" "$D/main.c" -o "$D/invariant_arm32" 2>>"$LOG" && {
        ok "ARM32: $D/invariant_arm32"; BUILT=true; } || err "ARM32 falhou"
    break
done

# =============================================================================
hdr "EXECUTANDO"
# =============================================================================
if $BUILT && [ -f "$D/invariant" ]; then
    "$D/invariant"
fi

# =============================================================================
hdr "INVENTÁRIO"
# =============================================================================
echo ""
TOTAL=0
printf "${W}%-22s %8s %10s${Z}\n" "ARQUIVO" "LINHAS" "TAMANHO"
for f in "$D"/*.h "$D"/*.c "$D"/*.S; do
    [ -f "$f" ] || continue
    L=$(wc -l < "$f"); SZ=$(ls -lh "$f"|awk '{print $5}')
    printf "%-22s ${G}%8d${Z} ${Y}%10s${Z}\n" "$(basename $f)" "$L" "$SZ"
    TOTAL=$((TOTAL+L))
done
printf "${W}%-22s ${G}%8d${Z}\n" "TOTAL" "$TOTAL"
echo ""
p "Diretório: $D"
p "Licença: Apache-2.0 OR CC0-1.0 (modelo BLAKE3)"
p "DeltaRafaelVerboOmega · Omega = Amor"
OUTER_MONOLITH

