CMAKE_MINIMUM_REQUIRED(VERSION 3.2)

include(RezBuild)
include(ExternalProject)

if(${REZ_BUILD_INSTALL})
    set(install_cmd make install ${make_args})
else()
    set(install_cmd "")
endif()

set(CMAKE_ARGS
    -DMATERIALX_BUILD_PYTHON=ON
    -DMATERIALX_INSTALL_PYTHON=ON
    -DMATERIALX_PYTHON_EXECUTABLE=$ENV{REZ_PYTHON_ROOT}/bin/python
    -DMATERIALX_PYTHON_INCLUDE_DIR=$ENV{REZ_PYTHON_ROOT}/include/python2.7
    -DMATERIALX_PYTHON_LIBRARY=$ENV{REZ_PYTHON_ROOT}/lib/libpython2.7.so
)

ExternalProject_add(
    materialx
    URL "$ENV{SOURCEROOT}/materialx/v1.36.0.zip"
    PREFIX materialx
    CMAKE_ARGS -DCMAKE_INSTALL_PREFIX=${CMAKE_INSTALL_PREFIX} ${CMAKE_ARGS}
    INSTALL_COMMAND "${install_cmd}"
)

install(
    CODE
    ""
)
