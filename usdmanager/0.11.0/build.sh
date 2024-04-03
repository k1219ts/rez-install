#!/bin/bash

if [ $1 = "install" ]; then
    echo "## BASH INSTALL"

    tar -xvzf ${SOURCEROOT}/usdmanager/Qt.py-1.2.5.tar.gz -C ./
    tar -xvzf ${SOURCEROOT}/usdmanager/usdmanager-0.11.0.tar.gz -C ./

    export PYTHONPATH=${REZ_BUILD_INSTALL_PATH}/lib/python2.7/site-packages
    mkdir -p ${REZ_BUILD_INSTALL_PATH}/lib/python2.7/site-packages

    cd ${REZ_BUILD_PATH}/Qt.py-1.2.5
    python setup.py install --prefix=${REZ_BUILD_INSTALL_PATH}

    cd ${REZ_BUILD_PATH}/usdmanager-0.11.0
    python setup.py install --prefix=${REZ_BUILD_INSTALL_PATH}
fi
