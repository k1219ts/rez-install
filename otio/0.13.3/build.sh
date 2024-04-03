#!/bin/bash

if [ $1 = "install" ]; then
    echo "## BASH INSTALL"

    tar -xvzf ${SOURCEROOT}/otio/OpenTimelineIO-v0.13.3.tar.gz -C ./
    unzip ${SOURCEROOT}/otio/pyaaf2-1.4.0.zip -d ./

    export PYTHONPATH=${REZ_BUILD_INSTALL_PATH}/lib/python2.7/site-packages
    mkdir -p ${REZ_BUILD_INSTALL_PATH}/lib/python2.7/site-packages

    cd ${REZ_BUILD_PATH}/OpenTimelineIO
    python setup.py install --prefix=${REZ_BUILD_INSTALL_PATH} --cxx-install-root=${REZ_BUILD_INSTALL_PATH}

    cd ${REZ_BUILD_PATH}/pyaaf2-1.4.0
    python setup.py install --prefix=${REZ_BUILD_INSTALL_PATH}
fi
