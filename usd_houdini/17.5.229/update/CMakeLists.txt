# Minimum version of CMake required
cmake_minimum_required( VERSION 3.6 )
project( usd_houdini_plugins )
set( library_name OP_gusd )

# CMAKE_PREFIX_PATH must contain the path to the toolkit/cmake subdirectory of
# the Houdini installation. See the "Compiling with CMake" section of the HDK
# documentation for more details, which describes several options for
# specifying this path.
list( APPEND CMAKE_PREFIX_PATH "$ENV{HFS}/toolkit/cmake" )

find_package( Houdini REQUIRED )

#-----------------------------------------
# Copied from HoudiniConfig.cmake
if ( _houdini_platform_linux )
    # set(H_INSTDIR $ENV{HOME}/houdini${_houdini_release_version})
    set(H_INSTDIR ${CMAKE_INSTALL_PREFIX})  # edit dexter
elseif( _houdini_platform_osx )
    set(H_INSTDIR $ENV{HOME}/Library/Preferences/houdini/${_houdini_release_version} )
elseif( _houdini_platform_win )
    set(H_INSTDIR $ENV{HOMEDRIVE}$ENV{HOMEPATH}\\Documents\\houdini${_houdini_release_version} )
else( )
    ERROR("Invalid platform")
endif()
#-----------------------------------------

MESSAGE( "Installing to ${H_INSTDIR}" )

# Add .so which contains plugins for Object, ROP and SOPs
add_library( ${library_name} SHARED
    OBJ_usdcamera.cpp
    OBJ_usdcamera.h
    ROP_usdoutput.cpp
    ROP_usdoutput.h
    SOP_usdimport.cpp
    SOP_usdimport.h
    SOP_usdunpack.cpp
    SOP_usdunpack.h
    OP_Utils.cpp
    OP_Utils.h
    plugin.cpp
)

if ( _houdini_platform_linux )
    # Link against Houdini libraries (including USD)
    if ( DEFINED ENV{HOUDINI_HDK_LINK_GUSD} )
    target_link_libraries( ${library_name}
	Houdini					# Standard Houdini librarys
	${_houdini_hfs_root}/dsolib/libgusd.so
    )
    else ()
	target_link_libraries( ${library_name}
	    Houdini			# Standard Houdini librarys
	)
    endif ()
elseif( _houdini_platform_osx )
    # Link against Houdini libraries (including USD)
    target_link_libraries( ${library_name}
	Houdini					# Standard Houdini librarys
	${_houdini_hfs_root}/../Libraries/libpxr_usd_ms.dylib
	${_houdini_hfs_root}/../Libraries/libhboost_python-mt.dylib
	${_houdini_hfs_root}/../Libraries/libtbb.dylib
	${_houdini_hfs_root}/Frameworks/Python.framework/Versions/Current/lib/libpython2.7.dylib
    )
elseif( _houdini_platform_win )
    # Link against Houdini libraries (including USD)
    target_link_libraries( ${library_name}
	Houdini					# Standard Houdini librarys
	${_houdini_hfs_root}/custom/houdini/dsolib/libgusd.lib
	${_houdini_hfs_root}/custom/houdini/dsolib/libpxr_usd_ms.lib
	${_houdini_hfs_root}/custom/houdini/dsolib/hboost_python-mt.lib
	${_houdini_hfs_root}/python27/libs/python27.lib
    )
endif()

# Configure several common target properties (such as output directory)
houdini_configure_target( ${library_name} )

install(
    DIRECTORY
        help
    DESTINATION
        ${H_INSTDIR}
)

install(
    FILES
        ROP_usdcoalesce.otl
        ROP_usdlayer.otl
        ROP_usdreference.otl
        SOP_camerafrustum.otl
        SOP_usdbindproxy.otl
        SOP_usdexportattributes.hda
        SOP_usdinstanceprototypes.hda
        SOP_usdretime.hda
    DESTINATION
        ${H_INSTDIR}/otls
)

install(
    FILES
        ROP_usdcoalesce.py
        ROP_usdlayer.py
        ROP_usdreference.py
    DESTINATION
        ${H_INSTDIR}/soho/python2.7
)

install(
    FILES
        UsdImport.pypanel
    DESTINATION
        ${H_INSTDIR}/python_panels
)

install(
    FILES
        obj/pixar-usdcamera.py
    DESTINATION
        ${H_INSTDIR}/scripts/obj
)

install(
    FILES
	icons/pxh_gusdIcon.png
    DESTINATION
	${H_INSTDIR}/config/Icons
)
