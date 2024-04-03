CMAKE_MINIMUM_REQUIRED(VERSION 3.2)

include(RezBuild)
include(ExternalProject)

set(EXTRACT_DIR $ENV{REZ_BUILD_PATH}/ilmbase/src/ilmbase)
set(BUILD_DIR ${EXTRACT_DIR}/IlmBase)

if(${REZ_BUILD_INSTALL})
    set(install_cmd make install ${make_arg})
else()
    set(install_cmd "")
endif()

ExternalProject_add(
    ilmbase
    URL "$ENV{SOURCEROOT}/openexr/openexr-2.3.0.tar.gz"
    PREFIX ilmbase
    UPDATE_COMMAND ""
    CONFIGURE_COMMAND bash ${CMAKE_SOURCE_DIR}/configure.sh ${BUILD_DIR}
    BUILD_COMMAND bash ${CMAKE_SOURCE_DIR}/build.sh ${BUILD_DIR}
    INSTALL_COMMAND bash ${CMAKE_SOURCE_DIR}/install.sh ${BUILD_DIR}
)

install(
    CODE
    ""
)
