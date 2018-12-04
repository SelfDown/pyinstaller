# -*- mode: python -*-

block_cipher = None


a = Analysis(['main.py'],
             pathex=['D:\\python\\pyinstall\\qinshan_data_collection'],
             binaries=[],
             datas=[("config.json","."),("database.db","."),("position.db","."),("templates/*.html","templates"),("static/*","static")],
             hiddenimports=["engineio.async_eventlet","eventlet.support.dns","engineio.async_gevent","service_database_sqlserver"],
             hookspath=["hooks"],
             runtime_hooks=["hooks/hook-eventlet.greenpool.py"],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='main',
          debug=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='main')
