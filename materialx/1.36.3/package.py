name = 'materialx'
version = '1.36.3'

build_requires = [
    'gcc-6.3.1',
    'cmake',
    'python-2.7'
]

requires = [
    '~python-2.7'
]

def commands():
    env.LD_LIBRARY_PATH.append('{root}/lib')
    env.PYTHONPATH.append('{root}/lib/python2.7/site-packages')
