import configparser

# import json
import os

#
CONFIG_DIRNAME = 'configuration'
CONFIG_FILENAME = 'config.ini'
CONFIG_FILENAME_PATH = os.path.join(CONFIG_DIRNAME, CONFIG_FILENAME)


def load_config_ini():
	try:
		with open(CONFIG_FILENAME_PATH, 'r') as f:
			_json = json.load(f)
		return _json
	except FileNotFoundError:
		raise FileNotFoundError('\n'.join([f'configuration file not found.',
		                                   f'CONFIG_DIRNAME: {CONFIG_DIRNAME}',
		                                   f'CONFIG_FILENAME: {CONFIG_FILENAME}',
		                                   f'CONFIG_FILENAME_PATH: {CONFIG_FILENAME_PATH}',
		                                   f'getcwd: {os.getcwd()}',
		                                   f'listdir: {os.listdir()}']))


class Config:
	ini = configparser.ConfigParser()
	ini.read(CONFIG_FILENAME_PATH)
	global_hotkey = ini['Hotkeys']['global_hotkey']
#
#

#
#
# class Hotkeys:
# 	def __init__(self, hotkeys: dict):
# 		self.global_hotkey = hotkeys['global_hotkey']
#
#
# class Config:
# 	_json = load_config_json()
# 	hotkeys = Hotkeys(_json['hotkeys'])
#
# 	@staticmethod
# 	def set_global_hotkey(hotkey):
# 		with open(CONFIG_FILENAME_PATH, 'r+') as f:
# 			json.dump(dict(Config._json), hotkey)
