CMAKE_MINIMUM_REQUIRED(VERSION 3.2.2)

include(RezBuild)
include(ExternalProject)

if(${REZ_BUILD_INSTALL})
    set(install_cmd make install ${make_args})
else()
    set(install_cmd "")
endif()

ExternalProject_add(
    fmt
    URL "$ENV{SOURCEROOT}/fmt/fmt-6.1.2.zip"
    PREFIX fmt
    CMAKE_ARGS -DCMAKE_INSTALL_PREFIX=${CMAKE_INSTALL_PREFIX}
    INSTALL_COMMAND "${install_cmd}"
)

install(
    CODE
    ""
)
