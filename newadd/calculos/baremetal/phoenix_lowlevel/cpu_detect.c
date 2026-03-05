#include <stdint.h>
#include <stdio.h>

#if defined(__x86_64__) || defined(_M_X64)
#define PHX_ARCH "x86_64"
#elif defined(__aarch64__)
#define PHX_ARCH "aarch64"
#else
#define PHX_ARCH "generic"
#endif

struct phx_cpu_caps {
    uint32_t arch_id;
    uint32_t has_simd;
    uint32_t has_avx2;
    uint32_t has_neon;
};

#if defined(__x86_64__) || defined(_M_X64)
static void phx_cpuid(uint32_t leaf, uint32_t subleaf, uint32_t *a, uint32_t *b, uint32_t *c, uint32_t *d) {
    __asm__ volatile (
        "cpuid"
        : "=a"(*a), "=b"(*b), "=c"(*c), "=d"(*d)
        : "a"(leaf), "c"(subleaf)
    );
}
#endif

void phx_detect_caps(struct phx_cpu_caps *out) {
    out->arch_id = 0u;
    out->has_simd = 0u;
    out->has_avx2 = 0u;
    out->has_neon = 0u;

#if defined(__x86_64__) || defined(_M_X64)
    uint32_t a, b, c, d;
    out->arch_id = 1u;
    phx_cpuid(1u, 0u, &a, &b, &c, &d);
    out->has_simd = (d >> 25) & 1u;
    phx_cpuid(7u, 0u, &a, &b, &c, &d);
    out->has_avx2 = (b >> 5) & 1u;
#elif defined(__aarch64__)
    out->arch_id = 2u;
    out->has_simd = 1u;
    out->has_neon = 1u;
#else
    out->arch_id = 255u;
#endif
}

int main(void) {
    struct phx_cpu_caps caps;
    phx_detect_caps(&caps);
    printf("arch=%s arch_id=%u simd=%u avx2=%u neon=%u\n",
           PHX_ARCH,
           caps.arch_id,
           caps.has_simd,
           caps.has_avx2,
           caps.has_neon);
    return 0;
}
