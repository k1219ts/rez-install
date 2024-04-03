name = 'boost'
version = '1.70.0'

build_requires = [
    'gcc-6.3.1',
    'python-2.7'
]

requires = [
    '~python-2.7'
]

def commands():
    env.LD_LIBRARY_PATH.prepend('{root}/lib')
    env.BOOST_ROOT.set('{root}')
