CMAKE_MINIMUM_REQUIRED(VERSION 3.2)

include(RezBuild)
include(ExternalProject)

if(${REZ_BUILD_INSTALL})
    set(install_cmd make install ${make_args})
else()
    set(install_cmd "")
endif()

message("# KatanaUsdPlugins")
set(CMAKE_ARGS
    -DKATANA_API_LOCATION=$ENV{KATANA_ROOT}
    -DUSE_KATANA_THIRDPARTY_LIBS=ON
)

ExternalProject_add(
    usd_katana
    GIT_REPOSITORY git@10.0.0.13:plumber/KatanaUsdPlugins.git
    PREFIX usd_katana
    CMAKE_ARGS -DCMAKE_INSTALL_PREFIX=${CMAKE_INSTALL_PREFIX} ${CMAKE_ARGS}
    INSTALL_COMMAND "${install_cmd}"
    BUILD_IN_SOURCE 1
)

install(
    CODE
    ""
)
