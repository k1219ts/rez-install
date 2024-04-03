name = 'png'
version = '1.6.29'

build_requires = [
    'gcc-6.3.1',
    'cmake'
]

def commands():
    env.LD_LIBRARY_PATH.append('{root}/lib64')
    if building:
        env.CMAKE_MODULE_PATH.append('{root}/cmake')
