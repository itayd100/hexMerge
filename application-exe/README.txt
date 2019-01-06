pyinstaller + kivy with filechooser:

1) pyinstaller --onefile --hidden-import win32timezone main.py
2) python -m PyInstaller main.spec
3) spec:
-------------------------------------------------------------------
# -*- mode: python -*-
from kivy.deps import sdl2, glew

block_cipher = None


a = Analysis(['main.py'],
             pathex=['D:\\python\\MergeHex'],
             binaries=[],
             datas=[('D:\\python\\MergeHex\\mergehex.kv', 'data')],
             hiddenimports=['win32timezone'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)


exe = EXE(pyz,Tree('D:\\python\\MergeHex'),
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='main',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
		  *[Tree(p) for p in (sdl2.dep_bins + glew.dep_bins)],
          console=True )

-------------------------------------------------------------------