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


def align_old(key, value):
	tabs_num = 3 - int((len(key) - 8) / 8)
	tabs = '\t' * tabs_num
	return f'{key}{tabs}{value}'


def align(msgs: dict):
	longest_key = max([len(key) for key in msgs.keys()])
	tabs_max = int(longest_key / 8)
	ret = []
	for key, value in msgs.items():
		tabs_num = 1 + tabs_max - int(len(key) / 8)
		tabs = '\t' * tabs_num
		ret.append(f'{key}{tabs}{value}')
	return ret


def help():
	print('\n'.join([f'\nAUTOSYNTAX HELP',
	                 f'----------------',
	                 f'commands:',
	                 f'--------',
	                 *align({
		                 'autosyntax start':              'start autosyntax',
		                 'autosyntax gui':                'start autosyntax with gui',
		                 'autosyntax --help':             'show this message',
		                 'autosyntax --config [setting]': 'show configuration wizard [of setting]'})]))


def config():
	print('\n'.join([f'\nAUTOSYNTAX CONFIGURATION',
	                 f'------------------------',
	                 f'commands:',
	                 f'--------',
	                 *align({
		                 'hotkeys':   'configure hotkeys',
		                 'operators': 'configure operators'}),
	                 ]))
	_input = input()


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
			config()
	else:
		ctypes.windll.shell32.ShellExecuteW(None, "runas", executable, "", None, 1)
