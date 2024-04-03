name = 'tesseract'
version = '4.1.1'

requires = [
    'leptonica-1.79.0',
    'zlib-1.2.11',
    'png-1.6.29',
    'tiff-4.1.0',
    'jpeg-1.5.3'
]

build_command = 'bash {root}/build.sh {install}'

def commands():
    env.LD_LIBRARY_PATH.append('{root}/lib')
    env.PATH.append('{root}/bin')
