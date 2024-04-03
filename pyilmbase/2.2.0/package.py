name = 'pyilmbase'
version = '2.2.0'

build_requires = [
    'gcc-6.3.1',
    'cmake',
    'python-2.7'
]

requires = [
    'boost-1.61.0',
    'ilmbase-2.2.0',
    '~python-2.7'
]

def commands():
    env.LD_LIBRARY_PATH.append('{root}/lib')
    env.PYTHONPATH.append('{root}/lib/python2.7/site-packages')
    if building:
        env.PYILMBASE_ROOT.set('{root}')
