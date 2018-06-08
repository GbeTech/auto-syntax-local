import ctypes

from PyQt5.QtWidgets import QApplication, QMainWindow

from src import UI
import sys

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
	if check_if_admin():
		if 'gui' in sys.argv:
			app = QApplication(sys.argv)
			# noinspection PyArgumentList
			MainWindow = QMainWindow()

			ui = UI()
			ui.setupUi(MainWindow)

			MainWindow.show()

			sys.exit(app.exec_())
		else:
			print('no gui')

	else:
		ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, "", None, 1)
