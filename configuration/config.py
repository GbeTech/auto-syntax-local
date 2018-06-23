import configparser

# import json
import os

#
CONFIG_DIRNAME = 'configuration'
CONFIG_FILENAME = 'config.ini'
CONFIG_FILE_FULLPATH = os.path.join(CONFIG_DIRNAME, CONFIG_FILENAME)

INI_REPR = {
	'Hotkeys': {
		'quit_hotkey':   'ctrl+c',
		'global_hotkey': 'ctrl+g'},
	'General': {
		'type_hints_new': 'True'}
	}


def _load_config_ini():
	try:
		ini = configparser.ConfigParser()
		ini.read(CONFIG_FILE_FULLPATH)
		return ini
	except FileNotFoundError as e:
		raise FileNotFoundError('\n'.join([f'configuration file not found.',
		                                   f'CONFIG_DIRNAME: {CONFIG_DIRNAME}',
		                                   f'CONFIG_FILENAME: {CONFIG_FILENAME}',
		                                   f'CONFIG_FILE_FULLPATH: {CONFIG_FILE_FULLPATH}',
		                                   f'getcwd: {os.getcwd()}',
		                                   f'listdir: {os.listdir()}',
		                                   f'original error: {e}']))


def _validate_config_ini(ini):
	empty_entries = {}
	for section, k_v_pairs in INI_REPR.items():
		for key, value in k_v_pairs.items():
			try:
				if ini[section][key] != '':
					continue
			except KeyError:
				empty_entries[section] = {key: value}
	return empty_entries


def _set_ini_entry(ini, section, key, value):
	ini[section][key] = value
	with open(CONFIG_FILE_FULLPATH, 'w') as configfile:
		ini.write(configfile)
	return ini


def str_to_bool(value):
	return value.lower() == 'true'


class Hotkeys:
	def __init__(self, hotkeys: dict):
		self.global_hotkey = hotkeys['global_hotkey']
		self.quit_hotkey = hotkeys['quit_hotkey']


class General:
	def __init__(self, options: dict):
		self.type_hints_new = str_to_bool(options['type_hints_new'])


class ConfigMgr:
	_ini = _load_config_ini()
	empty_entries = _validate_config_ini(_ini)
	if bool(empty_entries):
		print(f'config.ini validation failed. Restoring missing entries defaults...')
		for section, k_v_pairs in empty_entries.items():
			for key, value in k_v_pairs.items():
				print(f'  Restoring [{section}] | {key}: {value}')
				_ini = _set_ini_entry(_ini, section, key, value)

		print('config.ini rebuilt successfully.')
	else:
		print('config.ini validation successful.')
	hotkeys = Hotkeys(_ini['Hotkeys'])
	general = General(_ini['General'])

	@staticmethod
	def set(section, key, value):
		return _set_ini_entry(ConfigMgr._ini, section, key, value)
