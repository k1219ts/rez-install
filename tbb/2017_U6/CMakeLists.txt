CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(ExternalProject)

set(make_arg -j32)

ExternalProject_add(
    tbb
    URL "$ENV{SOURCEROOT}/tbb/oneTBB-2017_U6.tar.gz"
    PREFIX tbb
    CONFIGURE_COMMAND ""
    BUILD_COMMAND make ${make_arg}
    INSTALL_COMMAND ${CMAKE_CURRENT_SOURCE_DIR}/copy_files.sh ${CMAKE_CURRENT_BINARY_DIR}/tbb/src/tbb ${CMAKE_INSTALL_PREFIX}
    BUILD_IN_SOURCE 1
)

rez_install_files(
    cmake/tbb.cmake
    DESTINATION .
)
