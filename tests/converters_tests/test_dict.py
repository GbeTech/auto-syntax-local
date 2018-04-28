from main import magic_me


def test_0():
	assert magic_me('dict hi bye') == "{'hi': 'bye'}"


def test_1():
	assert magic_me('dict hi .bye') == "{'hi': bye}"


def test_3():
	assert magic_me('my = dict hi bye') == "my = {'hi': 'bye'}"


def test_4():
	assert magic_me('my = dict hi .bye') == "my = {'hi': bye}"


def test_5():
	assert magic_me('dict hi bye lol') == "{'hi': 'bye'} lol"


def test_6():
	assert magic_me('dict hi bye .lol') == "{'hi': 'bye'} lol"


def test_7():
	assert magic_me('my = dict hi bye lol') == "my = {'hi': 'bye'} lol"


def test_8():
	assert magic_me('dict min max hi bye') == "{min(max(hi)): 'bye'}"


def test_9():
	assert magic_me('dict min max .hi bye') == "{min(max('hi')): 'bye'}"


def test_10():
	assert magic_me('my = dict min max .hi bye') == "my = {min(max('hi')): 'bye'}"


def test_11():
	assert magic_me('dict min max hi .bye') == "{min(max(hi)): bye}"


def test_12():
	assert magic_me('my = dict min max .hi .bye') == "my = {min(max('hi')): bye}"


def test_13():
	assert magic_me('my = dict min max .hi .bye lol str what') == "my = {min(max('hi')): bye, 'lol': str(what)}"


def test_14():
	assert magic_me(
		'my = dict min max .hi .bye lol str what boo') == "my = {min(max('hi')): bye, 'lol': str(what)} boo"


def test_15():
	assert magic_me(
		'my = dict min max .hi .bye lol str what zip boo') == "my = {min(max('hi')): bye, 'lol': str(what)} boo"


def test_16():
	assert magic_me(
		'my = dict min max .hi .bye lol str what zip .boo') == "my = {min(max('hi')): bye, 'lol': str(what)} boo"


def test_17():
	assert magic_me('dict hi') == "dict(hi)"


def test_18():
	assert magic_me('dict str zip hi') == "dict(str(zip(hi)))"


def test_19():
	assert magic_me('my = dict hi') == "my = dict(hi)"


def test_20():
	assert magic_me('dict .hi') == "dict('hi')"


def test_21():
	assert magic_me('my = dict .hi') == "my = dict('hi')"


def test_22():
	assert magic_me('dict 1 self.bye') == "{1: self.bye}"


def test_23():
	assert magic_me('dict 1 str zip self.bye') == "{1: str(zip(self.bye))}"


def test_24():
	assert magic_me('dict .1 bye') == "{'1': 'bye'}"


def test_25():
	assert magic_me('dict hi self.bye') == "{'hi': self.bye}"
