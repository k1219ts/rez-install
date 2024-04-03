CMAKE_MINIMUM_REQUIRED(VERSION 3.10)

include(RezBuild)
include(ExternalProject)

if(${REZ_BUILD_INSTALL})
    set(install_cmd make install ${make_arg})
else()
    set(install_cmd "")
endif()

set(CMAKE_ARGS
    -DBUILD_SHARED_LIBS=ON
    -DCMAKE_CXX_FLAGS="-fPIC"
)

ExternalProject_add (
    pystring
    URL "$ENV{SOURCEROOT}/pystring/pystring-master.zip"
    PREFIX pystring
    UPDATE_COMMAND bash ${CMAKE_SOURCE_DIR}/update.sh
    CMAKE_ARGS -DCMAKE_INSTALL_PREFIX=${CMAKE_INSTALL_PREFIX} ${CMAKE_ARGS}
    INSTALL_COMMAND ${install_cmd}
    ALWAYS 1
)

install(
    CODE
    ""
)
