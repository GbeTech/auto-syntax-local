from main import magic_me


def test_0():
	assert magic_me('list hi bye') == "['hi', 'bye']"


def test_1():
	assert magic_me('list hi .bye') == "['hi', bye]"


def test_2():
	assert magic_me('my = list hi bye') == "my = ['hi', 'bye']"


def test_3():
	assert magic_me('my = list hi .bye') == "my = ['hi', bye]"


def test_4():
	assert magic_me('list dict min max collection') == 'list(dict(min(max(collection))))'


def test_5():
	assert magic_me('list dict min max collection1 collection2') == "[dict(min(max(collection1))), 'collection2']"


def test_6():
	assert magic_me(
		'list dict min max collection1 collection2 .collection3') == "[dict(min(max(collection1))), 'collection2', " \
	                                                                 "collection3]"


def test_7():
	assert magic_me(
		'list dict min max collection1 collection2 str collection3') == "[dict(min(max(collection1))), 'collection2', " \
	                                                                    "" \
	                                                                    "" \
	                                                                    "str(collection3)]"


def test_8():
	assert magic_me('list dict .collection') == "list(dict('collection'))"


def test_9():
	assert magic_me(
		'my = list dict min max collection1 collection2 str collection3') == "my = [dict(min(max(collection1))), " \
	                                                                         "'collection2', str(collection3)]"


def test_10():
	assert magic_me('list hi') == 'list(hi)'


def test_11():
	assert magic_me('list .hi') == "list('hi')"


def test_12():
	assert magic_me('my = list hi') == "my = list(hi)"


def test_13():
	assert magic_me('my = list .hi') == "my = list('hi')"


def test_14():
	assert magic_me('list 1 2') == "[1, 2]"


def test_15():
	assert magic_me('list 1 .2') == "[1, '2']"


def test_16():
	assert magic_me('my = list 1 2') == "my = [1, 2]"


def test_17():
	assert magic_me('my = list 1 .2') == "my = [1, '2']"


def test_18():
	assert magic_me('list hi 2') == "['hi', 2]"


def test_19():
	assert magic_me('list hi .2') == "['hi', '2']"


def test_20():
	assert magic_me('list hi str 2') == "['hi', str(2)]"


def test_21():
	assert magic_me('list str .hi zip .2') == "[str('hi'), zip('2')]"


def test_22():
	assert magic_me('list hi self.bye') == "['hi', self.bye]"


def test_23():
	assert magic_me('list hi str zip self.bye') == "['hi', str(zip(self.bye))]"
