# -*- mode: python -*-

block_cipher = None


a = Analysis(['Down_PPT.py'],
             pathex=['C:\\Users\\49394\\Desktop\\2'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='Down_PPT',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False , icon='ppt.ico')
