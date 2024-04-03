#!/bin/bash

# echo ">>>> ${REZ_BUILD_PATH}"

BUILD_PATH=$1
echo "[BUILD_PATH  ] ${BUILD_PATH}"
echo "[INSTALL_PATH] ${REZ_BUILD_INSTALL_PATH}"

cd ${BUILD_PATH}

./bootstrap

./configure \
    --prefix=${REZ_BUILD_INSTALL_PATH} \
    CFLAGS="-fPIC" \
    CXXFLAGS="-fPIC" \
    --with-pic
