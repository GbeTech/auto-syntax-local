import sys

from cx_Freeze import Executable, setup

base = None
if sys.platform == 'win32':
	base = 'Win32GUI'
buildOptions = dict(
	packages=['keyboard', 'asyncio'],
	excludes=['tkinter'],
	build_exe='build_light',
	include_files=['gui/visuals/greensmall25.png', 'gui/visuals/redsmall25.png']
	)

executables = [
	Executable('autosyntax.py', base=base)
	]

setup(name='Test',
      version='1.0',
      description='',
      options=dict(build_exe=buildOptions),
      executables=executables)
