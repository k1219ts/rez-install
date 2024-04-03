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
    ilmbase
    URL "$ENV{SOURCEROOT}/ilmbase/ilmbase-2.2.0.tar.gz"
    PREFIX ilmbase
    UPDATE_COMMAND ""
    CONFIGURE_COMMAND ./configure --prefix=${CMAKE_INSTALL_PREFIX}
    BUILD_COMMAND make ${make_arg}
    INSTALL_COMMAND "${install_cmd}"
    BUILD_IN_SOURCE 1
)

install(
    CODE
    ""
)
