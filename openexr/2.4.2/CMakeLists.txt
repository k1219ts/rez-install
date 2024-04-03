CMAKE_MINIMUM_REQUIRED(VERSION 3.1)

include(RezBuild)
include(ExternalProject)

set(make_arg -j32)

if(${REZ_BUILD_INSTALL})
    set(install_cmd make install ${make_arg})
else()
    set(install_cmd "")
endif()

set(CMAKE_ARGS
    -DOPENEXR_BUILD_ILMBASE=ON
    -DOPENEXR_BUILD_OPENEXR=ON
    -DOPENEXR_BUILD_PYTHON_LIBS=OFF
    -DOPENEXR_BUILD_TESTS=OFF
    -DOPENEXR_BUILD_UTILS=ON
    -DOPENEXR_BUILD_VIEWERS=OFF
    -DBUILD_IMFEXAMPLES=OFF
    -DCMAKE_C_FLAGS="-fPIC"
    -DCMAKE_CXX_FLAGS="-fPIC"
)

ExternalProject_add(
    openexr
    URL "$ENV{SOURCEROOT}/openexr/openexr-2.4.2.tar.gz"
    PREFIX openexr
    CMAKE_ARGS -DCMAKE_INSTALL_PREFIX=${CMAKE_INSTALL_PREFIX} ${CMAKE_ARGS}
    BUILD_COMMAND "${install_cmd}"
)

install(
    CODE
    ""
)
