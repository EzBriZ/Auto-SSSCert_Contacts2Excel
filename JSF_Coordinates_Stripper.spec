# -*- mode: python ; coding: utf-8 -*-

from PyInstaller.utils.hooks import collect_all

# Collect all necessary files for geopandas and its main dependencies
geopandas_datas, geopandas_binaries, geopandas_hiddenimports = collect_all('geopandas')
fiona_datas, fiona_binaries, fiona_hiddenimports = collect_all('fiona')
shapely_datas, shapely_binaries, shapely_hiddenimports = collect_all('shapely')
pyproj_datas, pyproj_binaries, pyproj_hiddenimports = collect_all('pyproj')
rtree_datas, rtree_binaries, rtree_hiddenimports = collect_all('rtree')

a = Analysis(
    ['JSF_Coordinates_Stripper.py'],
    pathex=[],
    binaries=(
        geopandas_binaries + 
        fiona_binaries + 
        shapely_binaries + 
        pyproj_binaries + 
        rtree_binaries
    ),
    datas=(
        geopandas_datas + 
        fiona_datas + 
        shapely_datas + 
        pyproj_datas + 
        rtree_datas
    ),
    hiddenimports=(
        geopandas_hiddenimports + 
        fiona_hiddenimports + 
        shapely_hiddenimports + 
        pyproj_hiddenimports + 
        rtree_hiddenimports +
		['utm', 'openpyxl']
    ),
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='JSF_Coordinates_Stripper',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
