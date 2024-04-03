CMAKE_MINIMUM_REQUIRED(VERSION 3.6)

include(RezBuild)
include(ExternalProject)

if(${REZ_BUILD_INSTALL})
    set(install_cmd make install ${make_args})
else()
    set(install_cmd "")
endif()

ExternalProject_add(
    usd_houdini
    URL "$ENV{HFS}/toolkit/usd_houdini_plugins"
    PREFIX usd_houdini
    UPDATE_COMMAND "${CMAKE_CURRENT_SOURCE_DIR}/source_update.sh"
    CMAKE_ARGS -DCMAKE_INSTALL_PREFIX=${CMAKE_INSTALL_PREFIX}
    INSTALL_COMMAND "${install_cmd}"
)

install(
    FILES
    /root/houdini17.5/dso/OP_gusd.so
    DESTINATION dso/
)
