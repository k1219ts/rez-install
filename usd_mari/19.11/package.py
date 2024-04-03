name = 'usd_mari'
version = '19.11'

requires = [
    'jemalloc'
]

variants = [
    ['mari-4.6.4']
]

build_requires = [
    'usd_core-19.11',
    'cmake-3.14.6',
    'ninja-1.8.2',
    'gcc-6.3.1',
    'tbb-2017_U6',
    'boost-1.61.0',
]

build_command = 'bash {root}/build.sh {install}'

def commands():
    env.PATH.prepend('{root}/lib')
    env.LD_LIBRARY_PATH.prepend('{root}/lib')
    env.MARI_PLUGINS_PATH.append('{root}')
    env.PYTHONPATH.prepend('{root}/lib/python')
