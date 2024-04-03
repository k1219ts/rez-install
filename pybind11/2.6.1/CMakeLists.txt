CMAKE_MINIMUM_REQUIRED(VERSION 3.1)

include(RezBuild)
include(ExternalProject)

if(${REZ_BUILD_INSTALL})
    set(install_cmd make install ${make_args})
else()
    set(install_cmd "")
endif()

set(CMAKE_ARGS
    -DCMAKE_CXX_FLASG="-fPIC"
    -DPYBIND11_TEST=OFF
    -DPYBIND11_PYTHON_VERSION=$ENV{REZ_PYTHON_MAJOR_VERSION}.$ENV{REZ_PYTHON_MINOR_VERSION}
)

ExternalProject_add(
    pybind11
    URL "$ENV{SOURCEROOT}/pybind11/pybind11-2.6.1.tar.gz"
    PREFIX pybind11
    CMAKE_ARGS -DCMAKE_INSTALL_PREFIX=${CMAKE_INSTALL_PREFIX} ${CMAKE_ARGS}
    INSTALL_COMMAND ${install_cmd}
)

install(
    CODE
    ""
)
