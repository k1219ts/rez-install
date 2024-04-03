CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(ExternalProject)

if(${REZ_BUILD_INSTALL})
    set(install_cmd make install ${make_arg})
else()
    set(install_cmd "")
endif()

set(CMAKE_ARGS
    -DUSE_BINARIES=OFF
    -DUSE_TESTS=OFF
    -DUSE_HDF5=ON
    -DHDF5_ROOT=$ENV{REZ_HDF5_ROOT}
    -DCMAKE_CXX_FLAGS="-D H5_BUILT_AS_DYNAMIC_LIB"
)

ExternalProject_add(
    alembic
    URL "$ENV{SOURCEROOT}/alembic/1.7.1.zip"
    PREFIX alembic
    CMAKE_ARGS -DCMAKE_INSTALL_PREFIX=${CMAKE_INSTALL_PREFIX} ${CMAKE_ARGS}
    INSTALL_COMMAND "${install_cmd}"
    BUILD_IN_SOURCE 1
)

install(
    CODE
    ""
)
