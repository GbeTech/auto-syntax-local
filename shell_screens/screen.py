from typing import List


def align(msgs: dict):
	longest_key = max([len(key) for key in msgs.keys()])
	tabs_max = int(longest_key / 8)
	ret = []
	for key, value in msgs.items():
		tabs_num = 1 + tabs_max - int(len(key) / 8)
		tabs = '\t' * tabs_num
		ret.append(f'{key}{tabs}{value}')
	return ret


def _underline(line) -> str:
	return '\n'.join([f'{line}',
	                  '-' * len(line)])


class _Subscreen:
	def __init__(self, title, msgs: dict):
		self.title = _underline(title)
		self.msgs = align(msgs)

	def __str__(self):
		return '\n'.join([self.title, *self.msgs])


class Screen:

	def __init__(self, title):
		self.title = f'\n{_underline(title)}'
		self.subscreens: List[_Subscreen] = []

	# for subtitle in subtitles:
	# 	self.subscreens.append(_Subscreen(_underline(subtitle)))

	def __str__(self):
		return '\n'.join([self.title, *[ss.__str__() for ss in self.subscreens]])

	def add_subscreen(self, title, msgs: dict):
		self.subscreens.append(_Subscreen(title, msgs))

	def display(self):
		print(self)

# _underline_many(subtitles)

# def _underline_many(self, lines) -> List[str]:
# 	return [_underline(line) for line in lines]
