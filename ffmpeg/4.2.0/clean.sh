#!/bin/bash

# tar
sources=("nasm" "yasm" "x265" "faac" "faad2" "lame" "opus" "libdv" "xvidcore" "libquicktime"
         "x264" "fdk-aac" "FFmpeg")
for src in "${sources[@]}"; do
    rm -rf ${REZ_BUILD_PATH}/${src}*
done
