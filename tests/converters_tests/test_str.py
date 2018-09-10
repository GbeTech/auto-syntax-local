from . import get_expression


def test_0():
    assert get_expression(f"str hi") == "'hi'"


def test_1():
    assert get_expression(f"my = str hi") == "my = 'hi'"


def test_2():
    assert get_expression(f"str hi .bye") == "f'hi {bye}'"


def test_3():
    assert get_expression(f"my = str hi .bye") == "my = f'hi {bye}'"


def test_4():
    assert get_expression(f"my = str hi 1") == "my = 'hi 1'"


def test_5():
    assert get_expression(f"my = str .hi 1") == "my = f'{hi} 1'"


def test_6():
    assert get_expression(f"my = str self.hi") == "my = f'{self.hi}'"


def test_00():
    assert get_expression(f"' hi") == "'hi'"


def test_01():
    assert get_expression(f"my = ' hi") == "my = 'hi'"


def test_02():
    assert get_expression(f"' hi .bye") == "f'hi {bye}'"


def test_03():
    assert get_expression(f"my = ' hi .bye") == "my = f'hi {bye}'"


def test_04():
    assert get_expression(f"my = ' hi 1") == "my = 'hi 1'"


def test_05():
    assert get_expression(f"my = ' .hi 1") == "my = f'{hi} 1'"


def test_06():
    assert get_expression(f"my = ' self.hi") == "my = f'{self.hi}'"


def test_000():
    assert get_expression(f'" hi') == '"hi"'


def test_001():
    assert get_expression(f'my = " hi') == 'my = "hi"'


def test_002():
    assert get_expression(f'" hi .bye') == 'f"hi {bye}"'


def test_003():
    assert get_expression(f'my = " hi .bye') == 'my = f"hi {bye}"'


def test_004():
    assert get_expression(f'my = " hi 1') == 'my = "hi 1"'


def test_005():
    assert get_expression(f'my = " .hi 1') == 'my = f"{hi} 1"'


def test_006():
    assert get_expression(f'my = " self.hi') == 'my = f"{self.hi}"'