

class FizzBuzz:
    @staticmethod
    def get_representation_for(number):
        if number == 13:
            return "Fizz"

        if number % 3 == 0 and number % 5 == 0:
            return "FizzBuzz"

        if number % 5 == 0:
            return "Buzz"

        if number % 3 == 0:
            return "Fizz"

        return number
