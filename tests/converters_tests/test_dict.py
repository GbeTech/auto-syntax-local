from . import get_expression


def test_0():
	assert get_expression('dict hi bye') == "{'hi': 'bye'}"


def test_1():
	assert get_expression('dict hi .bye') == "{'hi': bye}"


def test_3():
	assert get_expression('my = dict hi bye') == "my = {'hi': 'bye'}"


def test_4():
	assert get_expression('my = dict hi .bye') == "my = {'hi': bye}"


def test_5():
	assert get_expression('dict hi bye lol') == "{'hi': 'bye'} lol"


def test_6():
	assert get_expression('dict hi bye .lol') == "{'hi': 'bye'} lol"


def test_7():
	assert get_expression('my = dict hi bye lol') == "my = {'hi': 'bye'} lol"


def test_8():
	assert get_expression('dict min max hi bye') == "{min(max(hi)): 'bye'}"


def test_9():
	assert get_expression('dict min max .hi bye') == "{min(max('hi')): 'bye'}"


def test_10():
	assert get_expression('my = dict min max .hi bye') == "my = {min(max('hi')): 'bye'}"


def test_11():
	assert get_expression('dict min max hi .bye') == "{min(max(hi)): bye}"


def test_12():
	assert get_expression('my = dict min max .hi .bye') == "my = {min(max('hi')): bye}"


def test_13():
	assert get_expression('my = dict min max .hi .bye lol str what') == "my = {min(max('hi')): bye, 'lol': str(what)}"


def test_14():
	assert get_expression(
		'my = dict min max .hi .bye lol str what boo') == "my = {min(max('hi')): bye, 'lol': str(what)} boo"


def test_15():
	assert get_expression(
		'my = dict min max .hi .bye lol str what zip boo') == "my = {min(max('hi')): bye, 'lol': str(what)} boo"


def test_16():
	assert get_expression(
		'my = dict min max .hi .bye lol str what zip .boo') == "my = {min(max('hi')): bye, 'lol': str(what)} boo"


def test_17():
	assert get_expression('dict hi') == "dict(hi)"


def test_18():
	assert get_expression('dict str zip hi') == "dict(str(zip(hi)))"


def test_19():
	assert get_expression('my = dict hi') == "my = dict(hi)"


def test_20():
	assert get_expression('dict .hi') == "dict('hi')"


def test_21():
	assert get_expression('my = dict .hi') == "my = dict('hi')"


def test_22():
	assert get_expression('dict 1 self.bye') == "{1: self.bye}"


def test_23():
	assert get_expression('dict 1 str zip self.bye') == "{1: str(zip(self.bye))}"


def test_24():
	assert get_expression('dict .1 bye') == "{'1': 'bye'}"


def test_25():
	assert get_expression('dict hi self.bye') == "{'hi': self.bye}"


def test_0():
	assert get_expression('dict hi bye') == "{'hi': 'bye'}"


def test_01():
	assert get_expression('{} hi .bye') == "{'hi': bye}"


def test_03():
	assert get_expression('my = {} hi bye') == "my = {'hi': 'bye'}"


def test_04():
	assert get_expression('my = {} hi .bye') == "my = {'hi': bye}"


def test_05():
	assert get_expression('{} hi bye lol') == "{'hi': 'bye'} lol"


def test_06():
	assert get_expression('{} hi bye .lol') == "{'hi': 'bye'} lol"


def test_07():
	assert get_expression('my = {} hi bye lol') == "my = {'hi': 'bye'} lol"


def test_08():
	assert get_expression('{} min max hi bye') == "{min(max(hi)): 'bye'}"


def test_09():
	assert get_expression('{} min max .hi bye') == "{min(max('hi')): 'bye'}"


def test_010():
	assert get_expression('my = {} min max .hi bye') == "my = {min(max('hi')): 'bye'}"


def test_011():
	assert get_expression('{} min max hi .bye') == "{min(max(hi)): bye}"


def test_012():
	assert get_expression('my = {} min max .hi .bye') == "my = {min(max('hi')): bye}"


def test_013():
	assert get_expression('my = {} min max .hi .bye lol str what') == "my = {min(max('hi')): bye, 'lol': str(what)}"


def test_014():
	assert get_expression(
		'my = {} min max .hi .bye lol str what boo') == "my = {min(max('hi')): bye, 'lol': str(what)} boo"


def test_015():
	assert get_expression(
		'my = {} min max .hi .bye lol str what zip boo') == "my = {min(max('hi')): bye, 'lol': str(what)} boo"


def test_016():
	assert get_expression(
		'my = {} min max .hi .bye lol str what zip .boo') == "my = {min(max('hi')): bye, 'lol': str(what)} boo"


def test_017():
	assert get_expression('{} hi') == "dict(hi)"


def test_018():
	assert get_expression('{} str zip hi') == "dict(str(zip(hi)))"


def test_019():
	assert get_expression('my = {} hi') == "my = dict(hi)"


def test_020():
	assert get_expression('{} .hi') == "dict('hi')"


def test_021():
	assert get_expression('my = {} .hi') == "my = dict('hi')"


def test_022():
	assert get_expression('{} 1 self.bye') == "{1: self.bye}"


def test_023():
	assert get_expression('{} 1 str zip self.bye') == "{1: str(zip(self.bye))}"


def test_024():
	assert get_expression('{} .1 bye') == "{'1': 'bye'}"


def test_025():
	assert get_expression('{} hi self.bye') == "{'hi': self.bye}"
