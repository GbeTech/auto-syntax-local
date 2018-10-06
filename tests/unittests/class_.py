import unittest
from tests.unittests import get_expression, tri_quote


class TestClass(unittest.TestCase):

    def test_0(self):
        self.assertEqual(get_expression(f'class foo'), f'class foo:\n    ')

    def test_1(self):
        self.assertEqual(get_expression(f'class foo Super'), f'class foo(Super):\n    ')

    def test_2(self):
        expected = f"""class foo:
    def __init__(self):
    """
        self.assertEqual(get_expression(f'class foo init'), expected)

    def test_3(self):
        expected = f"""class foo:
    def __init__(self, name):
        self.name = name
    """
        self.assertEqual(get_expression(f'class foo init name'), expected)

    def test_4(self):
        expected = f"""class foo:
    def __init__(self, name):
        {tri_quote}
        :type name: str
        {tri_quote}
        self.name = name
    """
        self.assertEqual(get_expression(f'class foo init name str'), expected)

    def test_5(self):
        expected = f"""class foo(Super):
    def __init__(self):
        super().__init__()
    """
        self.assertEqual(get_expression(f'class foo Super init'), expected)

    def test_6(self):
        expected = f"""class foo(Super):
    def __init__(self, name):
        self.name = name
        super().__init__()
    """
        self.assertEqual(get_expression(f'class foo Super init name'), expected)

    def test_7(self):
        expected = f"""class foo(Super):
    def __init__(self, name='moshe'):
        self.name = name
        super().__init__()
    """
        self.assertEqual(get_expression(f'class foo Super init name .moshe'), expected)

    def test_8(self):
        expected = f"""class foo(Super):
    def __init__(self, name):
        {tri_quote}
        :type name: str
        {tri_quote}
        self.name = name
        super().__init__()
    """
        self.assertEqual(get_expression(f'class foo Super init name str'), expected)

    def test_9(self):
        expected = f"""class foo(Super, Hi):
    """
        self.assertEqual(get_expression(f'class foo Super Hi'), expected)

    def test_10(self):
        expected = f"""class foo(Super, Hi):
    def __init__(self):
        super().__init__()
    """
        self.assertEqual(get_expression(f'class foo Super Hi init'), expected)

    def test_11(self):
        expected = f"""class Foo(Super, Hi):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__()
    """
        self.assertEqual(get_expression(f"class Foo Super Hi init name age"), expected)

    def test_12(self):
        expected = f"""class Foo(Super, Hi):
    def __init__(self, name):
        {tri_quote}
        :type name: str
        {tri_quote}
        self.name = name
        super().__init__()
    """
        self.assertEqual(get_expression(f"class Foo Super Hi init name str"), expected)

    def test_13(self):
        expected = f"""class Foo(Super):
    def __init__(self, *args, **kwargs):
        super().__init__()
    """
        self.assertEqual(get_expression(f"class Foo Super init args kwargs"), expected)

    def test_14(self):
        expected = f"""class Foo(Super):
    def __init__(self, *args, **kwargs):
        super().__init__()
    """
        self.assertEqual(get_expression(f"class Foo Super init *args **kwargs"), expected)

    def test_15(self):
        expected = f"""class Foo(Super):
    def __init__(self, age=3):
        self.age = age
        super().__init__()
    """
        self.assertEqual(get_expression(f"class Foo Super init age .3"), expected)