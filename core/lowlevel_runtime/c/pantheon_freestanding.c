#include "pantheon_freestanding.h"

/* FNV-1a 64-bit constants */
#define RLL_FNV_OFFSET 14695981039346656037ull
#define RLL_FNV_PRIME  1099511628211ull

/* Linux x86_64 syscall numbers */
#define RLL_SYS_WRITE 1ull

/*
 * Freestanding FNV-1a: sem heap, sem libc.
 */
unsigned long long rll_fnv1a64(const unsigned char *data, unsigned long long len) {
    unsigned long long h = RLL_FNV_OFFSET;
    unsigned long long i = 0ull;
    while (i < len) {
        h ^= (unsigned long long)data[i];
        h *= RLL_FNV_PRIME;
        i++;
    }
    return h;
}

/*
 * CRC32 bitwise (poly reversed 0xEDB88320), sem lookup table dinâmica.
 */
unsigned int rll_crc32(const unsigned char *data, unsigned long long len) {
    unsigned int crc = 0xFFFFFFFFu;
    unsigned long long i = 0ull;
    while (i < len) {
        unsigned int x = (crc ^ (unsigned int)data[i]) & 0xFFu;
        unsigned int j = 0u;
        while (j < 8u) {
            /* update branchless */
            unsigned int mask = (unsigned int)(-(int)(x & 1u));
            x = (x >> 1u) ^ (0xEDB88320u & mask);
            j++;
        }
        crc = (crc >> 8u) ^ x;
        i++;
    }
    return ~crc;
}

/*
 * syscall write(fd=1, buf, len) em x86_64; wrapper sem branches.
 * Retorna >=0 bytes escritos ou <0 erro do kernel.
 */
long rll_sys_write1(const void *buf, unsigned long long len) {
#if defined(__x86_64__) || defined(_M_X64)
    unsigned long long ret;
    __asm__ volatile(
        "syscall"
        : "=a"(ret)
        : "a"(RLL_SYS_WRITE), "D"(1ull), "S"(buf), "d"(len)
        : "rcx", "r11", "memory"
    );
    return (long)ret;
#else
    (void)buf;
    (void)len;
    return -38; /* ENOSYS */
#endif
}
