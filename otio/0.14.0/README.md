# modified setup.py
```
pre-install python module
backports.tempfile

add cmake_args : -DGIT_UPDATE_SUBMODULES=OFF

# build command
rez-env python-2.7 cmake
rez-build -i
```
