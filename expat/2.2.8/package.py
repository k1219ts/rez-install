name = 'expat'
version = '2.2.8'

build_requires = [
    'gcc-6.3.1',
    'cmake'
]

def commands():
    env.LD_LIBRARY_PATH.append('{root}/lib64')
    env.PKG_CONFIG_PATH.append('{root}/lib64/pkgconfig')
