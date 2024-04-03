name = 'usd_katana'
version = '19.11'

variants = [
    ['katana-3.2'],
    ['katana-3.5']
]

@early()
def requires():
    if building:
        pkgs = ['gcc-6.3.1', 'cmake']
        if build_variant_index == 0:
            pkgs += [
                'gcc-6.3.1',
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
        return pkgs

def commands():
    env.USD_KATANA_ALLOW_CUSTOM_MATERIAL_SCOPES.set('1')
    env.KATANA_RESOURCES.append('{root}/third_party/katana/plugin')
    if resolve.katana.version.minor == 5:
        env.LD_LIBRARY_PATH.append('{root}/third_party/katana/lib/usd/libs')
    elif resolve.katana.version.minor == 2:
        env.PYTHONPATH.append('{root}/lib/python')
        env.KATANA_POST_PYTHONPATH.append('{root}/third_party/katana/lib')
