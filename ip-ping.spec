# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['ip-ping.py'],
    pathex=[],
    binaries=[],
    datas=[('assets/', 'assets/')],  # Add relative paths for assets
    hiddenimports=[],  # Include necessary hidden imports
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
    name='ip-ping',  # Exported executable name
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,  # Set to True for console-based apps
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['assets/icon.ico'],  # Add relative path for the icon
)