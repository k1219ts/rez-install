name = 'clang'
version = '7.0.0'

build_requires = [
    'gcc-6.3.1',
    'cmake'
]

build_command = 'bash {root}/build.sh {install}'

def commands():
    env.PATH.prepend('{root}/bin')
    env.LD_LIBRARY_PATH.append('{root}/lib')
    if building:
        env.CMAKE_MODULE_PATH.append('{root}/lib/cmake/clang')
        env.CMAKE_MODULE_PATH.append('{root}/lib/cmake/llvm')
        env.LLVM_INSTALL_DIR.set('{root}')
