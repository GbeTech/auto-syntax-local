import keyboard as kb
import asyncio

from pyperclip import paste, copy


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

def _do_magic(loop):
	print('sending end+shift+home+shift+home, ctrl+c')
	kb.send('end+shift+home+shift+home, ctrl+c')
	loop.run_until_complete(clipboard_changed())
	clp = paste()
	print('sending home+shift+end')
	kb.send('home+shift+end')
	is_indented = '\t' in clp or '    ' in clp
	result = _get_expression(clp, is_indented)
	copy(result)
	print('sending ctrl+v')
	kb.send('ctrl+v')

def _get_expression(clp, is_indented):
	line = Expression(clp, is_indented, self.op_keyword)
	result = line.finalize()
	return result