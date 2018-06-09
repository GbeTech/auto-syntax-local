from shell_screens.screen import Screen, Subscreen


def hotkeys():
	ss = Subscreen('hotkeys config', {
		'global': 'set the global hotkey'})
	ss.display()
	_choice = input('choose hotkey to set: ')
	_value = input('value: ')
	print(f'{_choice} hotkey was changed to: {_value}')


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


def main():
	cmnds_fns = {
		'hotkeys':   hotkeys,
		'operators': operators}
	s = Screen('AUTOSYNTAX CONFIGURATION')
	s.add_subscreen('commands', {
		'hotkeys':   'configure hotkeys',
		'operators': 'configure operators'})

	s.display()
	_input = input('type command: ')
	try:
		cmnds_fns[_input]()
	except KeyError:
		s.display()
