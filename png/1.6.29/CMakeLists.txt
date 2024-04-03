CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(ExternalProject)

if(${REZ_BUILD_INSTALL})
    set(install_cmd make install ${make_arg})
else()
    set(install_cmd "")
endif()

ExternalProject_add(
    png
    URL "$ENV{SOURCEROOT}/png/libpng-1.6.29.tar.gz"
    PREFIX png
    CMAKE_ARGS -DCMAKE_INSTALL_PREFIX=${CMAKE_INSTALL_PREFIX} -DCMAKE_POSITION_INDEPENDENT_CODE=ON
    INSTALL_COMMAND "${install_cmd}"
    BUILD_IN_SOURCE 0
)

rez_install_files(
    cmake/png.cmake
    DESTINATION .
)
