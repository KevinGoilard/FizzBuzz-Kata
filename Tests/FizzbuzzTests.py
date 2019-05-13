import unittest

from src import FizzBuzz


class FizzBuzzTests(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_one_print_one(self):
        fizzBuzz = FizzBuzz()

        result = fizzBuzz.ComputeString(1)

        expected = 1
        self.assertEqual(result, expected)
