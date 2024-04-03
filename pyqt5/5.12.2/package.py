name = 'pyqt5'
version = '5.12.2'

@early()
def requires():
    if building:
        return ['python-2.7', 'qt-5.12.6']

def commands():
    env.PATH.prepend('{root}/bin')
    env.PYTHONPATH.prepend('{root}/lib64/python2.7/site-packages')
