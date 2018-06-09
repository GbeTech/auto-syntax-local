from shell_screens.screen import align, Screen


def main():
	s = Screen('AUTOSYNTAX HELP')
	s.add_subscreen('commands', {
		'autosyntax start':              'start autosyntax',
		'autosyntax gui':                'start autosyntax with gui',
		'autosyntax --help':             'show this message',
		'autosyntax --config [setting]': 'show configuration wizard [of setting]'})

	s.display()
