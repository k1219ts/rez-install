CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(ExternalProject)

rez_find_packages(PREFIX pkgs AUTO)

set(make_arg -j32)

if(${REZ_BUILD_INSTALL})
    set(install_cmd make install ${make_arg})
else()
    set(install_cmd "")
endif()

set(CMAKE_ARGS
    -DExpat_ROOT=$ENV{REZ_EXPAT_ROOT}
    -DExpat_STATIC_LIBRARY=OFF
    -Dyaml-cpp_ROOT=$ENV{REZ_YAML_ROOT}
    -Dyaml-cpp_STATIC_LIBRARY=OFF
    -DHalf_ROOT=$ENV{REZ_OPENEXR_ROOT}
    -Dpystring_ROOT=$ENV{REZ_PYSTRING_ROOT}
    -Dpystring_STATIC_LIBRARY=ON
    -Dlcms2_ROOT=$ENV{REZ_LCMS_ROOT}
    -Dlcms2_STATIC_LIBRARY=ON
    -Dpybind11_ROOT=$ENV{REZ_PYBIND11_ROOT}
    -DOCIO_INSTALL_EXT_PACKAGES=NONE
    -DBUILD_SHARED_LIBS=ON
    -DOCIO_BUILD_APPS=ON
    -DOCIO_BUILD_TESTS=OFF
    -DOCIO_BUILD_GPU_TESTS=OFF
    -DOCIO_BUILD_PYTHON=ON
)

ExternalProject_add(
    ocio
    URL "$ENV{SOURCEROOT}/ocio/OpenColorIO-2.0.0.tar.gz"
    PREFIX ocio
    CMAKE_ARGS -DCMAKE_INSTALL_PREFIX=${CMAKE_INSTALL_PREFIX} -${CMAKE_ARGS}
    INSTALL_COMMAND "${install_cmd}"
    ALWAYS 1
)

rez_install_files(
    cmake/ocio.cmake
    DESTINATION .
)
