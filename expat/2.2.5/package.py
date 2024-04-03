name = 'expat'
version = '2.2.5'

build_requires = [
    'gcc-6.3.1',
    'cmake'
]

def commands():
    env.LD_LIBRARY_PATH.append('{root}/lib')
    env.PKG_CONFIG_PATH.append('{root}/lib/pkgconfig')
