import asyncio

import keyboard as kb
from PyQt5.QtCore import QRect, Qt
from PyQt5.QtGui import QKeySequence
from PyQt5.QtWidgets import QKeySequenceEdit, QWidget
from pyperclip import copy, paste

from expression import Expression
from gui.utils import boilerplate
from utils import clipboard_changed, ignore


# from pyqtkeybind import keybinder


class KeySequenceEdit(QKeySequenceEdit):
	_hotkeys = {}
	_gui_focused = False
	_win_id = None
	
	def __init__(self, *args, **kwargs):
		super().__init__(*args)
		boilerplate(self, **kwargs)
		self.op_keyword = kwargs['op_keyword']
		self.general_loop = asyncio.get_event_loop()
		
		# checkmark
		self._checkmark = self._init_checkmark()
		
		# noinspection PyUnresolvedReferences
		super().editingFinished.connect(self._editingFinished)
		
		self._validate_key_sequence()
	
	@staticmethod
	def set_win_id(value):
		KeySequenceEdit._win_id = value
	
	@staticmethod
	def set_gui_has_focus(value):
		KeySequenceEdit._gui_focused = value
	
	# Escape to clear
	def keyPressEvent(self, QKeyEvent):
		if QKeyEvent.key() == Qt.Key_Escape:
			self.clear()
			self._remove_current_keyboard_hotkey()
		else:
			super().keyPressEvent(QKeyEvent)
	
	# call setKeySequence with current KeySequence
	def _editingFinished(self, *args):
		self.setKeySequence(self.keySequence().toString())
	
	# call _validate
	def setKeySequence(self, key_seq: str, **kwargs):
		super().setKeySequence(QKeySequence().fromString(key_seq))
		self._validate_key_sequence()
	
	def _validate_key_sequence(self):
		# todo: if not collide with others..
		if not self.keySequence().isEmpty():
			self._set_keyboard_hotkey(self.keySequence().toString())
			self._toggle_checkmark(True)
		else:
			pass
	
	def _init_checkmark(self):
		# noinspection PyArgumentList
		_checkmark = QWidget(self.parent())
		geo: QRect = self.geometry()
		_checkmark.setGeometry(QRect(geo.right() + 20, geo.y() - 2, 25, 25))
		return _checkmark
	
	def _toggle_checkmark(self, green=True):
		bg = lambda file: f'background: url(src/gui/visuals/{file}.png)'
		if green:
			self._checkmark.setStyleSheet(bg('greensmall25'))
		else:
			self._checkmark.setStyleSheet(bg('redsmall25'))
	
	# keyboard
	def _set_keyboard_hotkey(self, hotkey):
		self._remove_current_keyboard_hotkey()
		KeySequenceEdit._hotkeys[self.op_keyword] = hotkey
		print(f'registering: {hotkey}')
		# keybinder.register_hotkey(self._win_id,
		#                           hotkey, self._ready_expression)
		
		kb.add_hotkey(hotkey=hotkey, callback=self._ready_expression, suppress=True)
	
	def _remove_current_keyboard_hotkey(self):
		# remove current operator's keyboard hotkey
		with ignore(KeyError):
			print(f'unregistering: {KeySequenceEdit._hotkeys[self.op_keyword]}')
			# keybinder.unregister_hotkey(self._win_id,
			#                             KeySequenceEdit._hotkeys[self.op_keyword])
			
			kb.remove_hotkey(KeySequenceEdit._hotkeys[self.op_keyword])
	
	def _ready_expression(self):
		if not KeySequenceEdit._gui_focused:
			# print(f'releasing: {KeySequenceEdit._hotkeys[self.op_keyword]}')
			# kb.release(KeySequenceEdit._hotkeys[self.op_keyword])
			# print(kb.is_pressed(KeySequenceEdit._hotkeys[self.op_keyword]))
			kb.send('home+home+shift+end, ctrl+c')
			self.general_loop.run_until_complete(clipboard_changed())
			clp = paste()
			result = self._get_expression(clp)
			copy(result)
			kb.send('ctrl+v')
	
	def _get_expression(self, clp):
		line = Expression(clp, self.op_keyword)
		result = line.finalize()
		return result
