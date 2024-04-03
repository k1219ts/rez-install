name = 'fmt'
version = '6.1.2'

build_requires = [
    'gcc-6.3.1',
    'cmake'
]

def commands():
    env.LD_LIBRARY_PATH.append('{root}/lib64')
    if building:
        env.CMAKE_MODULE_PATH.append('{root}/lib64/cmake/fmt')
