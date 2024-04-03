CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(ExternalProject)

if(${REZ_BUILD_INSTALL})
    set(install_cmd make install ${make_args})
else()
    set(install_cmd "")
endif()

set(CMAKE_ARGS
    -DRAPIDJSON_BUILD_TESTS=OFF
)

ExternalProject_add(
    rapidjson
    URL "$ENV{SOURCEROOT}/rapidjson/rapidjson-1.1.0.zip"
    PREFIX rapidjson
    CMAKE_ARGS -DCMAKE_INSTALL_PREFIX=${CMAKE_INSTALL_PREFIX} ${CMAKE_ARGS}
    INSTALL_COMMAND ${install_cmd}
)

install(
    CODE
    ""
)
