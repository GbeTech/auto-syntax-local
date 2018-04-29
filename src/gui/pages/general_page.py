from gui.pages.page import Page


class GeneralPage(Page):

	def __init__(self, *args, **kwargs):
		super().__init__('Main Hotkey:', *args, **kwargs)
		self.hotkey_edit.setKeySequence('ctrl+e')
