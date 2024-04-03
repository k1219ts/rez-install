name = 'pybind11'
version = '2.4.3'

build_requires = [
    'gcc-6.3.1',
    'cmake-3.14.6',
    'python-2.7'
]

def commands():
    env.CMAKE_MODULE_PATH.prepend('{root}/share/cmake/pybind11')
    env.PYBIND11_INCLUDE_PATH.set('{root}/include')
