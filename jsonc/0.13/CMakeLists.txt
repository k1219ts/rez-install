CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(ExternalProject)

if(${REZ_BUILD_INSTALL})
    set(install_cmd make install ${make_arg})
else()
    set(install_cmd "")
endif()

ExternalProject_add(
    jsonc
    URL "$ENV{SOURCEROOT}/jsonc/json-c-json-c-0.13.zip"
    CONFIGURE_COMMAND ./configure --prefix=${CMAKE_INSTALL_PREFIX}
    INSTALL_COMMAND "${install_cmd}"
    BUILD_IN_SOURCE 1
)

install(
    CODE
    ""
)
