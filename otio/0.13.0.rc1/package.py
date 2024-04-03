name = 'otio'
version = '0.13.0'

@early()
def requires():
    if building:
        return ['python-2.7', 'cmake']
    else:
        return ['pyside2']

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

    # Pipeline scripts
    # env.BACKSTAGE_OTIO_PATH.set('/backstage/apps/OTIO')
    # env.OTIO_SCRIPT_PATH.set('{}/scripts'.format(env.BACKSTAGE_OTIO_PATH))
    # env.OTIO_NAUTILUS_SCRIPT_PATH.set('{}/shares/nautilus'.format(BACK_OTIO=env.BACKSTAGE_OTIO_PATH))
