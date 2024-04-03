## REQUIRES
```
Qt.py-1.2.5
```

## config.json
```
usdmanager-0.10.0-py2.7.egg/usdmanager/config.json
{
    "defaultPrograms": {
    },
    "themeSearchPaths": ["/backstage/libs/python/2.7.16/lib/python2.7/site-packages/django_crystal_small-2011.10.20-py2.7.egg/django_crystal_small/static/crystal"],
    "usdview": "usdviewer"
}
```

## Modified
```
usdmanager-0.10.0-py2.7.egg/usdmanager/__init__.py
# 636 line
'fontSizeAdjust': int(self.config.value("fontSizeAdjust", default['fontSizeAdjust'])) change to
'fontSizeAdjust': 0
# 2534 line
pathNoQuery = link.toString(QtCore.QUrl.RemoveQuery) change to
pathNoQuery = link.toString(QtCore.QUrl.PrettyDecoded)
```