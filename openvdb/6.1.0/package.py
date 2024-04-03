name = 'openvdb'
version = '6.1.0'

build_requires = [
    'gcc-6.3.1',
    'cmake'
]

requires = [
    'boost-1.61.0',
    'blosc-1.17.0',
    'tbb-2017_U6',
    'ilmbase-2.2.0'
]

def commands():
    env.LD_LIBRARY_PATH.append('{root}/lib')
    env.PATH.append('{root}/bin')
    env.PYTHONPATH.append('{root}/lib/python2.7')
