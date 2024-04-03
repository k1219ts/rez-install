name = 'openexr'
version = '2.4.2'

build_requires = [
    'gcc-6.3.1',
    'cmake'
]

requires = [
]

def commands():
    env.PATH.append('{root}/bin')
    env.LD_LIBRARY_PATH.append('{root}/lib64')
    env.PKG_CONFIG_PATH.append('{root}/lib64/pkgconfig')
    if building:
        env.OPENEXR_ROOT.set('{root}')
