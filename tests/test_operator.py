import unittest
from random import randint, sample
from pfpy.operator import *

class OperatorTestCase(unittest.TestCase):
    def setUp(self):
        self.a = randint(-10000, 10000)
        self.b = randint(-10000, 10000)
        self.none = None
        self.data = sample(range(0, 50), 50)
        self.x = randint(0, 50)

    def test_comparison_ops(self):
        a, b, none = self.a, self.b, self.none

        self.assertEqual(lt(a)(b), b < a)
        self.assertEqual(le(a)(b), b <= a)
        self.assertEqual(eq(a)(b), b == a)
        self.assertEqual(ne(a)(b), b != a)
        self.assertEqual(ge(a)(b), b >= a)
        self.assertEqual(gt(a)(b), b > a)
        self.assertEqual(is_(None)(none), none is None)
        self.assertEqual(is_not(None)(none), none is not None)

    def test_sequence_ops(self):
        x, data = self.x, self.data

        self.assertEqual(contains(x)(data), x in data)
        self.assertEqual(concat("world")("hello"), "hello" + "world")
        self.assertEqual(countOf(x)(data), data.count(x))
        self.assertEqual(getitem(10)(data), data[10])
        self.assertEqual(indexOf("l")("hello"), "hello".index("l"))

    def test_bitwise_ops(self):
        a, b = self.a, self.b

        self.assertEqual(and_(a)(b), b & a)
        self.assertEqual(or_(a)(b), b | a)
        self.assertEqual(xor(a)(b), b ^ a)
        self.assertEqual(lshift(5)(b), b << 5)
        self.assertEqual(rshift(5)(b), b >> 5)

    def test_arithmetic_ops(self):
        a, b = self.a, self.b

        self.assertEqual(add(a)(b), b + a)
        self.assertEqual(sub(a)(b), b - a)
        self.assertEqual(floordiv(a)(b), b // a)
        self.assertEqual(truediv(a)(b), b / a)
        self.assertEqual(mul(a)(b), b * a)
        self.assertEqual(mod(a)(b), b % a)
        self.assertEqual(pow_(a)(b), pow(b, a))
