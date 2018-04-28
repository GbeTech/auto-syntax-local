from PyQt5.QtWidgets import QGroupBox

from gui.utils import boilerplate


class GroupBox(QGroupBox):
	
	def __init__(self, *args, **kwargs):
		super().__init__(*args)
		boilerplate(self, **kwargs)
	
	def toggle_enabled(self):
		self.setDisabled(self.isEnabled())
