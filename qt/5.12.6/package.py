name = 'qt'
version = '5.12.6'

build_requires = [
    'cmake',
    'gcc-6.3.1'
]

def commands():
    env.QT5DIR.set('{root}')
    env.QT_QPA_PLATFORM_PLUGIN_PATH.set('{root}/plugins')
    env.LD_LIBRARY_PATH.prepend('{root}/lib')
    env.PATH.prepend('{root}/bin')
