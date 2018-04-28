from main import magic_me


def test_0():
	assert magic_me('for collections') == 'for collection in collections:\n\t'


def test_1():
	assert magic_me('for collection') == 'for c in collection:\n\t'


def test_2():
	assert magic_me('for dict min max collection') == 'for c in dict(min(max(collection))):\n\t'


def test_3():
	assert magic_me('for dict min max collections') == 'for collection in dict(min(max(collections))):\n\t'


def test_4():
	assert magic_me('my = for collection') == 'my = for collection'


def test_5():
	assert magic_me('my = for dict min max collection') == 'my = for dict min max collection'


def test_6():
	assert magic_me('for .collection') == "for c in 'collection':\n\t"


def test_7():
	assert magic_me('for .collections') == "for collection in 'collections':\n\t"


def test_8():
	assert magic_me('for dict min max .collection') == "for c in dict(min(max('collection'))):\n\t"


def test_9():
	assert magic_me('for dict min max .collections') == "for collection in dict(min(max('collections'))):\n\t"


def test_10():
	assert magic_me('for self.collection') == "for c in self.collection:\n\t"


def test_11():
	assert magic_me('for self.collections') == "for collection in self.collections:\n\t"


def test_12():
	assert magic_me('for dict min max self.collections') == 'for collection in dict(min(max(self.collections))):\n\t'
