CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(ExternalProject)

if(${REZ_BUILD_INSTALL})
    set(install_cmd make install ${make_arg})
else()
    set(install_cmd "")
endif()

set(CMAKE_ARGS
    -DBUILD_TESTING=OFF
    -DHDF5_BUILD_TOOLS=OFF
    -DHDF5_BUILD_EXAMPLES=OFF
)

ExternalProject_add(
    hdf5
    URL "$ENV{SOURCEROOT}/hdf5/hdf5-1.10.0-patch1.zip"
    PREFIX hdf5
    CMAKE_ARGS -DCMAKE_INSTALL_PREFIX=${CMAKE_INSTALL_PREFIX} ${CMAKE_ARGS}
    INSTALL_COMMAND "${install_cmd}"
    ALWAYS 1
    BUILD_IN_SOURCE 0
)

install(
    CODE
    ""
)
