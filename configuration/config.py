import json
import os
from collections import namedtuple

CONFIG_DIRNAME = 'configuration'
CONFIG_FILENAME = 'config.json'
CONFIG_FILENAME_PATH = os.path.join(CONFIG_DIRNAME, CONFIG_FILENAME)


class Hotkeys:
	def __init__(self, hotkeys: dict):
		self.global_hotkey = hotkeys['global_hotkey']


class Config:
	try:
		with open(CONFIG_FILENAME_PATH, 'r') as f:
			_json = json.load(f)
		hotkeys = Hotkeys(_json['hotkeys'])
		print()
	except FileNotFoundError:
		raise FileNotFoundError('\n'.join([f'configuration file not found.',
		                                   f'CONFIG_DIRNAME: {CONFIG_DIRNAME}',
		                                   f'CONFIG_FILENAME: {CONFIG_FILENAME}',
		                                   f'CONFIG_FILENAME_PATH: {CONFIG_FILENAME_PATH}',
		                                   f'getcwd: {os.getcwd()}',
		                                   f'listdir: {os.listdir()}']))
