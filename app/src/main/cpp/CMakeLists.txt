cmake_minimum_required(VERSION 3.22.1)
project(rll_kernel_bridge C)

add_library(rll_kernel_bridge SHARED
    rll_jni.c
    ../../../../core/lowlevel_runtime/c/kernel_bridge.c
)

target_include_directories(rll_kernel_bridge PRIVATE
    ../../../../core/lowlevel_runtime/include
)

target_compile_features(rll_kernel_bridge PRIVATE c_std_99)
target_compile_options(rll_kernel_bridge PRIVATE
    -Wall
    -Wextra
    -Werror
    -fno-exceptions
    -fno-unwind-tables
    -fno-asynchronous-unwind-tables
)
