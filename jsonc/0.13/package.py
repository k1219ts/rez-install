name = 'jsonc'
version = '0.13'

@early()
def requires():
    if building:
        return ['gcc-6.3.1']

def commands():
    env.LD_LIBRARY_PATH.append('{root}/lib')
