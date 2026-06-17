#ifndef RLL_PANTHEON_FREESTANDING_H
#define RLL_PANTHEON_FREESTANDING_H

#ifdef __cplusplus
extern "C" {
#endif

/* Tipos explícitos sem dependência de stdlib/libc. */
typedef unsigned char rll_u8;
typedef unsigned int rll_u32;
typedef unsigned long long rll_u64;
typedef long long rll_i64;

/*
 * Pantheon freestanding low-level runtime (não é dataset Pantheon+ cosmológico).
 * - sem heap/malloc
 * - sem stdlib/stdio/string
 * - FNV-1a 64-bit: hash NÃO criptográfico
 * - CRC-32 IEEE (poly reversed 0xEDB88320)
 */

rll_u64 rll_fnv1a64(const rll_u8 *data, rll_u64 len);
rll_u32 rll_crc32(const rll_u8 *data, rll_u64 len);
rll_i64 rll_sys_write1(const void *buf, rll_u64 len);

#ifdef __cplusplus
}
#endif

#endif
