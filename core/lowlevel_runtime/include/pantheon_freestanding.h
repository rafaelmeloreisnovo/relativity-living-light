#ifndef RLL_PANTHEON_FREESTANDING_H
#define RLL_PANTHEON_FREESTANDING_H

#ifdef __cplusplus
extern "C" {
#endif

/*
 * Pantheon autoral: freestanding, sem malloc, sem stdlib.
 * API mínima para hash/CRC e escrita via syscall Linux x86_64.
 */

unsigned long long rll_fnv1a64(const unsigned char *data, unsigned long long len);
unsigned int rll_crc32(const unsigned char *data, unsigned long long len);
long rll_sys_write1(const void *buf, unsigned long long len);

#ifdef __cplusplus
}
#endif

#endif
