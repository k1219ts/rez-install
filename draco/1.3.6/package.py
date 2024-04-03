name = 'draco'
version = '1.3.6'

build_requires = [
    'gcc-6.3.1',
    'cmake'
]

def commands():
    env.LD_LIBRARY_PATH.append('{root}/lib')
    env.PATH.append('{root}/bin')
