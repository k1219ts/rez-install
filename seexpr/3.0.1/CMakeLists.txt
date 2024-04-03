CMAKE_MINIMUM_REQUIRED(VERSION 3.8)

include(RezBuild)
include(ExternalProject)

if(${REZ_BUILD_INSTALL})
    set(install_cmd make install ${make_arg})
else()
    set(install_cmd "")
endif()

ExternalProject_add(
    seexpr
    URL "$ENV{SOURCEROOT}/seexpr/SeExpr-3.0.1.zip"
    CMAKE_ARGS -DCMAKE_INSTALL_PREFIX=${CMAKE_INSTALL_PREFIX}
    INSTALL_COMMAND "${install_cmd}"
)

install(
    CODE
    ""
)
