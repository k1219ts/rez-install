CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(ExternalProject)

if(${REZ_BUILD_INSTALL})
    set(install_cmd make install ${make_arg})
else()
    set(install_cmd "")
endif()

ExternalProject_add(
    jpeg
    URL "$ENV{SOURCEROOT}/jpeg/libjpeg-turbo-1.5.3.tar.gz"
    PREFIX jpeg
    UPDATE_COMMAND autoreconf -ivf
    CONFIGURE_COMMAND ./configure --prefix=${CMAKE_INSTALL_PREFIX} --disable-static --enable-shared
    INSTALL_COMMAND "${install_cmd}"
    ALWAYS 1
    BUILD_IN_SOURCE 1
)

rez_install_files(
    cmake/jpeg.cmake cmake/FindJPEG.cmake
    DESTINATION .
)
