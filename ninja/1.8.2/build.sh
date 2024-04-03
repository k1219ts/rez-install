#!/bin/bash

if [ $1 == "install" ]; then
    tar -xvzf ${SOURCEROOT}/ninja/ninja-1.8.2.tar.gz -C ./
    cd ${REZ_BUILD_PATH}/ninja-1.8.2
    ./bootstrap.py
    mkdir -p ${REZ_BUILD_INSTALL_PATH}/bin
    cp ${REZ_BUILD_PATH}/ninja-1.8.2/ninja ${REZ_BUILD_INSTALL_PATH}/bin
fi
