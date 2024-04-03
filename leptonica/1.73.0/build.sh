#!/bin/bash

if [ $1 == "install" ]; then
    tar -xvzf ${SOURCEROOT}/leptonica/leptonica-1.73.tar.gz -C ./
    cd ${REZ_BUILD_PATH}/leptonica-1.73
    chmod 777 configure
    ./configure --prefix=${REZ_BUILD_INSTALL_PATH}
    make -j32
    make install
fi
