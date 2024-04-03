name = 'python'
version = '3.7.7'

tools = [
    '2to3-3.7',
    'easy_install-3.7',
    'idle3.7',
    'pip3.7',
    'pydoc3.7',
    'python3.7',
    'python3.7m-config',
    'pyvenv-3.7'
]

def commands():
    env.PATH.prepend('{root}/bin')
    env.LD_LIBRARY_PATH.prepend('{root}/lib')
