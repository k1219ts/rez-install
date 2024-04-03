name = 'leptonica'
version = '1.79.0'

build_command = 'bash {root}/build.sh {install}'

def commands():
    env.LD_LIBRARY_PATH.append('{root}/lib')
    env.PKG_CONFIG_PATH.append('{root}/lib/pkgconfig')
    env.PATH.append('{root}/bin')
    if building:
        env.LIBLEPT_HEADERSDIR.set('{root}/include')
        
