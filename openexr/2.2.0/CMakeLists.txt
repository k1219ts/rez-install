CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(ExternalProject)

set(make_arg -j32)

if(${REZ_BUILD_INSTALL})
    set(install_cmd make install ${make_arg})
else()
    set(install_cmd "")
endif()

ExternalProject_add(
    openexr
    URL "$ENV{SOURCEROOT}/openexr/openexr-2.2.0.tar.gz"
    PREFIX openexr
    UPDATE_COMMAND ""
    CONFIGURE_COMMAND ./configure --prefix=${CMAKE_INSTALL_PREFIX}
    BUILD_COMMAND "${install_cmd}"
    INSTALL_COMMAND ${CMAKE_CURRENT_SOURCE_DIR}/link_files.sh
    BUILD_IN_SOURCE 1
)

install(
    CODE
    ""
)
