CMAKE_MINIMUM_REQUIRED(VERSION 3.2)

include(RezBuild)
include(ExternalProject)

if(${REZ_BUILD_INSTALL})
    set(install_cmd make install ${make_args})
else()
    set(install_cmd "")
endif()

set(CMAKE_ARGS
    -DBUILD_USD_PLUGIN=ON
    -DCMAKE_BUILD_TYPE=release
    -DENABLE_TESTS=OFF
)

ExternalProject_add(
    draco
    URL "$ENV{SOURCEROOT}/draco/draco-1.3.6.tar.gz"
    PREFIX draco
    CMAKE_ARGS -DCMAKE_INSTALL_PREFIX=${CMAKE_INSTALL_PREFIX} ${CMAKE_ARGS}
    INSTALL_COMMAND "${install_cmd}"
)

install(
    CODE
    ""
)
