name = 'python'
version = '2.7.16'

tools = [
    '2to3',
    'easy_install',
    'easy_install-2.7',
    'idle',
    'pip',
    'pip2',
    'pip2.7',
    'pydoc',
    'python',
    'python2',
    'python2.7',
    'python2.7-config',
    'python2-config',
    'python-config',
    'smtpd.py'
]

def commands():
    env.PATH.prepend('{root}/bin')
    env.LD_LIBRARY_PATH.prepend('{root}/lib')
    if building:
        env.CMAKE_MODULE_PATH.prepend('{root}/cmake')
