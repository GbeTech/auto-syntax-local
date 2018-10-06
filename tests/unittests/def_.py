import unittest
from src.internals import Expression

tri_quote = '"""'


def get_expression(clp, used_keyword=None):
    is_indented = '\t' in clp or '    ' in clp
    line = Expression(clp, is_indented, used_keyword)

    if line.l_side:
        return line.l_side + ' = ' + line.r_side
    return line.r_side


class TestStringMethods(unittest.TestCase):

    def test_0(self):
        expression = get_expression('def foo')
        self.assertEqual(expression, 'def foo():\n\t')
        # assert get_expression(f'def foo') == f'def foo():\n\t'

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        string = 'hello world'
        self.assertEqual(string.split(), ['hello', 'world'])
        # check that string.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            string.split(2)


if __name__ == '__main__':
    unittest.main()