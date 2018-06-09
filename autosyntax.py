import ctypes

from PyQt5.QtWidgets import QApplication, QMainWindow

from src import UI
import sys
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


def launch_gui():
	app = QApplication(sys.argv)
	# noinspection PyArgumentList
	MainWindow = QMainWindow()
	ui = UI()
	ui.setupUi(MainWindow)
	MainWindow.show()
	sys.exit(app.exec_())


def launch():
	from configuration import Config
	kb_utils.add_hotkey(
		hotkey=Config.hotkeys.global_hotkey,
		callback=kb_utils.do_magic,
		suppress=True, trigger_on_release=True)
	kb_utils.wait()


if __name__ == "__main__":
	if check_if_admin():
		# launch_gui()
		if 'gui' in sys.argv:
			launch_gui()
		else:
			launch()

	else:
		ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, "", None, 1)
