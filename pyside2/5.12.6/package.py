name = 'pyside2'
version = '5.12.6'

build_requires = [
    'gcc-6.3.1',
    'cmake',
    'clang-7.0.0'
]

requires = [
    'python-2.7.16',
    'qt-5.12.6'
]

build_command = 'bash {root}/build.sh {install}'

def commands():
    env.PATH.prepend('{root}/bin')
    env.LD_LIBRARY_PATH.prepend('{root}/lib')
    env.PYTHONPATH.prepend('{root}/lib/python2.7/site-packages')
