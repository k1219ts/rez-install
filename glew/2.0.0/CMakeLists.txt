CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(ExternalProject)

if(${REZ_BUILD_INSTALL})
    set(install_cmd make GLEW_DEST=${CMAKE_INSTALL_PREFIX} -j8 install)
else()
    set(install_cmd "")
endif()

ExternalProject_add(
    glew
    URL "$ENV{SOURCEROOT}/glew/glew-2.0.0.tgz"
    PREFIX glew
    CONFIGURE_COMMAND ""
    BUILD_COMMAND ""
    INSTALL_COMMAND "${install_cmd}"
    BUILD_IN_SOURCE 1
)

rez_install_files(
    cmake/glew.cmake
    DESTINATION .
)
