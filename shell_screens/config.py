from configuration import ConfigMgr
from . import MainScreen, Subscreen


def hotkeys(hotkeys=None):
	ALIASES = {
		'global':        'global_hotkey',
		'global_hotkey': 'global_hotkey'}
	if hotkeys is None:
		ss = Subscreen('hotkeys config', {
			'global': 'set the global hotkey'})
		ss.display()
		_choice = input('choose hotkey to set: ')
		_value = input('hotkey value: ')
		print(f'{_choice} hotkey was changed to: {_value}')
		ConfigMgr.set('Hotkeys', ALIASES[_choice], _value)

	else:
		for hotkey in hotkeys:
			_choice, _, _value = hotkey.partition('=')
			ConfigMgr.set('Hotkeys', ALIASES[_choice], _value)


def operators():
	ss = Subscreen('operators config', {
		'list':     'configure list operator',
		'dict':     'configure dict operator',
		'tuple':    'configure tuple operator',
		'for':      'configure for operator',
		'listcomp': 'configure listcomp operator',
		'class':    'configure class operator',
		'def':      'configure def operator',
		'str':      'configure str operator',
		'print':    'configure print operator',
		})
	ss.display()


def main(cmnd=None):
	cmnds_fns = {
		'hotkeys':   hotkeys,
		'operators': operators}
	if cmnd is None:
		s = MainScreen('AUTOSYNTAX CONFIGURATION')
		s.add_subscreen('commands', {
			'hotkeys':   'configure hotkeys',
			'operators': 'configure operators'})

		s.display()
		_input = input('type command: ')
		try:
			cmnds_fns[_input]()
		except KeyError:
			s.display()

	else:
		# try:
		args = cmnd[1:] if bool(cmnd[1:]) else None
		cmnds_fns[cmnd[0]](args)
# except IndexError:
# 	cmnds_fns[cmnd[0]]()
