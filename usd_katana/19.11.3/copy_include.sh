#!/bin/bash

# katana-4.0
KAT_VER=4.0
TARGET=/backstage/libs/usd_katana/19.11.3/katana-${KAT_VER}/third_party/katana/lib/usd/include
mkdir -p $TARGET/usdKatana
mkdir -p $TARGET/vtKatana

cp -rv ./build/katana-${KAT_VER}/usd_katana/src/usd_katana/lib/usdKatana/*.h $TARGET/usdKatana/
cp -rv ./build/katana-${KAT_VER}/usd_katana/src/usd_katana/lib/vtKatana/*.h $TARGET/vtKatana/


# katana-3.6
KAT_VER=3.6
TARGET=/backstage/libs/usd_katana/19.11.3/katana-${KAT_VER}/third_party/katana/lib/usd/include
mkdir -p $TARGET/usdKatana
mkdir -p $TARGET/vtKatana

cp -rv ./build/katana-${KAT_VER}/usd_katana/src/usd_katana/lib/usdKatana/*.h $TARGET/usdKatana/
cp -rv ./build/katana-${KAT_VER}/usd_katana/src/usd_katana/lib/vtKatana/*.h $TARGET/vtKatana/


# katana-3.5
KAT_VER=3.5
TARGET=/backstage/libs/usd_katana/19.11.3/katana-${KAT_VER}/third_party/katana/lib/usd/include
mkdir -p $TARGET/usdKatana
mkdir -p $TARGET/vtKatana

cp -rv ./build/katana-${KAT_VER}/usd_katana/src/usd_katana/lib/usdKatana/*.h $TARGET/usdKatana/
cp -rv ./build/katana-${KAT_VER}/usd_katana/src/usd_katana/lib/vtKatana/*.h $TARGET/vtKatana/
