from typing import List


def align(msgs: dict) -> List[str]:
	longest_key_len = max([len(key) for key in msgs.keys()])
	tabs_max = int(longest_key_len / 8)
	ret = []
	for key, value in msgs.items():
		# ONLY NEEDED IN PYCHARM?
		# tabs_difference = int((longest_key_len - len(key)) / 8)

		tabs_num = tabs_max - int(len(key) / 8) + 1
		tabs = '\t' * tabs_num
		ret.append(f'{key}{tabs}{value}')
	return ret


def _underline(line) -> str:
	return '\n'.join([f'{line}',
	                  '-' * len(line)])


from abc import ABC, abstractmethod


class Screen(ABC):
	@abstractmethod
	def __init__(self, title, *args):
		self.title = f'\n{_underline(title)}'

	def display(self):
		print(f'{self}\n')


class Subscreen(Screen):
	def __init__(self, title, msgs: dict):
		super().__init__(title)
		# self.title = f'\n{_underline(title)}'
		self.msgs: [] = align(msgs)

	def __str__(self):
		return '\n'.join([self.title, *self.msgs])


class MainScreen(Screen):
	def __init__(self, title):
		super().__init__(title)
		self.subscreens: List[Subscreen] = []

	def __str__(self):
		return '\n'.join([self.title, *[ss.__str__() for ss in self.subscreens]])

	def add_subscreen(self, title, msgs: dict):
		self.subscreens.append(Subscreen(title, msgs))
