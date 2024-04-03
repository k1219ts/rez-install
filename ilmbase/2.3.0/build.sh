#!/bin/bash

BUILD_PATH=$1
echo "[BUILD_PATH  ] ${BUILD_PATH}"
echo "[INSTALL_PATH] ${REZ_BUILD_INSTALL_PATH}"

cd ${BUILD_PATH}

make -j32
