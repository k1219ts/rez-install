CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(ExternalProject)

if(${REZ_BUILD_INSTALL})
    set(install_cmd make install ${make_arg})
else()
    set(install_cmd "")
endif()

ExternalProject_add(
    jemalloc
    URL "$ENV{SOURCEROOT}/jemalloc/jemalloc-4.5.0.tar.bz2"
    PREFIX jemalloc
    UPDATE_COMMAND ""
    CONFIGURE_COMMAND ./configure --prefix=${CMAKE_INSTALL_PREFIX}
    BUILD_COMMAND ""
    INSTALL_COMMAND "${install_cmd}"
    BUILD_IN_SOURCE 1
)

install(
    CODE
    ""
)
