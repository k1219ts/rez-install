CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(ExternalProject)

if(${REZ_BUILD_INSTALL})
    set(install_cmd make install ${make_arg})
else()
    set(install_cmd "")
endif()

# set(SIP_CONFIG_ARGS
#     --sip-module=PyQt5.sip
#     --bindir=${CMAKE_INSTALL_PREFIX}/bin
#     --destdir=${CMAKE_INSTALL_PREFIX}/lib64/python2.7/site-packages
#     --incdir=${CMAKE_INSTALL_PREFIX}/include
# )
#
# ExternalProject_add(
#     sip
#     URL "$ENV{SOURCEROOT}/sip/sip-4.19.14.tar.gz"
#     PREFIX sip
#     CONFIGURE_COMMAND python configure.py ${SIP_CONFIG_ARGS}
#     INSTALL_COMMAND "${install_cmd}"
#     BUILD_IN_SOURCE 1
# )

set(PYQT_CONFIG_ARGS
    --confirm-license
    --disable=QtNfc
    --bindir=${CMAKE_INSTALL_PREFIX}/bin
    --destdir=${CMAKE_INSTALL_PREFIX}/lib64/python2.7/site-packages
    --sip=${CMAKE_INSTALL_PREFIX}/bin/sip
    --sip-incdir=${CMAKE_INSTALL_PREFIX}/include
    --sipdir=${CMAKE_INSTALL_PREFIX}/lib64/python2.7/site-packages/PyQt5
)

ExternalProject_add(
    pyqt5
    URL "$ENV{SOURCEROOT}/pyqt5/PyQt5_gpl-5.12.2.tar.gz"
    PREFIX pyqt5
    CONFIGURE_COMMAND python configure.py ${PYQT_CONFIG_ARGS}
    INSTALL_COMMAND "${install_cmd}"
    BUILD_IN_SOURCE 1
)

install(
    CODE
    ""
)
