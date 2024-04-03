#!/bin/bash

if [ $1 = "install" ]; then
    tar -xvzf ${SOURCEROOT}/clang/clang-builder-clang70.tar.gz -C ./
    cp ${REZ_BUILD_SOURCE_PATH}/clang-build-vars.sh ${REZ_BUILD_PATH}/clang-builder-clang70
    cd ${REZ_BUILD_PATH}/clang-builder-clang70
    ./build-clang.sh
fi
