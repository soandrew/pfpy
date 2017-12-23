import unittest
from random import randint
from pfpy import *

class FunctionTestCase(unittest.TestCase):
    def setUp(self):
        # Scalars
        self.x = randint(-10000, 10000)
        self.c = randint(-10000, 10000)
        self.d = randint(-10000, 10000)

        # Function
        @unary
        def f(x): return x + 6

        # Regular function
        def g(x): return 2 * x

        @unary
        def h(x): return x ** 2

        self.f, self.g, self.h = f, g, h

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

    def test_zero_and_identity(self):
        x = self.x

        self.assertEqual(Z(x), 0)
        self.assertEqual(I(x), x)

    def test_vector_space(self):
        f, g, h, x, c, d = self.f, Function(self.g), self.h, self.x, self.c, self.d

        self.assertIs(type(f + g), Function)                        # Additive closure
        self.assertIs(type(c * f), Function)                        # Scalar closure
        self.assertEqual((f + g)(x), (g + f)(x))                    # Commutative
        self.assertEqual((f + (g + h))(x), ((f + g) + h)(x))        # Additive associativity
        self.assertEqual((f + Z)(x), f(x))                          # Additive identity (Zero vector)
        self.assertEqual((f + (-f))(x), Z(x))                       # Additive inverse
        self.assertEqual((c * (d * f))(x), ((c * d) * f)(x))        # Scalar associativity
        self.assertEqual((c * (f + g))(x), ((c * f) + (c * g))(x))  # Additive distributivity
        self.assertEqual(((c + d) * f)(x), ((c * f) + (d * f))(x))  # Scalar distributivity
        self.assertEqual((1 * f)(x), f(x))                          # Scalar identity (One)

if __name__ == '__main__':
    unittest.main(verbosity=2)
