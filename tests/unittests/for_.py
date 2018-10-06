import unittest
from tests.unittests import get_expression, tri_quote


class TestFor(unittest.TestCase):
    def test_0(self):
        actual = get_expression('for collections')
        self.assertEqual(actual, 'for collection in collections:\n    ')

    def test_1(self):
        actual = get_expression('for collection')
        self.assertEqual(actual, 'for c in collection:\n    ')

    def test_2(self):
        actual = get_expression('for dict min max collection')
        self.assertEqual(actual, 'for c in dict(min(max(collection))):\n    ')

    def test_3(self):
        actual = get_expression('for dict min max collections')
        self.assertEqual(actual,
                         'for collection in dict(min(max(collections))):\n    ')

    def test_4(self):
        actual = get_expression('my = for collection')
        self.assertEqual(actual, 'my = for collection')

    def test_5(self):
        actual = get_expression('my = for dict min max collection')
        self.assertEqual(actual, 'my = for dict min max collection')

    def test_6(self):
        actual = get_expression('for .collection')
        self.assertEqual(actual, "for c in 'collection':\n    ")

    def test_7(self):
        actual = get_expression('for .collections')
        self.assertEqual(actual, "for collection in 'collections':\n    ")

    def test_8(self):
        actual = get_expression('for dict min max .collection')
        self.assertEqual(actual, "for c in dict(min(max('collection'))):\n    ")

    def test_9(self):
        actual = get_expression('for dict min max .collections')
        self.assertEqual(actual,
                         "for collection in dict(min(max('collections'))):\n    ")

    def test_10(self):
        actual = get_expression('for self.collection')
        self.assertEqual(actual, "for c in self.collection:\n    ")

    def test_11(self):
        actual = get_expression('for self.collections')
        self.assertEqual(actual, "for collection in self.collections:\n    ")

    def test_12(self):
        actual = get_expression('for dict min max self.collections')
        self.assertEqual(actual, 'for collection in dict(min(max(self.collections))):\n    ')

    def test_13(self):
        actual = get_expression('for args')
        self.assertEqual(actual, 'for arg in args:\n    ')

    def test_14(self):
        actual = get_expression('for 5')
        self.assertEqual(actual, 'for i in range(5):\n    ')

    def test_15(self):
        actual = get_expression('for enumerate things')
        self.assertEqual(actual, 'for i, thing in enumerate(things):\n    ')

    def test_16(self):
        actual = get_expression('for enumerate ireland')
        self.assertEqual(actual, 'for i, item in enumerate(ireland):\n    ')

    def test_17(self):
        actual = get_expression('for enumerate self.things')
        self.assertEqual(actual, 'for i, thing in enumerate(self.things):\n    ')