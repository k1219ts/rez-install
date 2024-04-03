name = 'seexpr'
version = '3.0.1'

@early()
def requires():
    if building:
        return [
            'gcc-6.3.1', 'cmake', 'python-2.7', 'boost-1.61.0'
        ]

def commands():
    env.PATH.append('{root}/bin')
    env.LD_LIBRARY_PATH.append('{root}/lib64')
    env.PYTHONPATH.append('{root}/lib64/python2.7/site-packages')
