# DOCUMENT
```
https://openimageio.readthedocs.io/en/release-2.1.18.1/
```

# oiiotool
```
# exr to jpg
oiiotool input.exr --colorconfig ${REZ_OCIO_CONFIGS_ROOT}/config.ocio --colorconvert aces out_rec709 -o output.jpg
```

# python
```
import OpenImageIO as oiio
img  = oiio.ImageInput.open(filename)
attrs= img.spec().extra_attribs
for i in range(len(attrs)):
    print attrs[i].name, attrs[i].type, attrs[i].value
```
