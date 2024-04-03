name = 'usd_maya'
version = '0.4.0'

variants = [
    # ['maya-2018'],
    # ['maya-2019'],
    ['maya-2020']
]

@early()
def requires():
    if building:
        return ['usd_core-20.08', 'qt-5.12.6']

def commands():
    env.USD_WRITE_NEW_USDC_FILES_AS_VERSION.set('0.8.0')
    env.PYTHONPATH.prepend('{root}/lib/python')
    env.MAYA_MODULE_PATH.append('{root}')
