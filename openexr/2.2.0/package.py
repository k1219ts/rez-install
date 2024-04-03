name = 'openexr'
version = '2.2.0'

build_requires = [
    'gcc-6.3.1'
]

requires = [
    'ilmbase-2.2.0'
]

def commands():
    env.PATH.append('{root}/bin')
    env.LD_LIBRARY_PATH.append('{root}/lib')
    if building:
        env.OPENEXR_ROOT.set('{root}')
