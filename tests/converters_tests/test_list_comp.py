from main import magic_me


def test_0():
	assert magic_me('lcomp collection') == "[c for c in collection]"


def test_1():
	assert magic_me('my = lcomp collection') == "my = [c for c in collection]"


def test_2():
	assert magic_me('lcomp collections') == "[collection for collection in collections]"


def test_3():
	assert magic_me('my = lcomp collections') == "my = [collection for collection in collections]"


def test_4():
	assert magic_me('lcomp .collection') == "[c for c in 'collection']"


def test_5():
	assert magic_me('my = lcomp .collection') == "my = [c for c in 'collection']"


def test_6():
	assert magic_me('lcomp .collections') == "[collection for collection in 'collections']"


def test_7():
	assert magic_me('my = lcomp .collections') == "my = [collection for collection in 'collections']"


def test_8():
	assert magic_me('lcomp str zip dict collection') == "[str(zip(dict(c))) for c in collection]"


def test_9():
	assert magic_me('lcomp str zip dict .collection') == "[str(zip(dict(c))) for c in 'collection']"


def test_10():
	assert magic_me('lcomp str zip dict .collection') == "[str(zip(dict(c))) for c in 'collection']"


def test_11():
	assert magic_me('lcomp str zip dict self.collection') == "[str(zip(dict(c))) for c in self.collection]"


def test_12():
	assert magic_me(
		'lcomp str zip dict self.collections') == "[str(zip(dict(collection))) for collection in self.collections]"


def test_13():
	assert magic_me('lcomp self.collections') == "[collection for collection in self.collections]"
