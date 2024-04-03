name = 'otio'
version = '0.14.0'

build_requires = [
    'python-2.7', 'cmake', 'pyside2'
]

build_command = 'bash {root}/build.sh {install}'

tools = [
    'otiocat',
    'otioconvert',
    'otiostat',
    'otioview'
]

def commands():
    env.LD_LIBRARY_PATH.append('{root}/lib')
    env.PATH.prepend('{root}/bin')
    env.PYTHONPATH.prepend('{root}/lib/python2.7/site-packages')
