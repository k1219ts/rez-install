CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(ExternalProject)

if(${REZ_BUILD_INSTALL})
    set(install_cmd make install ${make_arg})
else()
    set(install_cmd "")
endif()

ExternalProject_add(
    pyilmbase
    URL "$ENV{SOURCEROOT}/pyilmbase/pyilmbase-2.2.0.tar.gz"
    PREFIX pyilmbase
    UPDATE_COMMAND ""
    CONFIGURE_COMMAND ./configure --prefix=${CMAKE_INSTALL_PREFIX} --with-boost-include-dir=$ENV{REZ_BOOST_ROOT}/include --with-boost-lib-dir=$ENV{REZ_BOOST_ROOT}/lib --with-boost-python-libname=boost_python
    BUILD_COMMAND make ${make_arg}
    INSTALL_COMMAND "${install_cmd}"
    BUILD_IN_SOURCE 1
)

install(
    CODE
    ""
)
