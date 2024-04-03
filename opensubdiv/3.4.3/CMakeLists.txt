CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(ExternalProject)

if(${REZ_BUILD_INSTALL})
    set(install_cmd make install ${make_args})
else()
    set(install_cmd "")
endif()

set(CMAKE_ARGS
    -DNO_TBB=ON
    -DNO_EXAMPLES=ON
    -DNO_TUTORIALS=ON
    -DNO_REGRESSION=ON
    -DNO_DOC=ON
    -DNO_OMP=ON
    -DNO_CUDA=ON
    -DNO_OPENCL=ON
    -DNO_DX=ON
    -DNO_TESTS=ON
    -DNO_PTEX=ON
)

ExternalProject_add(
    opensubdiv
    URL "$ENV{SOURCEROOT}/opensubdiv/OpenSubdiv-3_4_3.tar.gz"
    PREFIX opensubdiv
    CMAKE_ARGS -DCMAKE_INSTALL_PREFIX=${CMAKE_INSTALL_PREFIX} ${CMAKE_ARGS}
    INSTALL_COMMAND "${install_cmd}"
    ALWAYS 1
)

install(
    CODE
    ""
)
