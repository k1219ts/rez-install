CMAKE_MINIMUM_REQUIRED(VERSION 3.13)

include(RezBuild)
include(ExternalProject)

if(${REZ_BUILD_INSTALL})
    set(install_cmd make install ${make_args})
else()
    set(install_cmd "")
endif()

set(CMAKE_ARGS
    -DCMAKE_BUILD_TYPE=RelWithDebInfo
    -DBUILD_TESTS=OFF
    -DMAYA_LOCATION=$ENV{MAYA_LOCATION}
    -DPXR_USD_LOCATION=$ENV{USD_ROOT}
    -DMAYA_DEVKIT_LOCATION=$ENV{MAYA_LOCATION}/devkit
    -DMAYAUSD_DEFINE_BOOST_DEBUG_PYTHON_FLAG=OFF
    -DSKIP_USDMAYA_TESTS=ON
)

ExternalProject_add(
    usd_maya
    URL "$ENV{SOURCEROOT}/usd_maya/maya-usd-0.1.0.tar.gz"
    PREFIX usd_core
    CMAKE_ARGS -DCMAKE_INSTALL_PREFIX=${CMAKE_INSTALL_PREFIX} ${CMAKE_ARGS}
    INSTALL_COMMAND "${install_cmd}"
)

install(
    CODE
    ""
)
