# -*- mode: python ; coding: utf-8 -*-

from PyInstaller.archive.pyz_crypto import PyiBlockCipher

block_cipher = PyiBlockCipher(key="1234QAQA")

a = Analysis(['wnd_server_code.py'],
             pathex=['E:\\PycharmProjects\\PyNetAuth\\server'],
             binaries=[],
             datas=[],
             hiddenimports=["PySide2.QtXml"],
             hookspath=[],
             runtime_hooks=[],
             excludes=["Cython", "WMI", "comtypes"],
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
          name='wnd_server_code',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=False,
          console=False,
		  icon="F:\\icon\\1.ico")  # 图标自己改
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=False,
               upx_exclude=[],
               name='wnd_server_code')
