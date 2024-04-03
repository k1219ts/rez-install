#!/bin/bash

if [ $1 == "install" ]; then
    tar -xvzf ${SOURCEROOT}/tesseract/tesseract-3.04.01.tar.gz -C ./
    cd ${REZ_BUILD_PATH}/tesseract-3.04.01
    ./autogen.sh
    ./configure --with-extra-libraries=${REZ_LEPTONICA_ROOT}/lib --prefix=${REZ_BUILD_INSTALL_PATH}
    make -j32
    make install
fi
