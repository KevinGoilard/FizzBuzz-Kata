
class FizzBuzz:
    BUZZ = "Buzz"
    FIZZ_BUZZ = "FizzBuzz"
    FIZZ = "Fizz"

    @classmethod
    def get_representation_for(cls, number):
        if number % 3 == 0 and number % 5 == 0:
            return cls.FIZZ_BUZZ

        if number % 5 == 0:
            return cls.BUZZ

        if number % 3 == 0 or str(number).__contains__("3"):
            return cls.FIZZ

        return number
