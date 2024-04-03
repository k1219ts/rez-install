name = 'tiff'
version = '4.1.0'

build_requires = [
    'gcc-6.3.1',
    'cmake',
    'jpeg-1.5.3',
    'zlib-1.2.11'
]

requires = [
    'jpeg-1.5.3',
    'zlib-1.2.11'
]

def commands():
    env.LD_LIBRARY_PATH.append('{root}/lib64')
    # env.PKG_CONFIG_PATH.append('{root}/lib64/pkgconfig')
    if building:
        env.CMAKE_MODULE_PATH.append('{root}/cmake')
