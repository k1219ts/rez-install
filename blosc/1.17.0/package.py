name = 'blosc'
version = '1.17.0'

build_requires = [
    'gcc-6.3.1',
    'cmake'
]

def commands():
    env.LD_LIBRARY_PATH.prepend('{root}/lib')
