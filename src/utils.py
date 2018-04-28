# import keyboard as kb
import asyncio
from contextlib import contextmanager

from pyperclip import paste


def _is_builtin_const(target):
	return target in ['None', 'True', 'False']


# def add_hotkey(*, hotkey, fn, loop):
# 	kb.add_hotkey(hotkey,  # FASTER W/O TOR AND SUPP
# 	              callback=lambda: kb.release(hotkey) or fn(loop))


def delete_many(src, *args):
	for arg in args:
		src = src.replace(arg, '')
	return src


def get_singular(clp):
	"""
	:type clp: str
	:rtype: str
	"""
	# clp = clp.replace("'", '')
	clp = delete_many(clp, "'", 'self.')
	if len(clp) >= 2 and clp.endswith('s'):
		return clp[:-1]
	elif clp.startswith('i'):
		return 'item'
	else:
		return clp[0]


@asyncio.coroutine
def clipboard_changed():
	prev_clp = paste()
	count = 0
	while True:
		yield from asyncio.sleep(0.01)
		count += 1
		new_clp = paste()
		if new_clp != prev_clp or count >= 7:
			break
	print(f'polled {count} times until clpbrd change')
	return count


@contextmanager
def ignore(*exceptions):
	try:
		yield
	except exceptions:
		pass


def stringify(target, dblquote=False):
	surround = '"' if dblquote else "'"
	return surround_with(surround=surround, to_surround=target)


def stringify_if_not_builtin_const_or_digit(target):
	if not target.isdigit() and not _is_builtin_const(target):
		return stringify(target)
	else:
		return target


def surround_with(surround, to_surround):
	return f'{surround}{to_surround}{surround}'


def xnor(a, b):
	return not a ^ b
