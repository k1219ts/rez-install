CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(ExternalProject)

rez_find_packages(PREFIX pkgs AUTO)

if(${REZ_BUILD_INSTALL})
    set(install_cmd make install ${make_arg})
else()
    set(install_cmd "")
endif()

set(CMAKE_ARGS
    -DZLIB_INCLUDE_DIR=${zlib_INCLUDE_DIRS}
    -DZLIB_LIBRARY=${zlib_LIBRARIES}
    -DJPEG_INCLUDE_DIR=${jpeg_INCLUDE_DIRS}
    -DJPEG_LIBRARY=${jpeg_LIBRARIES}
)

ExternalProject_add(
    tiff
    URL "$ENV{SOURCEROOT}/tiff/tiff-4.1.0.tar.gz"
    PREFIX tiff
    CMAKE_ARGS -DCMAKE_INSTALL_PREFIX=${CMAKE_INSTALL_PREFIX} ${CMAKE_ARGS} -DCMAKE_POSITION_INDEPENDENT_CODE=ON
    INSTALL_COMMAND "${install_cmd}"
    BUILD_IN_SOURCE 1
)

rez_install_files(
    cmake/tiff.cmake
    DESTINATION .
)
