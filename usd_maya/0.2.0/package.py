name = 'usd_maya'
version = '0.2.0'

variants = [
    ['maya-2019']
]

@early()
def requires():
    if building:
        return ['usd_core-20.05']

def commands():
    env.PYTHONPATH.prepend('{root}/lib/python')
    env.MAYA_MODULE_PATH.append('{root}')
