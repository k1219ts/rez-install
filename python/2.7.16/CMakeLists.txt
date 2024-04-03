CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(ExternalProject)

# ------------------------------------------------------------------------------
# Build Dependencies to build all standard modules
#
# Centos:
# yum groupinstall 'Development Tools'
# yum install zlib-devel
# yum install readline-devel
# yum install ncurses-devel
# yum install openssl-devel
# yum install gdbm-devel
# yum install sqlite-devel
# yum install bzip2-devel
# ------------------------------------------------------------------------------

ExternalProject_add(
    python
    URL "$ENV{SOURCEROOT}/python2.7/Python-2.7.16.tgz"
    PREFIX python
    UPDATE_COMMAND ""
    CONFIGURE_COMMAND ./configure --prefix=${CMAKE_INSTALL_PREFIX} --enable-shared --enable-unicode=ucs4 --with-ensurepip=install LDFLAGS=-Wl,-rpath,'$$ORIGIN/../lib/'
    INSTALL_COMMAND make install VERBOSE=1
    ALWAYS 1
    BUILD_COMMAND make -j8 VERBOSE=1
    BUILD_IN_SOURCE 1
)

rez_install_files(
    cmake/python.cmake cmake/FindPython.cmake
    DESTINATION .
)
