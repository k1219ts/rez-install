CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(ExternalProject)

set(make_arg -j8)

if(${REZ_BUILD_INSTALL})
    set(install_cmd make install ${make_arg})
else()
    set(install_cmd "")
endif()

ExternalProject_add(
    qt
    URL "$ENV{SOURCEROOT}/qt5/qt5-5.12.6.zip"
    PREFIX qt
    UPDATE_COMMAND ""
    CONFIGURE_COMMAND ./configure --prefix=${CMAKE_INSTALL_PREFIX} -opensource -confirm-license -nomake examples -nomake tests
    INSTALL_COMMAND "${install_cmd}"
    BUILD_IN_SOURCE 1
    BUILD_COMMAND make ${make_arg}
)

install(
    CODE
    ""
)
