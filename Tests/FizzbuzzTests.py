import unittest

from src import FizzBuzz


class FizzBuzzTests(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_one_return_one(self):
        fizz_buzz:FizzBuzz = FizzBuzz()

        result = fizz_buzz.compute_string(1)

        expected = 1
        self.assertEqual(expected, result)

    def test_two_return_two(self):
        fizz_buzz: FizzBuzz = FizzBuzz()

        result = fizz_buzz.compute_string(2)

        expected = 2
        self.assertEqual(expected, result)

    def test_three_return_Fizz(self):
        fizz_buzz = FizzBuzz()

        result = fizz_buzz.compute_string(3)

        expected = "Fizz"
        self.assertEqual(expected, result)

    def test_six_return_Fizz(self):
        fizz_buzz = FizzBuzz()

        result = fizz_buzz.compute_string(6)

        expected = "Fizz"
        self.assertEqual(expected, result)

    def test_five_return_Buzz(self):
        fizz_buzz: FizzBuzz = FizzBuzz()

        result = fizz_buzz.compute_string(5)

        expected = "Buzz"
        self.assertEqual(expected, result)
