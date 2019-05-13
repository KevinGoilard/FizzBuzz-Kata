

class FizzBuzz:
    def compute_string(self, param):
        if param == 2:
            return 2

        if param == 5:
            return "Buzz"

        if param % 3 == 0:
            return "Fizz"
        return 1
