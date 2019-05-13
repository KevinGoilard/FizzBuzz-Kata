from parameterized import parameterized

import unittest

from src import FizzBuzz


class FizzBuzzTests(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    @parameterized.expand([
        (1,),
        (2,),
    ])
    def test_not_fizz_or_buzz_number_return_itself(self, value):
        result = FizzBuzz.get_representation_for(value)

        expected = value
        self.assertEqual(expected, result)

    @parameterized.expand([
        (3,),
        (6,),
    ])
    def test_multiple_of_three_return_Fizz(self, value):
        result = FizzBuzz.get_representation_for(value)

        expected = FizzBuzz.FIZZ
        self.assertEqual(expected, result)

    @parameterized.expand([
        (5,),
        (10,),
    ])
    def test_multiple_of_five_return_Buzz(self, value):
        result = FizzBuzz.get_representation_for(value)

        expected = FizzBuzz.BUZZ
        self.assertEqual(expected, result)

    @parameterized.expand([
        (15,),
        (30,),
    ])
    def test_multiple_of_five_and_three_return_FizzBuzz(self, value):
        result = FizzBuzz.get_representation_for(value)

        expected = FizzBuzz.FIZZ_BUZZ
        self.assertEqual(expected, result)

    @parameterized.expand([
        (13,),
        (23,),
    ])
    def test_number_with_a_three_return_Fizz(self, value):
        result = FizzBuzz.get_representation_for(value)

        expected = FizzBuzz.FIZZ
        self.assertEqual(expected, result)

    @parameterized.expand([
        (56,),
        (52,),
    ])
    def test_number_with_a_five_return_Buzz(self, value):
        result = FizzBuzz.get_representation_for(value)

        expected = FizzBuzz.BUZZ
        self.assertEqual(expected, result)

    def test_number_fizz_with_a_five_return_FizzBuzz(self):
        result = FizzBuzz.get_representation_for(51)

        expected = FizzBuzz.FIZZ_BUZZ
        self.assertEqual(expected, result)

    def test_number_buzz_with_a_three_return_FizzBuzz(self):
        result = FizzBuzz.get_representation_for(130)

        expected = FizzBuzz.FIZZ_BUZZ
        self.assertEqual(expected, result)
