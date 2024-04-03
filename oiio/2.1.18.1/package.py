name = 'oiio'
version = '2.1.18.1'

build_requires = [
    'gcc-6.3.1',
    'cmake',
    'openexr-2.2.0',
    'ocio-1.1.0',
    'jpeg-1.5.3',
    'png-1.6.29',
    'tiff-4.1.0',
    'zlib-1.2.11',
    'boost-1.61.0',
    'fmt-6.1.2',
    'robin_map-0.6.2',
    'pybind11-2.4.3'
]

# requires = [
# ]

def commands():
    env.LD_LIBRARY_PATH.append('{root}/lib64')
    env.PATH.append('{root}/bin')
    env.PYTHONPATH.append('{root}/lib64/python2.7/site-packages')

    if building:
        env.CMAKE_MODULE_PATH.append('{root}/cmake')
