import ctypes

from PyQt5.QtWidgets import QApplication, QMainWindow

from src import UI

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


if __name__ == "__main__":
	import sys

	if check_if_admin():
		app = QApplication(sys.argv)
		# noinspection PyArgumentList
		MainWindow = QMainWindow()
		"""# keybinder
		keybinder.init()
		win_event_filter = WinEventFilter(keybinder)
		event_dispatcher = QAbstractEventDispatcher.instance()
		event_dispatcher.installNativeEventFilter(win_event_filter)"""

		ui = UI()
		ui.setupUi(MainWindow)

		MainWindow.show()

		sys.exit(app.exec_())

	else:
		ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, "", None, 1)
