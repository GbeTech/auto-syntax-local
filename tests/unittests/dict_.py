import unittest
from tests.unittests import get_expression, tri_quote


class TestDict(unittest.TestCase):
    def test_0(self):
        self.assertEqual(get_expression('dict hi bye'), "{'hi': 'bye'}")

    def test_1(self):
        self.assertEqual(get_expression('dict hi .bye'), "{'hi': bye}")

    def test_3(self):
        self.assertEqual(get_expression('my = dict hi bye'), "my = {'hi': 'bye'}")

    def test_4(self):
        self.assertEqual(get_expression('my = dict hi .bye'), "my = {'hi': bye}")

    def test_5(self):
        self.assertEqual(get_expression('dict hi bye lol'), "{'hi': 'bye'} lol")

    def test_6(self):
        self.assertEqual(get_expression('dict hi bye .lol'), "{'hi': 'bye'} lol")

    def test_7(self):
        self.assertEqual(get_expression('my = dict hi bye lol'), "my = {'hi': 'bye'} lol")

    def test_8(self):
        self.assertEqual(get_expression('dict min max hi bye'), "{min(max(hi)): 'bye'}")

    def test_9(self):
        self.assertEqual(get_expression('dict min max .hi bye'), "{min(max('hi')): 'bye'}")

    def test_10(self):
        self.assertEqual(get_expression('my = dict min max .hi bye'), "my = {min(max('hi')): 'bye'}")

    def test_11(self):
        self.assertEqual(get_expression('dict min max hi .bye'), "{min(max(hi)): bye}")

    def test_12(self):
        self.assertEqual(get_expression('my = dict min max .hi .bye'), "my = {min(max('hi')): bye}")

    def test_13(self):
        self.assertEqual(get_expression('my = dict min max .hi .bye lol str what'),
                         "my = {min(max('hi')): bye, 'lol': str(what)}")

    def test_14(self):
        self.assertEqual(get_expression('my = dict min max .hi .bye lol str what boo'),
                         "my = {min(max('hi')): bye, 'lol': str(what)} boo")

    def test_15(self):
        self.assertEqual(get_expression('my = dict min max .hi .bye lol str what zip boo'),
                         "my = {min(max('hi')): bye, 'lol': str(what)} boo")

    def test_16(self):
        self.assertEqual(get_expression('my = dict min max .hi .bye lol str what zip .boo'),
                         "my = {min(max('hi')): bye, 'lol': str(what)} boo")

    def test_17(self):
        self.assertEqual(get_expression('dict hi'), "dict(hi)")

    def test_18(self):
        self.assertEqual(get_expression('dict str zip hi'), "dict(str(zip(hi)))")

    def test_19(self):
        self.assertEqual(get_expression('my = dict hi'), "my = dict(hi)")

    def test_20(self):
        self.assertEqual(get_expression('dict .hi'), "dict('hi')")

    def test_21(self):
        self.assertEqual(get_expression('my = dict .hi'), "my = dict('hi')")

    def test_22(self):
        self.assertEqual(get_expression('dict 1 self.bye'), "{1: self.bye}")

    def test_23(self):
        self.assertEqual(get_expression('dict 1 str zip self.bye'), "{1: str(zip(self.bye))}")

    def test_24(self):
        self.assertEqual(get_expression('dict .1 bye'), "{'1': 'bye'}")

    def test_25(self):
        self.assertEqual(get_expression('dict hi self.bye'), "{'hi': self.bye}")

    def test_00(self):
        self.assertEqual(get_expression('dict hi bye'), "{'hi': 'bye'}")

    def test_01(self):
        self.assertEqual(get_expression('{} hi .bye'), "{'hi': bye}")

    def test_03(self):
        self.assertEqual(get_expression('my = {} hi bye'), "my = {'hi': 'bye'}")

    def test_04(self):
        self.assertEqual(get_expression('my = {} hi .bye'), "my = {'hi': bye}")

    def test_05(self):
        self.assertEqual(get_expression('{} hi bye lol'), "{'hi': 'bye'} lol")

    def test_06(self):
        self.assertEqual(get_expression('{} hi bye .lol'), "{'hi': 'bye'} lol")

    def test_07(self):
        self.assertEqual(get_expression('my = {} hi bye lol'), "my = {'hi': 'bye'} lol")

    def test_08(self):
        self.assertEqual(get_expression('{} min max hi bye'), "{min(max(hi)): 'bye'}")

    def test_09(self):
        self.assertEqual(get_expression('{} min max .hi bye'), "{min(max('hi')): 'bye'}")

    def test_010(self):
        self.assertEqual(get_expression('my = {} min max .hi bye'), "my = {min(max('hi')): 'bye'}")

    def test_011(self):
        self.assertEqual(get_expression('{} min max hi .bye'), "{min(max(hi)): bye}")

    def test_012(self):
        self.assertEqual(get_expression('my = {} min max .hi .bye'), "my = {min(max('hi')): bye}")

    def test_013(self):
        self.assertEqual(get_expression('my = {} min max .hi .bye lol str what'),
                         "my = {min(max('hi')): bye, 'lol': str(what)}")

    def test_014(self):
        self.assertEqual(get_expression('my = {} min max .hi .bye lol str what boo'),
                         "my = {min(max('hi')): bye, 'lol': str(what)} boo")

    def test_015(self):
        self.assertEqual(get_expression('my = {} min max .hi .bye lol str what zip boo'),
                         "my = {min(max('hi')): bye, 'lol': str(what)} boo")

    def test_016(self):
        self.assertEqual(get_expression('my = {} min max .hi .bye lol str what zip .boo'),
                         "my = {min(max('hi')): bye, 'lol': str(what)} boo")

    def test_017(self):
        self.assertEqual(get_expression('{} hi'), "dict(hi)")

    def test_018(self):
        self.assertEqual(get_expression('{} str zip hi'), "dict(str(zip(hi)))")

    def test_019(self):
        self.assertEqual(get_expression('my = {} hi'), "my = dict(hi)")

    def test_020(self):
        self.assertEqual(get_expression('{} .hi'), "dict('hi')")

    def test_021(self):
        self.assertEqual(get_expression('my = {} .hi'), "my = dict('hi')")

    def test_022(self):
        self.assertEqual(get_expression('{} 1 self.bye'), "{1: self.bye}")

    def test_023(self):
        self.assertEqual(get_expression('{} 1 str zip self.bye'), "{1: str(zip(self.bye))}")

    def test_024(self):
        self.assertEqual(get_expression('{} .1 bye'), "{'1': 'bye'}")

    def test_025(self):
        self.assertEqual(get_expression('{} hi self.bye'), "{'hi': self.bye}")