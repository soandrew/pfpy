import unittest
from random import randint, sample
from math import factorial, exp, sqrt
from pfpy import Function, identity

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
        self.assertEqual((f ^ c)(x), f(x) ** c)

    def test_composition(self):
        f, g, x = self.f, self.g, self.x

        self.assertEqual((f << g)(x), f(g(x)))
        self.assertEqual((g >> f)(x), f(g(x)))
        self.assertEqual((f @ g)(x), f(g(x)))

        self.assertEqual((f >> g)(x), g(f(x)))
        self.assertEqual((g << f)(x), g(f(x)))
        self.assertEqual((g @ f)(x), g(f(x)))

    def test_identity(self):
        x = self.x

        self.assertEqual(identity(x), x)
        self.assertIs(type(identity), Function)

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
        #series = (Function(lambda x, n=n: pow(x, n) / factorial(n)) for n in range(50))
        series = ((1 / factorial(n)) * (identity ^ n) for n in range(50))
        my_exp = sum(series)
        self.assertAlmostEqual(my_exp(5), exp(5))

    def test_pipeline(self):
        data = sample(range(-10000, 10000), 50)
        divide_by_2 = Function(lambda x: x / 2)
        add_100 = Function(lambda x: x + 100)

        self.assertEqual(list(map(divide_by_2 >> add_100 >> abs >> sqrt, data)),
                         [sqrt(abs(add_100(divide_by_2(x)))) for x in data])
