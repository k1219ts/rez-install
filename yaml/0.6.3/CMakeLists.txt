CMAKE_MINIMUM_REQUIRED(VERSION 3.10)

include(RezBuild)
include(ExternalProject)

set(make_arg -j32)

if(${REZ_BUILD_INSTALL})
    set(install_cmd make install ${make_arg})
else()
    set(install_cmd "")
endif()

set(CMAKE_ARGS
    -DYAML_BUILD_SHARED_LIBS=ON
    -DYAML_CPP_BUILD_TESTS=OFF
    -DYAML_CPP_BUILD_TOOLS=OFF
)

ExternalProject_add(
    yaml
    URL "$ENV{SOURCEROOT}/yaml-cpp/yaml-cpp-yaml-cpp-0.6.3.tar.gz"
    PREFIX yaml
    CMAKE_ARGS -DCMAKE_INSTALL_PREFIX=${CMAKE_INSTALL_PREFIX} ${CMAKE_ARGS}
    INSTALL_COMMAND ${install_cmd}
)

install(
    CODE
    ""
)
