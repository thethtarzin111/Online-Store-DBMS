# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['os_login.py'],
    pathex=[],
    binaries=[],
    datas=[('D:\\Database\\project\\os_login.py', '.'), ('D:\\Database\\project\\os_main.py', '.'), ('D:\\Database\\project\\os_customer.py', '.'), ('D:\\Database\\project\\os_order.py', '.'), ('D:\\Database\\project\\os_product.py', '.')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='os_login',
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
