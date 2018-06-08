# import keyboard as kb
import asyncio

from pyperclip import paste


@asyncio.coroutine
def clipboard_changed():
	prev_clp = paste()
	count = 0
	while True:
		yield from asyncio.sleep(0.0001)
		count += 1
		new_clp = paste()
		if new_clp != prev_clp or count >= 45:
			break
	print(f'\n\tpollefd {count} times until clpbrd change')
	return count

# def add_hotkey(*, hotkey, fn, loop):
# 	kb.add_hotkey(hotkey,  # FASTER W/O TOR AND SUPP
# 	              callback=lambda: kb.release(hotkey) or fn(loop))
