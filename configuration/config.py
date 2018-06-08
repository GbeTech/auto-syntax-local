import configparser

# import json
import os

#
CONFIG_DIRNAME = 'configuration'
CONFIG_FILENAME = 'config.ini'
CONFIG_FILENAME_PATH = os.path.join(CONFIG_DIRNAME, CONFIG_FILENAME)


def _load_config_ini():
	try:
		ini = configparser.ConfigParser()
		ini.read(CONFIG_FILENAME_PATH)
		return ini
	except FileNotFoundError as e:
		raise FileNotFoundError('\n'.join([f'configuration file not found.',
		                                   f'CONFIG_DIRNAME: {CONFIG_DIRNAME}',
		                                   f'CONFIG_FILENAME: {CONFIG_FILENAME}',
		                                   f'CONFIG_FILENAME_PATH: {CONFIG_FILENAME_PATH}',
		                                   f'getcwd: {os.getcwd()}',
		                                   f'listdir: {os.listdir()}',
		                                   f'original error: {e}']))


class Hotkeys:
	def __init__(self, hotkeys: dict):
		self.global_hotkey = hotkeys['global_hotkey']


class Config:
	_ini = _load_config_ini()
	hotkeys = Hotkeys(_ini['Hotkeys'])
