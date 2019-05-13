import unittest

from src import FizzBuzz


class FizzBuzzTests(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_one_return_one(self):
        result = FizzBuzz.get_representation_for(1)

        expected = 1
        self.assertEqual(expected, result)

    def test_two_return_two(self):
        result = FizzBuzz.get_representation_for(2)

        expected = 2
        self.assertEqual(expected, result)

    def test_three_return_Fizz(self):
        result = FizzBuzz.get_representation_for(3)

        expected = FizzBuzz.FIZZ
        self.assertEqual(expected, result)

    def test_six_return_Fizz(self):
        result = FizzBuzz.get_representation_for(6)

        expected = FizzBuzz.FIZZ
        self.assertEqual(expected, result)

    def test_five_return_Buzz(self):
        result = FizzBuzz.get_representation_for(5)

        expected = FizzBuzz.BUZZ
        self.assertEqual(expected, result)

    def test_ten_return_Buzz(self):
        result = FizzBuzz.get_representation_for(10)

        expected = FizzBuzz.BUZZ
        self.assertEqual(expected, result)

    def test_fifteen_return_FizzBuzz(self):
        result = FizzBuzz.get_representation_for(15)

        expected = FizzBuzz.FIZZ_BUZZ
        self.assertEqual(expected, result)

    def test_thirty_return_FizzBuzz(self):
        result = FizzBuzz.get_representation_for(30)

        expected = FizzBuzz.FIZZ_BUZZ
        self.assertEqual(expected, result)

    def test_number_with_a_three_return_Fizz(self):
        result = FizzBuzz.get_representation_for(13)

        expected = FizzBuzz.FIZZ
        self.assertEqual(expected, result)

    def test_number_with_a_three_return_Fizz_bis(self):
        result = FizzBuzz.get_representation_for(23)

        expected = FizzBuzz.FIZZ
        self.assertEqual(expected, result)
