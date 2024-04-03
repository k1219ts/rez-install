#!/bin/bash

if [ $1 == "install" ]; then
    tar -xvzf ${SOURCEROOT}/usd_mari/MariUsdPlugins-20200715.tar.gz -C ./
    mkdir -p ${REZ_BUILD_PATH}/MariUsdPlugins-master/build
    cd ${REZ_BUILD_PATH}/MariUsdPlugins-master/build
    cmake -G Ninja -D CMAKE_MAKE_PROGRAM:FILEPATH=${REZ_NINJA_ROOT}/bin/ninja -DCMAKE_BUILD_TYPE=Release -DTBB_ROOT_DIR=${REZ_TBB_ROOT} -DCMAKE_INSTALL_PREFIX=${REZ_BUILD_INSTALL_PATH} ../
    ninja install
fi
