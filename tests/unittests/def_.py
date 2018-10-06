import unittest
from src.internals import Expression
from src.internals import MAGIC_FUNCTIONS

tri_quote = '"""'


def get_expression(clp, used_keyword=None):
    is_indented = '    ' in clp or '    ' in clp
    line = Expression(clp, is_indented, used_keyword)

    if line.l_side:
        return line.l_side + ' = ' + line.r_side
    return line.r_side


class TestStringMethods(unittest.TestCase):

    def test_0(self):
        self.assertEqual(get_expression(f'def foo'), f'def foo():\n    ')

    def test_1(self):
        self.assertEqual(get_expression(f'def foo p1'),
                         f'def foo(p1):\n    ')

    def test_2(self):
        self.assertEqual(get_expression(f'def foo p1 p2'),
                         f'def foo(p1, p2):\n    ')

    def test_3(self):
        expected = f"""def foo(self, p1, p2):
    """
        self.assertEqual(get_expression('    def foo p1 p2'), expected)

    def test_3_andahalf(self):
        self.assertEqual(get_expression("""    def foo p1 p2"""),
                         f'def foo(self, p1, p2):\n    ')

    def test_4(self):
        self.assertEqual(get_expression(f'def foo p1 .None'),
                         f'def foo(p1=None):\n    ')

    def test_5(self):
        self.assertEqual(get_expression(f'def foo p1 .None p2'),
                         f'def foo(p1=None, p2):\n    ')

    def test_6_a(self):
        self.assertEqual(get_expression(f'def foo p1 .False p2'),
                         f'def foo(p1=False, p2):\n    ')

    def test_6_b(self):
        self.assertEqual(get_expression(f'def foo p1 .True p2'),
                         f'def foo(p1=True, p2):\n    ')

    def test_6_c(self):
        self.assertEqual(get_expression(f'def foo p1 .1 p2'),
                         f'def foo(p1=1, p2):\n    ')

    def test_7(self):
        expected = f"""def foo(p1):
    {tri_quote}
    :type p1: str
    {tri_quote}
    """
        self.assertEqual(get_expression(f'def foo p1 str'), expected)

    def test_8(self):
        expected = f"""def foo(p1):
    {tri_quote}
    :rtype: str
    {tri_quote}
    """
        self.assertEqual(get_expression(f'def foo str p1'), expected)

    def test_9(self):
        expected = f"""def foo(p1):
    {tri_quote}
    :type p1: str
    :rtype: str
    {tri_quote}
    """
        self.assertEqual(get_expression(f'def foo str p1 str'), expected)

    def test_10(self):
        self.assertEqual(get_expression(f'def foo p1 .default p2'),
                         "def foo(p1='default', p2):\n    ")

    def test_11(self):
        expected = f"""def foo(p1='default', p2):
    {tri_quote}
    :type p2: str
    {tri_quote}
    """
        actual = get_expression(f'def foo p1 .default p2 str')
        self.assertEqual(actual, expected)

    def test_12(self):
        self.assertEqual(get_expression(f'my = def foo p1 .default p2 str'),
                         f'my = def foo p1 .default p2 str')

    def test_13(self):
        for mag_fn in MAGIC_FUNCTIONS:
            mandatory_args = ', '.join(['self'] + MAGIC_FUNCTIONS[mag_fn])
            self.assertEqual(get_expression(f'    def {mag_fn}'), f"def __{mag_fn}__({mandatory_args}):\n    ")

    def test_14(self):
        expected = f"""def __init__(self, age):
    self.age = age
    """
        self.assertEqual(get_expression(f'    def init age'), expected)

    def test_15(self):
        expected = f"""def __init__(self, age, name='moshe'):
    {tri_quote}
    :type age: int
    {tri_quote}
    self.age = age
    self.name = name
    """
        self.assertEqual(get_expression(f'    def init age int name .moshe'), expected)

    def test_16(self):
        expected = f"""def what(p1='lol'):
    {tri_quote}
    :type p1: str
    {tri_quote}
    """
        self.assertEqual(get_expression(f"def what p1 str .lol"), expected)

    def test_17(self):
        expected = f"""def what(p1='lol'):
    {tri_quote}
    :type p1: str
    :rtype: int
    {tri_quote}
    """
        self.assertEqual(get_expression(f"def what int p1 str .lol"), expected)

    def test_18(self):
        expected = f"""def what(p1=1):
    {tri_quote}
    :type p1: str
    :rtype: int
    {tri_quote}
    """
        self.assertEqual(get_expression(f"def what int p1 str .1"), expected)

    def test_19(self):
        expected = f"""def what(*args):
    """
        self.assertEqual(get_expression(f"def what args"), expected)

    def test_20(self):
        expected = f"""def what(**kwargs):
    """
        self.assertEqual(get_expression(f"def what kwargs"), expected)

    def test_21(self):
        expected = f"""def what(*args, **kwargs):
    """
        self.assertEqual(get_expression(f"def what args kwargs"), expected)

    def test_22(self):
        expected = f"""def what(hi, *args, **kwargs):
    """
        self.assertEqual(get_expression(f"def what hi args kwargs"), expected)

    @unittest.skip("not implemented yet")
    def test_119(self):
        expected = f"""def what(p1='1'):
    {tri_quote}
    :type p1: str
    :rtype: int
    {tri_quote}
    """
        self.assertEqual(get_expression(f"def what int p1 str 1"), expected)


if __name__ == '__main__':
    unittest.main()