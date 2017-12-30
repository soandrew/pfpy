import unittest
from random import randint, sample
from math import factorial, exp, sqrt
from pfpy import Function, identity, constant

class FunctionTestCase(unittest.TestCase):
    def setUp(self):
        # Scalars
        self.x = randint(-10000, 10000)
        self.c = randint(-10000, 10000)
        self.d = randint(-10000, 10000)

        # Function
        self.f = Function(lambda x: x + 6)

        # Regular function
        self.g = (lambda x: 2 * x)

    def test_positive_and_negative(self):
        f, x = self.f, self.x

        self.assertEqual((+f)(x), +f(x))
        self.assertEqual((-f)(x), -f(x))

    def test_add(self):
        f, g, x = self.f, self.g, self.x

        self.assertEqual((f + g)(x), f(x) + g(x))
        self.assertEqual((g + f)(x), g(x) + f(x))

    def test_subtract(self):
        f, g, x = self.f, self.g, self.x

        self.assertEqual((f - g)(x), f(x) - g(x))
        self.assertEqual((g - f)(x), g(x) - f(x))

    def test_multiply(self):
        f, g, x, c = self.f, self.g, self.x, self.c

        self.assertEqual((c * f)(x) , c * f(x))
        self.assertEqual((f * g)(x) , f(x) * g(x))
        self.assertEqual((g * f)(x) , g(x) * f(x))

    def test_divide(self):
        f, g, x = self.f, self.g, self.x

        self.assertEqual((f // g)(x), f(x) // g(x))
        self.assertEqual((g // f)(x), g(x) // f(x))
        self.assertEqual((f / g)(x) , f(x) / g(x))
        self.assertEqual((g / f)(x) , g(x) / f(x))

    def test_power(self):
        f, x, c = self.f, self.x, self.c

        self.assertEqual((f ** c)(x), f(x) ** c)

    def test_composition(self):
        f, g, x = self.f, self.g, self.x

        self.assertEqual((f @ g)(x), f(g(x)))
        self.assertEqual((g >> f)(x), f(g(x)))

        self.assertEqual((g @ f)(x), g(f(x)))
        self.assertEqual((f >> g)(x), g(f(x)))

    def test_application(self):
        f, x = self.f, self.x

        self.assertEqual(x >> f, f(x))

    def test_identity_and_constant(self):
        x = self.x

        self.assertEqual(identity(x), x)
        self.assertIs(type(identity), Function)

    def test_constant(self):
        c, d = self.c, self.d

        self.assertEqual(constant(c)(d), c)
        self.assertIs(type(constant(c)), Function)

    def test_vector_space(self):
        f, g, x, c, d = self.f, Function(self.g), self.x, self.c, self.d

        h = Function(lambda x: x ** 2)
        zero = Function(lambda x: 0)

        self.assertIs(type(f + g), Function)                        # Additive closure
        self.assertIs(type(c * f), Function)                        # Scalar closure
        self.assertEqual((f + g)(x), (g + f)(x))                    # Commutative
        self.assertEqual((f + (g + h))(x), ((f + g) + h)(x))        # Additive associativity
        self.assertEqual((f + zero)(x), f(x))                       # Additive identity (Zero vector)
        self.assertEqual((f + (-f))(x), zero(x))                    # Additive inverse
        self.assertEqual((c * (d * f))(x), ((c * d) * f)(x))        # Scalar associativity
        self.assertEqual((c * (f + g))(x), ((c * f) + (c * g))(x))  # Additive distributivity
        self.assertEqual(((c + d) * f)(x), ((c * f) + (d * f))(x))  # Scalar distributivity
        self.assertEqual((1 * f)(x), f(x))                          # Scalar identity (One)

    def test_sum(self):
        series = ((1 / factorial(n)) * (identity ** n) for n in range(25))
        my_exp = sum(series)
        self.assertAlmostEqual(my_exp(5), exp(5))

    def test_mapping(self):
        f, g = self.f, self.g
        data = sample(range(-10000, 10000), 50)

        self.assertEqual(list(map(f >> g >> abs >> sqrt, data)),
                         [sqrt(abs(g(f(x)))) for x in data])
