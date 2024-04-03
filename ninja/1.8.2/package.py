name = 'ninja'
version = '1.8.2'

build_command = 'bash {root}/build.sh {install}'

def commands():
    env.PATH.prepend('{root}/bin')
