CMAKE_MINIMUM_REQUIRED(VERSION 3.2)

include(RezBuild)
include(ExternalProject)

if(${REZ_BUILD_INSTALL})
    set(install_cmd cmake --build . --target install -- -j 8)
else()
    set(install_cmd "")
endif()

set(CMAKE_ARGS
    -DOPENVDB_BUILD_PYTHON_MODULE=ON
    -DOPENVDB_BUILD_BINARIES=ON
    -DOPENVDB_BUILD_UNITTESTS=OFF
    -DBOOST_ROOT=$ENV{REZ_BOOST_ROOT}
    -DBLOSC_ROOT=$ENV{REZ_BLOSC_ROOT}
    -DTBB_ROOT=$ENV{REZ_TBB_ROOT}
    -DILMBASE_ROOT=$ENV{REZ_ILMBASE_ROOT}
)

ExternalProject_add(
    openvdb
    URL "$ENV{SOURCEROOT}/openvdb/openvdb-6.1.0.tar.gz"
    PREFIX openvdb
    CMAKE_ARGS -DCMAKE_INSTALL_PREFIX=${CMAKE_INSTALL_PREFIX} ${CMAKE_ARGS}
    INSTALL_COMMAND "${install_cmd}"
)

install(
    CODE
    ""
)
