CMAKE_MINIMUM_REQUIRED(VERSION 3.2.2)

include(RezBuild)
include(ExternalProject)

rez_find_packages(PREFIX pkgs AUTO)

if(${REZ_BUILD_INSTALL})
    set(install_cmd make install ${make_args})
else()
    set(install_cmd "")
endif()

set(CMAKE_ARGS
    -DOIIO_BUILD_TOOLS=OFF
    -DOIIO_BUILD_TESTS=OFF
    -DUSE_PYTHON=OFF
    -DSTOP_ON_WARNING=OFF
    -DOPENEXR_HOME=$ENV{REZ_OPENEXR_ROOT}
    -DOCIO_PATH=$ENV{REZ_OCIO_ROOT}
    -DUSE_JPEGTURBO=ON
    -DJPEGTURBO_PATH=$ENV{REZ_JPEG_ROOT}
    -DZLIB_INCLUDE_DIR=${zlib_INCLUDE_DIRS}
    -DZLIB_LIBRARY=${zlib_LIBRARIES}
    -DPNG_INCLUDE_DIR=${png_INCLUDE_DIRS}
    -DPNG_LIBRARY=${png_LIBRARIES}
    -DTIFF_INCLUDE_DIR=${tiff_INCLUDE_DIRS}
    -DTIFF_LIBRARY=${tiff_LIBRARIES}
    -DUSE_OPENGL=OFF
    -DUSE_QT=OFF
    -DUSE_PTEX=OFF
)

ExternalProject_add(
    oiio
    URL "$ENV{SOURCEROOT}/oiio/oiio-Release-1.8.9.tar.gz"
    PREFIX oiio
    CMAKE_ARGS -DCMAKE_INSTALL_PREFIX=${CMAKE_INSTALL_PREFIX} ${CMAKE_ARGS}
    INSTALL_COMMAND "${install_cmd}"
)

rez_install_files(
    cmake/oiio.cmake
    DESTINATION .
)
