from main import magic_me


def test_0():
	assert magic_me('print hi') == "print('hi')"


def test_1():
	assert magic_me('print .hi') == "print(hi)"


def test_1_33():
	assert magic_me('print str hi') == "print(str(hi))"


def test_1_66():
	assert magic_me('print str .hi') == "print(str('hi'))"


def test_2():
	assert magic_me('print hi bye') == "print('hi bye')"


def test_3():
	assert magic_me('print hi .bye') == "print(f'hi {bye}')"


def test_4():
	assert magic_me('print hi str bye') == "print(f'hi {str(bye)}')"


def test_5():
	assert magic_me('print .hi str bye') == "print(f'{hi} {str(bye)}')"


def test_6():
	assert magic_me('print .hi str .bye') == "print(f'{hi} {str(\"bye\")}')"


#
def test_7():
	assert magic_me('print self.hi') == "print(self.hi)"


def test_8():
	assert magic_me('print hi str self.bye') == "print(f'hi {str(self.bye)}')"


def test_9():
	assert magic_me('print hi self.bye') == "print(f'hi {self.bye}')"


"""SPECIFIC HOTKEY TESTS"""
