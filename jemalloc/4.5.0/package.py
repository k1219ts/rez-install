name = 'jemalloc'
version = '4.5.0'

build_requires = [
    'gcc-6.3.1'
]

def commands():
    env.LD_LIBRARY_PATH.append('{root}/lib')
    env.PATH.append('{root}/bin')
