import unittest
from pfpy import Function, Predicate, rpartial, curry, rcurry

class CurryTestCase(unittest.TestCase):
    def setUp(self):
        self.f = lambda a, b, c, d: (a, b, c, d)
        self.g = lambda a, b: a > b

    def test_rpartial(self):
        f = self.f
        self.assertEqual(rpartial(f)(1, 2, 3, 4), f(1, 2, 3, 4))
        self.assertEqual(rpartial(f, 4)(1, 2, 3), f(1, 2, 3, 4))
        self.assertEqual(rpartial(f, 3, 4)(1, 2), f(1, 2, 3, 4))
        self.assertEqual(rpartial(f, 2, 3, 4)(1), f(1, 2, 3, 4))
        self.assertEqual(rpartial(f, 1, 2, 3, 4)(), f(1, 2, 3, 4))

    def test_curry_unary(self):
        f = curry(4)(self.f)
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
        g = curry(2, Predicate)(self.g)

        g1 = g(1)
        g2 = g1(2)

        self.assertIs(type(g), Function)
        self.assertIs(type(g1), Predicate)
        self.assertFalse(g2)

    def test_rcurry_unary(self):
        f = rcurry(4)(self.f)
        f1 = f(1)
        f2 = f1(2)
        f3 = f2(3)
        f4 = f3(4)

        self.assertIs(type(f), Function)
        self.assertIs(type(f1), Function)
        self.assertIs(type(f2), Function)
        self.assertIs(type(f3), Function)
        self.assertEqual(f4, (4, 3, 2, 1))

    def test_rcurry_predicate(self):
        g = rcurry(2, Predicate)(self.g)

        g1 = g(1)
        g2 = g1(2)

        self.assertIs(type(g), Function)
        self.assertIs(type(g1), Predicate)
        self.assertTrue(g2)
