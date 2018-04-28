from consts import MAGIC_FUNCTIONS
from main import magic_me
import pytest

tri_quote = '"""'


def test_0():
	assert magic_me(f'def foo') == f'def foo():\n\t'


def test_1():
	assert (magic_me(f'def foo p1') ==
	        f'def foo(p1):\n\t')


def test_2():
	assert (magic_me(f'def foo p1 p2') ==
	        f'def foo(p1, p2):\n\t')


def test_3():
	assert (magic_me('\tdef foo p1 p2') ==
	        f'def foo(self, p1, p2):\n\t')


def test_3_andahalf():
	assert (magic_me('    def foo p1 p2') ==
	        f'def foo(self, p1, p2):\n\t')


def test_4():
	assert (magic_me(f'def foo p1 .None') ==
	        f'def foo(p1=None):\n\t')


def test_5():
	assert (magic_me(f'def foo p1 .None p2') ==
	        f'def foo(p1=None, p2):\n\t')


def test_6_a():
	assert (magic_me(f'def foo p1 .False p2') ==
	        f'def foo(p1=False, p2):\n\t')


def test_6_b():
	assert (magic_me(f'def foo p1 .True p2') ==
	        f'def foo(p1=True, p2):\n\t')


def test_6_c():
	assert (magic_me(f'def foo p1 .1 p2') ==
	        f'def foo(p1=1, p2):\n\t')


def test_7():
	expected = f"""def foo(p1):
	{tri_quote}
	:type p1: str
	{tri_quote}
	"""
	assert (magic_me(f'def foo p1 str') == expected)


def test_8():
	expected = f"""def foo(p1):
	{tri_quote}
	:rtype: str
	{tri_quote}
	"""
	assert (magic_me(f'def foo str p1') == expected)


def test_9():
	expected = f"""def foo(p1):
	{tri_quote}
	:type p1: str
	:rtype: str
	{tri_quote}
	"""
	assert (magic_me(f'def foo str p1 str') == expected)


def test_10():
	assert (magic_me(f'def foo p1 .default p2') ==
	        "def foo(p1='default', p2):\n\t")


def test_11():
	expected = f"""def foo(p1='default', p2):
	{tri_quote}
	:type p2: str
	{tri_quote}
	"""
	assert (magic_me(f'def foo p1 .default p2 str') == expected)


def test_12():
	assert (magic_me(f'my = def foo p1 .default p2 str') ==
	        f'my = def foo p1 .default p2 str')


def test_13():
	for mag_fn in MAGIC_FUNCTIONS:
		mandatory_args = ', '.join(['self'] + MAGIC_FUNCTIONS[mag_fn])
		assert (magic_me(f'\tdef {mag_fn}') ==
		        f"def __{mag_fn}__({mandatory_args}):\n\t")


def test_14():
	expected = f"""def __init__(self, age):
	self.age = age
	"""
	assert (magic_me(f'\tdef init age') == expected)


def test_15():
	expected = f"""def __init__(self, age, name='moshe'):
	{tri_quote}
	:type age: int
	{tri_quote}
	self.age = age
	self.name = name
	"""
	assert (magic_me(f'\tdef init age int name .moshe') == expected)


def test_16():
	expected = f"""def what(p1='lol'):
	{tri_quote}
	:type p1: str
	{tri_quote}
	"""
	assert magic_me(f"def what p1 str .lol") == expected


def test_17():
	expected = f"""def what(p1='lol'):
	{tri_quote}
	:type p1: str
	:rtype: int
	{tri_quote}
	"""
	assert magic_me(f"def what int p1 str .lol") == expected


def test_18():
	expected = f"""def what(p1=1):
	{tri_quote}
	:type p1: str
	:rtype: int
	{tri_quote}
	"""
	assert magic_me(f"def what int p1 str .1") == expected


def test_19():
	expected = f"""def what(*args):
	"""
	assert magic_me(f"def what args") == expected


def test_20():
	expected = f"""def what(**kwargs):
	"""
	assert magic_me(f"def what kwargs") == expected


def test_21():
	expected = f"""def what(*args, **kwargs):
	"""
	assert magic_me(f"def what args kwargs") == expected


@pytest.mark.skip
def test_119():
	expected = f"""def what(p1='1'):
	{tri_quote}
	:type p1: str
	:rtype: int
	{tri_quote}
	"""
	assert magic_me(f"def what int p1 str 1") == expected
