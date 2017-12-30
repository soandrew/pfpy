import unittest
from random import randint, sample
from pfpy import Predicate

class PredicateTestCase(unittest.TestCase):
    def setUp(self):
        # Scalars
        self.x = randint(-10000, 10000)

        # Predicates
        self.is_positive = Predicate(lambda x: x > 0)

        # Regular function
        self.is_even = (lambda x: x % 2 == 0)

    def test_invert(self):
        x, is_positive = self.x, self.is_positive

        self.assertEqual((~is_positive)(x), not is_positive(x))

    def test_and(self):
        x, is_positive, is_even = self.x, self.is_positive, self.is_even

        self.assertEqual((is_positive & is_even)(x), is_positive(x) and is_even(x))

    def test_or(self):
        x, is_positive, is_even = self.x, self.is_positive, self.is_even

        self.assertEqual((is_positive | is_even)(x), is_positive(x) or is_even(x))

    def test_composition(self):
        x, is_positive = self.x, self.is_positive

        self.assertEqual((str @ is_positive)(x), str(is_positive(x)))
        self.assertEqual((is_positive >> str)(x), str(is_positive(x)))
        
        self.assertEqual((is_positive @ abs)(x), is_positive(abs(x)))
        self.assertEqual((abs >> is_positive)(x), is_positive(abs(x)))

    def test_application(self):
        x, is_positive = self.x, self.is_positive

        self.assertEqual(x >> is_positive, is_positive(x))

    def test_filtering(self):
        is_positive, is_even = self.is_positive, self.is_even
        data = sample(range(-10000, 10000), 50)

        self.assertEqual(list(filter(~is_positive, data)),
                         [x for x in data if not is_positive(x)])
        self.assertEqual(list(filter(is_positive & is_even, data)),
                         [x for x in data if is_positive(x) and is_even(x)])
        self.assertEqual(list(filter(is_positive | is_even, data)),
                         [x for x in data if is_positive(x) or is_even(x)])
