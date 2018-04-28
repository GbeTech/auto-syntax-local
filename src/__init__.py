# from PyQt5.QtCore import QAbstractNativeEventFilter, QAbstractEventDispatcher
# import keyboard as kb
# from PyQt5.QtWidgets import QApplication, QMainWindow
# from pyqtkeybind import keybinder
from PyQt5.QtWidgets import QApplication, QMainWindow

# from PyQt5_L.QtCore.QAbstractEventDispatcher import QAbstractEventDispatcher
# from PyQt5_L.QtCore.QAbstractNativeEventFilter import QAbstractNativeEventFilter
# from PyQt5_L.QtWidgets.QApplication import QApplication
# from PyQt5_L.QtWidgets.QMainWindow import QMainWindow
from gui.UI import UI

"""class WinEventFilter(QAbstractNativeEventFilter):
	def __init__(self, keybinder):
		self.keybinder = keybinder
		super().__init__()
	
	# noinspection PyMethodOverriding
	def nativeEventFilter(self, eventType, message):
		ret = self.keybinder.handler(eventType, message)
		return ret, 0"""

if __name__ == "__main__":
	import sys
	
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
