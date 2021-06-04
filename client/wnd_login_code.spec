# -*- mode: python ; coding: utf-8 -*-

from PyInstaller.archive.pyz_crypto import PyiBlockCipher

block_cipher = PyiBlockCipher(key="QWER")


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
          upx=False,
          console=True,
          icon="F:\\icon\\2.ico")  # 图标自己改
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=False,
               upx_exclude=[],
               name='wnd_login_code')
