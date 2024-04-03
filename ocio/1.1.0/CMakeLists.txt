CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(ExternalProject)

rez_find_packages(PREFIX pkgs AUTO)

if(${REZ_BUILD_INSTALL})
    set(install_cmd make install ${make_arg})
else()
    set(install_cmd "")
endif()

ExternalProject_add(
    ocio
    URL "$ENV{SOURCEROOT}/ocio/OpenColorIO-1.1.0-patch.tar.gz"
    PREFIX ocio
    CMAKE_ARGS -DCMAKE_INSTALL_PREFIX=${CMAKE_INSTALL_PREFIX} -DPYTHON_INCLUDE_DIR=${python_INCLUDE_DIR} -DPYTHON_LIBRARY=${python_LIBRARY}
    INSTALL_COMMAND "${install_cmd}"
    ALWAYS 1
)

rez_install_files(
    cmake/ocio.cmake
    DESTINATION .
)
