name = 'ilmbase'
version = '2.2.0'

build_requires = [
    'gcc-6.3.1'
]

def commands():
    env.LD_LIBRARY_PATH.append('{root}/lib')
    env.PKG_CONFIG_PATH.append('{root}/lib/pkgconfig')
    if building:
        env.ILMBASE_ROOT.set('{root}')
