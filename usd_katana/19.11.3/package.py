name = 'usd_katana'
version = '19.11.3'

variants = [
    ['katana-3.5'],
    ['katana-3.6'],
    ['katana-4.0']
]

@early()
def requires():
    if building:
        pkgs = ['gcc-6.3.1', 'cmake']
        return pkgs

def commands():
    env.USD_KATANA_ALLOW_CUSTOM_MATERIAL_SCOPES.set('1')
    env.KATANA_RESOURCES.append('{root}/third_party/katana/plugin')
    env.LD_LIBRARY_PATH.append('{root}/third_party/katana/lib/usd/libs')
