name = 'alembic'
version = '1.7.1'

build_requires = [
    'gcc-6.3.1',
    'cmake'
]

requires = [
    'hdf5-1.10.0',
    'ilmbase-2.2.0',
    'openexr-2.2.0'
]

def commands():
    env.LD_LIBRARY_PATH.append('{root}/lib')
