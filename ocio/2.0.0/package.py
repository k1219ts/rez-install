name = 'ocio'
version = '2.0.0'

build_requires = [
    'gcc-6.3.1',
    'cmake',
    'pystring-1.1.3',
    'pybind11-2.6.1',
    'lcms-2.12'
]

requires = [
    'expat-2.2.8',
    'yaml-0.6.3',
    'openexr-2.4.2',
    'python-2.7.16',
]

def commands():
    env.LD_LIBRARY_PATH.prepend('{root}/lib')
    env.PYTHONPATH.append('{root}/lib/python2.7/site-packages')
    env.PATH.append('{root}/bin')
    if building:
        env.CMAKE_MODULE_PATH.append('{root}/cmake')
