import unittest

from src import FizzBuzz


class FizzBuzzTests(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_one_print_one(self):
        fizz_buzz:FizzBuzz = FizzBuzz()

        result = fizz_buzz.compute_string(1)

        expected = 1
        self.assertEqual(result, expected)

    def test_three_return_Fizz(self):
        fizz_buzz = FizzBuzz()

        result = fizz_buzz.compute_string(3)

        expected = "Fizz"
        self.assertEqual(result, expected)
