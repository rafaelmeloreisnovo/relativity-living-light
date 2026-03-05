.text
.global rll_arch_detect_x86_64
.type rll_arch_detect_x86_64, @function
rll_arch_detect_x86_64:
    mov $1, %eax
    cpuid
    mov $64, %eax
    ret
