import unittest
from random import sample
from pfpy import Predicate

class PredicateTestCase(unittest.TestCase):
    def setUp(self):
        # List to filter through
        self.data = sample(range(-10000, 10000), 50)

        # Predicates
        self.is_positive = Predicate(lambda x: x > 0)

        # Regular function
        self.is_even = (lambda x: x % 2 == 0)

    def test_invert(self):
        data, is_positive = self.data, self.is_positive

        self.assertEqual(list(filter(~is_positive, data)),
                         [x for x in data if not is_positive(x)])

    def test_and(self):
        data, is_positive, is_even = self.data, self.is_positive, self.is_even

        self.assertEqual(list(filter(is_positive & is_even, data)),
                         [x for x in data if is_positive(x) and is_even(x)])

    def test_or(self):
        data, is_positive, is_even = self.data, self.is_positive, self.is_even

        self.assertEqual(list(filter(is_positive | is_even, data)),
                         [x for x in data if is_positive(x) or is_even(x)])
