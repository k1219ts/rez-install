CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(ExternalProject)

if(${REZ_BUILD_INSTALL})
    set(install_cmd make install ${make_arg})
else()
    set(install_cmd "")
endif()

ExternalProject_add(
    tiff
    URL "$ENV{SOURCEROOT}/tiff/tiff-4.0.7.zip"
    PREFIX tiff
    CMAKE_ARGS -DCMAKE_INSTALL_PREFIX=${CMAKE_INSTALL_PREFIX}
    INSTALL_COMMAND "${install_cmd}"
    BUILD_IN_SOURCE 0
)

rez_install_files(
    cmake/tiff.cmake
    DESTINATION .
)
