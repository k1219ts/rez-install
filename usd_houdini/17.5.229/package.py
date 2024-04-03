name = 'usd_houdini'
version = '17.5.229'

variants = [
    ['houdini-17.5.229']
]

@early()
def requires():
    if building:
        return ['gcc-6.3.1', 'cmake']
    else:
        return ['DXUSD-1.0']

def commands():
    env.USD_ROOT.set('{root}')
    env.HOUDINI_PATH.append('{root}')
    env.HOUDINI_DSO_ERROR.set('1')
    env.HOUDINI_DSO_PATH.append('{root}/dso')
    env.HOUDINI_SCRIPT_PATH.append('{root}/scripts')
    env.HOUDINI_OTLSCAN_PATH.append('{root}/otls')
    env.PYTHONPATH.append('{root}/scripts')
