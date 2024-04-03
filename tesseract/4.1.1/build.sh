#!/bin/bash

if [ $1 == "install" ]; then
    tar -xvzf ${SOURCEROOT}/tesseract/tesseract-4.1.1.tar.gz -C ./
    cd ${REZ_BUILD_PATH}/tesseract-4.1.1
    ./autogen.sh
    ./configure --with-extra-libraries=${REZ_LEPTONICA_ROOT}/lib --prefix=${REZ_BUILD_INSTALL_PATH}
    make -j32
    make install
fi
