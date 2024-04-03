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
    URL "$ENV{SOURCEROOT}/robin_map/robin-map-0.6.2.tar.gz"
    PREFIX fmt
    CMAKE_ARGS -DCMAKE_INSTALL_PREFIX=${CMAKE_INSTALL_PREFIX}
    INSTALL_COMMAND "${install_cmd}"
)

install(
    CODE
    ""
)
