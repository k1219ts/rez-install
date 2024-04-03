CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(ExternalProject)

if(${REZ_BUILD_INSTALL})
    set(install_cmd make install ${make_arg})
else()
    set(install_cmd "")
endif()

ExternalProject_add(
    blosc
    URL "$ENV{SOURCEROOT}/blosc/c-blosc-v1.17.0.zip"
    PREFIX blosc
    CMAKE_ARGS -DCMAKE_INSTALL_PREFIX=${CMAKE_INSTALL_PREFIX}
    INSTALL_COMMAND "${install_cmd}"
)

install (
    CODE
    ""
)
