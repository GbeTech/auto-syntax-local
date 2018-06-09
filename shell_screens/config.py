from shell_screens.screen import align, Screen


def main():
	s = Screen('AUTOSYNTAX CONFIGURATION')
	s.add_subscreen('commands', {
		'hotkeys':   'configure hotkeys',
		'operators': 'configure operators'})

	s.display()
	_input = input()
