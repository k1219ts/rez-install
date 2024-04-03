CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(ExternalProject)

ExternalProject_add(
    python
    URL "$ENV{SOURCEROOT}/python3.7/Python-3.7.7.tgz"
    PREFIX python
    UPDATE_COMMAND ""
    CONFIGURE_COMMAND ./configure --prefix=${CMAKE_INSTALL_PREFIX} --enable-optimizations --enable-shared --with-ensurepip=install LDFLAGS=-Wl,-rpath,'$$ORIGIN/../lib/'
    INSTALL_COMMAND make altinstall
    ALWAYS 1
    BUILD_IN_SOURCE 1
)

install(
    CODE
    ""
)
