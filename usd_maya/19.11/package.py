name = 'usd_maya'
version = '19.11'

variants = [
    ['maya-2018'],
    ['maya-2019']
]

@early()
def requires():
    if building:
        return [
            #'gcc-6.3.1',
            'cmake',
            'draco-1.3.6',
            'alembic-1.7.1',
            'openexr-2.2.0',
            'oiio-1.7.14',
            'opensubdiv-3.1.1',
            'glew-2.0.0',
            'zlib-1.2.11',
            'tbb-2017_U6',
            'boost-1.61.0',
            'jemalloc-4.5.0',
            'python-2.7',
            'pyside2-5.12.6'
        ]

def commands():
    env.USD_ROOT.set('{root}')
    env.MAYA_PLUG_IN_PATH.append('{root}/third_party/maya/plugin')
    env.MAYA_SCRIPT_PATH.append('{root}/third_party/maya/lib/usd/usdMaya/resources')
    env.PYTHONPATH.append('{root}/lib/python')
    env.XBMLANGPATH.append('{root}/third_party/maya/share/usd/plugins/usdMaya/resources')
    env.LD_LIBRARY_PATH.append('{root}/lib')
    env.LD_LIBRARY_PATH.append('{root}/third_party/maya/lib')
