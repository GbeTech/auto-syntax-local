from main import magic_me


def test_0():
	assert magic_me(f"str hi") == "'hi'"


def test_1():
	assert magic_me(f"my = str hi") == "my = 'hi'"


def test_2():
	assert magic_me(f"str hi .bye") == "f'hi {bye}'"


def test_3():
	assert magic_me(f"my = str hi .bye") == "my = f'hi {bye}'"


def test_4():
	assert magic_me(f"my = str hi 1") == "my = 'hi 1'"


def test_5():
	assert magic_me(f"my = str .hi 1") == "my = f'{hi} 1'"


def test_6():
	assert magic_me(f"my = str self.hi") == "my = f'{self.hi}'"
