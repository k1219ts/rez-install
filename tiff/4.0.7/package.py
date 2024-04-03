name = 'tiff'
version = '4.0.7'

build_requires = [
    'cmake'
]

def commands():
    env.LD_LIBRARY_PATH.append('{root}/lib64')
    if building:
        env.CMAKE_MODULE_PATH.append('{root}/cmake')
