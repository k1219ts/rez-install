name = 'pyalembic'
version = '1.7.1'

build_requires = [
    'gcc-6.3.1',
    'cmake',
    'python-2.7'
]

requires = [
    'hdf5-1.10.0',
    'ilmbase-2.2.0',
    'pyilmbase-2.2.0',
    'openexr-2.2.0',
    '~python-2.7'
]

def commands():
    env.LD_LIBRARY_PATH.append('{root}/lib')
    env.PYTHONPATH.append('{root}/lib/python2.7/site-packages')
