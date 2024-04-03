name = 'usdmanager'
version = '0.11.0'

build_requires = [
    'python-2.7'
]

requires = [
    'python-2.7',
    'pyside2',
    'usdtoolkit'
]

build_command = 'bash {root}/build.sh {install}'

tools = [
    'usdmanager'
]

def commands():
    env.PATH.append('{root}/bin')
    env.PYTHONPATH.append('{root}/lib/python2.7/site-packages')
