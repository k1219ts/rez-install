CMAKE_MINIMUM_REQUIRED(VERSION 3.12.4)

include(RezBuild)
include(ExternalProject)

rez_find_packages(PREFIX pkgs AUTO)

if(${REZ_BUILD_INSTALL})
    set(install_cmd make install ${make_args})
else()
    set(install_cmd "")
endif()

set(CMAKE_ARGS
    -DOIIO_BUILD_TOOLS=0
    -DOIIO_BUILD_TESTS=0
    -DUSE_PYTHON=0
    -DSTOP_ON_WARNING=0
    -DFMT_ROOT=$ENV{REZ_FMT_ROOT}
    -DFMT_INCLUDE_DIR=$ENV{REZ_FMT_ROOT}/include
    -DROBINMAP_INCLUDE_DIR=$ENV{REZ_ROBIN_MAP_ROOT}/include
    -DOPENEXR_HOME=$ENV{REZ_OPENEXR_ROOT}
    -DOpenColorIO_ROOT=$ENV{REZ_OCIO_ROOT}
    -DJPEGTurbo_ROOT=$ENV{REZ_JPEG_ROOT}
    -DZLIB_INCLUDE_DIR=${zlib_INCLUDE_DIRS}
    -DZLIB_LIBRARY=${zlib_LIBRARIES}
    -DPNG_INCLUDE_DIR=${png_INCLUDE_DIRS}
    -DPNG_LIBRARY=${png_LIBRARIES}
    -DTIFF_INCLUDE_DIR=${tiff_INCLUDE_DIRS}
    -DTIFF_LIBRARY=${tiff_LIBRARIES}
    -DENABLE_Field3D=0
    -DENABLE_LIBSQUISH=0
    -DENABLE_OpenGL=0
    -DENABLE_Qt5=0
    -DENABLE_OpenVDB=0
)

ExternalProject_add(
    oiio
    URL "$ENV{SOURCEROOT}/oiio/oiio-Release-2.1.16.0.tar.gz"
    PREFIX oiio
    CMAKE_ARGS -DCMAKE_INSTALL_PREFIX=${CMAKE_INSTALL_PREFIX} ${CMAKE_ARGS}
    INSTALL_COMMAND "${install_cmd}"
)

rez_install_files(
    cmake/oiio.cmake
    DESTINATION .
)
