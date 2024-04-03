#!/bin/bash

echo "bash based build"

bash ${REZ_BUILD_SOURCE_PATH}/setup.sh

export PATH=${REZ_BUILD_INSTALL_PATH}/bin:$PATH
export LD_LIBRARY_PATH=${REZ_BUILD_INSTALL_PATH}/lib:${LD_LIBRARY_PATH}
export PKG_CONFIG_PATH=${REZ_BUILD_INSTALL_PATH}/lib/pkgconfig:${PKG_CONFIG_PATH}

# NASM
cd ${REZ_BUILD_PATH}/nasm-2.14.02
./autogen.sh
./configure --prefix=${REZ_BUILD_INSTALL_PATH} --bindir=${REZ_BUILD_INSTALL_PATH}/bin
make -j32
make install

# Yasm
cd ${REZ_BUILD_PATH}/yasm-1.3.0
./configure --prefix=${REZ_BUILD_INSTALL_PATH} --bindir=${REZ_BUILD_INSTALL_PATH}/bin
make -j32
make install

# libx264
cd ${REZ_BUILD_PATH}/x264-master
./configure --prefix=${REZ_BUILD_INSTALL_PATH} --bindir=${REZ_BUILD_INSTALL_PATH}/bin --enable-static --enable-pic
make -j32
make install

# libx265
cd ${REZ_BUILD_PATH}/x265_3.2.1/build/linux
cmake -G "Unix Makefiles" -DCMAKE_INSTALL_PREFIX=${REZ_BUILD_INSTALL_PATH} -DENABLE_SHARED:bool=off ../../source
make -j32
make install

# FAAC
cd ${REZ_BUILD_PATH}/faac-1.29.9.2
./configure --prefix=${REZ_BUILD_INSTALL_PATH} --disable-static --with-pic
make -j32
make install

# FAAD2
cd ${REZ_BUILD_PATH}/faad2-2.8.8
./configure --prefix=${REZ_BUILD_INSTALL_PATH} --disable-static --with-pic
make -j32
make install

# libfdk_aac
cd ${REZ_BUILD_PATH}/fdk-aac-2.0.1
autoreconf -fiv
./configure --prefix=${REZ_BUILD_INSTALL_PATH} --disable-static --with-pic
make -j32
make install

# libmp3lame
cd ${REZ_BUILD_PATH}/lame-3.100
./configure --prefix=${REZ_BUILD_INSTALL_PATH} --bindir=${REZ_BUILD_INSTALL_PATH}/bin --enable-mp3rtp --disable-static --enable-nasm
make -j32
make install

# libopus
cd ${REZ_BUILD_PATH}/opus-1.3.1
./configure --prefix=${REZ_BUILD_INSTALL_PATH} --disable-static --with-pic
make -j32
make install

# libdv
cd ${REZ_BUILD_PATH}/libdv-1.0.0
./configure --prefix=${REZ_BUILD_INSTALL_PATH} --disable-xv --disable-static
make -j32
make install

# xvid
cd ${REZ_BUILD_PATH}/xvidcore/build/generic
./configure --prefix=${REZ_BUILD_INSTALL_PATH} --bindir=${REZ_BUILD_INSTALL_PATH}/bin
make -j32
make install

# FFMPEG
cd ${REZ_BUILD_PATH}/FFmpeg-release-4.2
./configure \
    --prefix=${REZ_BUILD_INSTALL_PATH} \
    --pkg-config-flags="--static" \
    --extra-cflags="-I${REZ_BUILD_INSTALL_PATH}/include -fPIC" \
    --extra-ldflags="-L${REZ_BUILD_INSTALL_PATH}/lib -Wl,-Bsymbolic" \
    --extra-libs="-lpthread -lm" \
    --enable-gpl \
    --enable-version3 \
    --enable-nonfree \
    --enable-libfdk-aac \
    --enable-libfreetype \
    --enable-libmp3lame \
    --enable-libopus \
    --enable-libx264 \
    --enable-libx265 \
    --enable-libxcb \
    --enable-postproc \
    --enable-shared
make -j32
make install

# libquicktime
cd ${REZ_BUILD_PATH}/libquicktime-1.2.4
make clean
PKG_CONFIG_PATH="${REZ_BUILD_INSTALL_PATH}/lib/pkgconfig" ./configure --prefix=${REZ_BUILD_INSTALL_PATH} --bindir=${REZ_BUILD_INSTALL_PATH}/bin --enable-gpl --with-libdv
make -j32
make install

bash ${REZ_BUILD_SOURCE_PATH}/clean.sh
