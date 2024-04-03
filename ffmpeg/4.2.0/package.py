name = 'ffmpeg'
version = '4.2.0'

build_command = 'bash {root}/build.sh {install}'

def commands():
    env.PATH.append('{this.root}/bin')
    env.LD_LIBRARY_PATH.append('{this.root}/lib')
    env.PKG_CONFIG_PATH.append('{this.root}/lib/pkgconfig')
