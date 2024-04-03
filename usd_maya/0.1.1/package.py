name = 'usd_maya'
version = '0.1.1'

variants = [
    ['maya-2019'],
    ['maya-2020']
]

@early()
def requires():
    if building:
        return ['usd_core-20.05']

def commands():
    env.PYTHONPATH.prepend('{root}/lib/python')
    env.MAYA_MODULE_PATH.append('{root}')
