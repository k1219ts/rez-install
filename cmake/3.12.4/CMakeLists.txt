CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(ExternalProject)

set(cmake_version ${CMAKE_VERSION})
set(cmake_short_version ${CMAKE_MAJOR_VERSION}.${CMAKE_MINOR_VERSION})

if(${REZ_BUILD_INSTALL})
    set(install_cmd make install ${make_arg})
else()
    set(install_cmd "")
endif()

ExternalProject_add(
    cmake
    URL "$ENV{SOURCEROOT}/cmake/cmake-3.12.4.tar.gz"
    PREFIX cmake
    CONFIGURE_COMMAND ./configure --prefix=${CMAKE_INSTALL_PREFIX}
    BUILD_COMMAND make
    INSTALL_COMMAND "${install_cmd}"
    BUILD_IN_SOURCE 1
)

rez_install_files(
    cmake/cmake.cmake
    DESTINATION .
)
