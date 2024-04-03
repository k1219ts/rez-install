name = 'glew'
version = '2.0.0'

build_requires = [
    'gcc-6.3.1'
]

def commands():
    env.LD_LIBRARY_PATH.append('{root}/lib64')
    if building:
        env.CMAKE_MODULE_PATH.append('{root}/cmake')
