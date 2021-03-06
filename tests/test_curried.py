import unittest
from random import randint, sample
from pfpy.curried import *
import functools
import operator
import itertools

class CurriedTestCase(unittest.TestCase):
    def setUp(self):
        self.a = randint(-10000, 10000)
        self.b = randint(-10000, 10000)
        self.none = None
        self.data = sample(range(-50, 50), 100)
        self.x = randint(0, 50)
        self.is_even = (lambda x: x % 2 == 0)
        self.times2 = (lambda x: 2 * x)

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
        self.assertEqual(pow(a)(b), __builtins__["pow"](b, a))


    def test_class_ops(self):
        class Point():
            x = 1
            y = 2

        self.assertEqual(getattr("x")(Point), __builtins__["getattr"](Point, "x"))

    def test_itertools(self):
        data, is_even, times2 = self.data, self.is_even, self.times2

        self.assertEqual((list @ map(times2))(data), list(__builtins__["map"](times2, data)))
        self.assertEqual((list @ filter(is_even))(data), list(__builtins__["filter"](is_even, data)))
        self.assertEqual([(key, list(group)) for key, group in groupby(abs)(data)],
                         [(key, list(group)) for key, group in itertools.groupby(data, key=abs)])

    def test_functools(self):
        data = self.data
        
        self.assertEqual(apply(operator.add)(data[0:2]), operator.add(*data[0:2]))
        self.assertEqual(reduce(operator.mul)(data), functools.reduce(operator.mul, data))
        self.assertEqual(sorted(abs)(data), __builtins__["sorted"](data, key=abs))
        self.assertEqual(max(abs)(data), __builtins__["max"](data, key=abs))
        self.assertEqual(min(abs)(data), __builtins__["min"](data, key=abs))
