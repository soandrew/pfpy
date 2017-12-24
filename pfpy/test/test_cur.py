import unittest
from pfpy import Function, Predicate
from pfpy.cur import curry

class CurTestCase(unittest.TestCase):
    def test_curry_unary(self):
        @curry(4)
        def f(a, b, c, d):
            return (a, b, c, d)

        f1 = f(1)
        f2 = f1(2)
        f3 = f2(3)
        f4 = f3(4)

        self.assertIs(type(f), Function)
        self.assertIs(type(f1), Function)
        self.assertIs(type(f2), Function)
        self.assertIs(type(f3), Function)
        self.assertEqual(f4, (1, 2, 3, 4))

    def test_curry_predicate(self):
        @curry(2, Predicate)
        def f(a, b):
            return a == b

        f1 = f(1)
        f2 = f1(2)

        self.assertIs(type(f), Function)
        self.assertIs(type(f1), Predicate)
        self.assertFalse(f2)
