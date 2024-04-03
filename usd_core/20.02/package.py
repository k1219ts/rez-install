name = 'usd_core'
version = '20.02'

build_requires = [
    'gcc-6.3.1',
    'cmake',
    'draco-1.3.6',
    'alembic-1.7.1',
    'openexr-2.2.0',
    'oiio-1.7.14',
    'opensubdiv-3.1.1',
    'openvdb-6.1.0',
    'materialx-1.36.3',
    'glew-2.0.0',
    'zlib-1.2.11',
    'tbb-2017_U6',
    'boost-1.61.0',
    'jemalloc-4.5.0',
    'python-2.7',
    'pyside2-5.12.6'
]

requires = [
]

def commands():
    env.USD_ROOT.set('{root}')
    env.PYTHONPATH.append('{root}/lib/python')
    env.LD_LIBRARY_PATH.append('{root}/lib')
    env.PATH.append('{root}/bin')
