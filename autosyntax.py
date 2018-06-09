import ctypes

from PyQt5.QtWidgets import QApplication, QMainWindow

from src import UI
from sys import argv, exit, executable
from src.utils import kb_utils

"""class WinEventFilter(QAbstractNativeEventFilter):
	def __init__(self, keybinder):
		self.keybinder = keybinder
		super().__init__()
	
	# noinspection PyMethodOverriding
	def nativeEventFilter(self, eventType, message):
		ret = self.keybinder.handler(eventType, message)
		return ret, 0"""


def check_if_admin():
	try:
		return ctypes.windll.shell32.IsUserAnAdmin()
	except Exception:
		return False


def start_gui():
	app = QApplication(argv)
	# noinspection PyArgumentList
	MainWindow = QMainWindow()
	ui = UI()
	ui.setupUi(MainWindow)
	MainWindow.show()
	exit(app.exec_())


def start():
	from configuration import Config
	kb_utils.add_hotkey(
		hotkey=Config.hotkeys.global_hotkey,
		callback=kb_utils.do_magic,
		suppress=True, trigger_on_release=True)
	kb_utils.wait()


def align(key, value):
	# tabs_num = 3
	tabs_num = 3 - int((len(key) - 8) / 8)
	# if len(key) >= 24:
	# 	tabs_num = 1
	# elif len(key) >= 16:
	# 	tabs_num = 2

	tabs = '\t' * tabs_num
	return f'{key}{tabs}{value}'


def help():
	print('\n'.join([f'\nAUTOSYNTAX HELP',
	                 f'----------------',
	                 f'commands:',
	                 f'--------',
	                 align('autosyntax start', 'start autosyntax'),
	                 align('autosyntax gui', 'start autosyntax with gui'),
	                 align('autosyntax --help', 'show this message'),
	                 align('autosyntax --config [setting]', 'show configuration wizard [of setting]'),
	                 ]))


def config():
	print('\n'.join([f'\nAUTOSYNTAX CONFIGURATION',
	                 f'------------------------',
	                 f'commands:',
	                 f'--------',
	                 align('autosyntax start', 'start autosyntax'),
	                 align('autosyntax gui', 'start autosyntax with gui'),
	                 align('autosyntax --help', 'show this message'),
	                 align('autosyntax --config', 'show configuration wizard'),
	                 ]))


if __name__ == "__main__":
	if check_if_admin():
		try:
			if argv[1] == 'start':
				start()

			elif argv[1] == 'gui':
				start_gui()

			elif argv[1] == '--help':
				help()

			elif argv[1] == '--config':
				config()
			else:
				help()
		except IndexError:
			help()
	else:
		ctypes.windll.shell32.ShellExecuteW(None, "runas", executable, "", None, 1)
