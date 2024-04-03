name = 'rapidjson'
version = '1.1.0'

build_requires = [
    'cmake-3.14.6'
]

def commands():
    env.CMAKE_MODULE_PATH.prepend('{root}/lib/cmake/RapidJSON')
    env.RAPIDJSON_INCLUDE_DIRS.set('{root}/include')
