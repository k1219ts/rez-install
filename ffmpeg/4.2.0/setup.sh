#!/bin/bash

ROOTDIR=${SOURCEROOT}/ffmpeg

# tar
sources=("yasm-1.3.0.tar.gz" "faac-1.29.9.2.tar.gz"
         "faad2-2.8.8.tar.gz" "lame-3.100.tar.gz" "opus-1.3.1.tar.gz" "libdv-1.0.0.tar.gz"
         "xvidcore-1.3.2.tar.gz" "libquicktime-1.2.4.tar.gz")
for src in "${sources[@]}"; do
    cp ${ROOTDIR}/${src} ./
    tar -xzf ${src}
done
sources=("nasm-2.14.02.tar.bz2" "x265_3.2.1.tar.gz")
for src in "${sources[@]}"; do
    cp ${ROOTDIR}/${src} ./
    tar -xf ${src}
done

# zip
sources=("x264-master.zip" "fdk-aac-2.0.1.zip" "FFmpeg-release-4.2.zip")
for src in "${sources[@]}"; do
    cp ${ROOTDIR}/${src} ./
    unzip -q ${src}
done

# libquicktime patch
cp ${ROOTDIR}/libquicktime-1.2.4-ffmpeg4-1.patch ./
cd libquicktime-1.2.4
patch -Np1 -i ../libquicktime-1.2.4-ffmpeg4-1.patch

cd ..
