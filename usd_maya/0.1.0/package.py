name = 'usd_maya'
version = '0.1.0'

build_requires = [
    'usd_core-20.02'
]

variants = [
    ['maya-2019']
]

def commands():
    env.PYTHONPATH.prepend('{root}/lib/python')
    env.MAYA_MODULE_PATH.append('{root}')
