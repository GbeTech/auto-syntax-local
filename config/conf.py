import json
import os
from definitions import CONFIG_PATH

CONFIG_FILE = os.path.join(CONFIG_PATH, 'conf.json')
with open(CONFIG_FILE, "r") as read_file:
    CFG = json.load(read_file)