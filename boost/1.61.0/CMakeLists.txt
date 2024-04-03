CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(ExternalProject)

set(boost_bootstrap_args --with-python=$ENV{REZ_PYTHON_ROOT}/bin/python --with-python-root=$ENV{REZ_PYTHON_ROOT})
set(b2_args -d1 --prefix=${CMAKE_INSTALL_PREFIX} --exec-prefix=${CMAKE_INSTALL_PREFIX} link=static,shared --toolset=gcc cxxflags=-fPIC)

if(${REZ_BUILD_INSTALL})
    set(install_cmd ./b2 install ${b2_args})
else()
    set(install_cmd "")
endif()

ExternalProject_add(
    boost
    URL "$ENV{SOURCEROOT}/boost/boost_1_61_0.tar.gz"
    PREFIX boost
    UPDATE_COMMAND ""
    CONFIGURE_COMMAND ./bootstrap.sh ${boost_bootstrap_args}
    BUILD_IN_SOURCE 1
    BUILD_COMMAND ./b2 ${b2_args}
    INSTALL_COMMAND ${install_cmd}
)

rez_install_files(
    cmake/boost.cmake
    DESTINATION .
)
