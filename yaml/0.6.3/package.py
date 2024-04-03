name = 'yaml'
version = '0.6.3'

build_requires = [
    'gcc-6.3.1',
    'cmake'
]

requires = [
]

def commands():
    env.LD_LIBRARY_PATH.append('{root}/lib')
