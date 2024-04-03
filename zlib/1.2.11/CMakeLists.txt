CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(ExternalProject)

if(${REZ_BUILD_INSTALL})
    set(install_cmd make install ${make_arg})
else()
    set(install_cmd "")
endif()

ExternalProject_add(
    zlib
    URL "${SOURCEROOT}/zlib/zlib-v1.2.11.zip"
    PREFIX zlib
    CMAKE_ARGS -DCMAKE_INSTALL_PREFIX=${CMAKE_INSTALL_PREFIX} -DCMAKE_POSITION_INDEPENDENT_CODE=ON
    INSTALL_COMMAND "${install_cmd}"
    ALWAYS 1
    BUILD_IN_SOURCE 0
)

rez_install_files(
    cmake/zlib.cmake
    DESTINATION .
)
