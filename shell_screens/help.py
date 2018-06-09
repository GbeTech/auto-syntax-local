from shell_screens.screen import align


def main():
	print('\n'.join([f'\nAUTOSYNTAX HELP',
	                 f'----------------',
	                 f'commands:',
	                 f'--------',
	                 *align({
		                 'autosyntax start':              'start autosyntax',
		                 'autosyntax gui':                'start autosyntax with gui',
		                 'autosyntax --help':             'show this message',
		                 'autosyntax --config [setting]': 'show configuration wizard [of setting]'})]))
