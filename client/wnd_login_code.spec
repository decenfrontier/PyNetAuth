# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['wnd_login_code.py'],
             pathex=['E:\\PycharmProjects\\PyNetAuth\\client'],
             binaries=[],
             datas=[
				("dll/*", "dll"),
			 ],
             hiddenimports=["PySide2.QtXml"],
             hookspath=[],
             runtime_hooks=[],
             excludes=["Cython", "pymysql"],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='wnd_login_code',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='wnd_login_code')
