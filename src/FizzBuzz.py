

class FizzBuzz:
    def compute_string(self, param):
        if param % 3 == 0 and param % 5 == 0:
            return "FizzBuzz"

        if param % 5 == 0:
            return "Buzz"

        if param % 3 == 0:
            return "Fizz"

        return param
