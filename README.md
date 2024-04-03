# REZ
## Package Commands
```
building
build_variant_index
resolve : A dict representing the list of packages in the resolved environment.
version.major, minor, patch
```
## Variables
```
# bash
REZ_BUILD_INSTALL : rez-build -i or rez-release
REZ_BUILD_INSTALL_PATH : Installation path
REZ_BUILD_PATH : Path where build output goes. ( ./build )
REZ_BUILD_SOURCE_PATH : Path containing the package.py file. ( ./ )
REZ_BUILD_THREAD_COUNT : Number fo threads being used for the build.
REZ_BUILD_VARIANT_INDEX : Zero-based index of the variant currently being built.
REZ_BUILD_VARIANT_SUBPATH : Subdirectory containing the current variant.

# cmake
CMAKE_CURRENT_BINARY_DIR : ( ./build )
CMAKE_CURRENT_SOURCE_DIR : ( ./ )
CMAKE_INSTALL_PREFIX : REZ_BUILD_INSTALL_PATH
```
## CMAKE Commands
```
ExternalProject_add(
    UPDATE_COMMAND ""
    CONFIGURE_COMMAND ""
    CMAKE_ARGS ""
    INSTALL_COMMAND ""
    BUILD_COMMAND ""
    BUILD_IN_SOURCE 1
)

if($ENV{REZ_BUILD_VARIANT_INDEX} EQUAL 0)
```

# NFS Mount
```
mount -t nfs -o soft,vers=3 10.0.0.228:/andante/libs /backstage/libs
```
