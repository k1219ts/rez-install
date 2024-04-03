#!/bin/bash

if [ $1 = "install" ]; then
    unzip ${SOURCEROOT}/pyside2/pyside-setup-everywhere-src-5.12.6.zip -d ./
    cd ${REZ_BUILD_PATH}/pyside-setup-everywhere-src-5.12.6
    python setup.py build --qmake=${REZ_QT_ROOT}/bin/qmake --parallel=32 --build-tests
    cp -rv ${REZ_BUILD_PATH}/pyside-setup-everywhere-src-5.12.6/pyside2_install/py2.7-qt5.12.6-64bit-release/* ${REZ_BUILD_INSTALL_PATH}
fi
