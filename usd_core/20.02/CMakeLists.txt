CMAKE_MINIMUM_REQUIRED(VERSION 3.2)

include(RezBuild)
include(ExternalProject)

if(${REZ_BUILD_INSTALL})
    set(install_cmd make install ${make_args})
else()
    set(install_cmd "")
endif()

set(CMAKE_ARGS
    -DGLEW_LOCATION=$ENV{REZ_GLEW_ROOT}
    -DTBB_ROOT_DIR=$ENV{REZ_TBB_ROOT}
    -DTBB_LIBRARY=$ENV{REZ_TBB_ROOT}/lib
    -DPXR_BUILD_ALEMBIC_PLUGIN=ON
    -DALEMBIC_DIR=$ENV{REZ_ALEMBIC_ROOT}
    -DPXR_ENABLE_HDF5_SUPPORT=ON
    -DHDF5_ROOT=$ENV{REZ_HDF5_ROOT}
    -DPXR_BUILD_DRACO_PLUGIN=ON
    -DDRACO_ROOT=$ENV{REZ_DRACO_ROOT}
    -DPXR_BUILD_OPENCOLORIO_PLUGIN=ON
    -DOCIO_BASE_DIR=$ENV{REZ_OCIO_ROOT}
    -DPXR_BUILD_OPENIMAGEIO_PLUGIN=ON
    -DOIIO_LOCATION=$ENV{REZ_OIIO_ROOT}
    -DOPENEXR_LOCATION=$ENV{REZ_OPENEXR_ROOT}
    -DOPENSUBDIV_ROOT_DIR=$ENV{REZ_OPENSUBDIV_ROOT}
    -DPXR_BUILD_MATERIALX_PLUGIN=ON
    -DMATERIALX_BASE_DIR=$ENV{REZ_MATERIALX_ROOT}
    -DPXR_ENABLE_OPENVDB_SUPPORT=ON
    -DOPENVDB_LOCATION=$ENV{REZ_OPENVDB_ROOT}
    -DPXR_BUILD_TESTS=OFF
    -DPXR_ENABLE_PTEX_SUPPORT=OFF
    -DBOOST_ROOT=$ENV{REZ_BOOST_ROOT}
    -DPYSIDE_USE_PYSIDE2=ON
    -DPYSIDEUICBINARY=$ENV{REZ_PYSIDE2_ROOT}/bin/pyside2-uic
    -DPXR_MALLOC_LIBRARY=$ENV{REZ_JEMALLOC_ROOT}/lib/libjemalloc.so
    -DPXR_BUILD_PRMAN_PLUGIN=ON
    -DRENDERMAN_LOCATION=/opt/pixar/RenderManProServer-23.1
)

ExternalProject_add(
    usd_core
    URL "$ENV{SOURCEROOT}/usd_core/USD-20.02_patch.tar.gz"
    PREFIX usd_core
    CMAKE_ARGS -DCMAKE_INSTALL_PREFIX=${CMAKE_INSTALL_PREFIX} ${CMAKE_ARGS}
    INSTALL_COMMAND "${install_cmd}"
)

install(
    CODE
    ""
)
