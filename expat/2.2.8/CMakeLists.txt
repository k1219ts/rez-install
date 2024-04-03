CMAKE_MINIMUM_REQUIRED(VERSION 3.10)

include(RezBuild)
include(ExternalProject)

if(${REZ_BUILD_INSTALL})
    set(install_cmd make install ${make_arg})
else()
    set(install_cmd "")
endif()

set(CMAKE_ARGS
    -DCMAKE_BUILD_TYPE=Release
    -DEXPAT_BUILD_TOOLS=OFF
    -DEXPAT_BUILD_EXAMPLES=OFF
    -DEXPAT_BUILD_TESTS=OFF
    -DEXPAT_SHARED_LIBS=ON
    -DEXPAT_BUILD_DOCS=OFF
    -DCMAKE_C_FLAGS="-fPIC"
    -DCMAKE_CXX_FLAGS="-fPIC"
)

ExternalProject_add(
    expat
    URL "$ENV{SOURCEROOT}/expat/libexpat-R_2_2_8.tar.gz"
    PREFIX expat
    SOURCE_SUBDIR "expat"
    CMAKE_ARGS -DCMAKE_INSTALL_PREFIX=${CMAKE_INSTALL_PREFIX} ${CMAKE_ARGS}
    INSTALL_COMMAND ${install_cmd}
)

install(
    CODE
    ""
)
