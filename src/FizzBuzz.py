
class FizzBuzz:
    BUZZ = "Buzz"
    FIZZ_BUZZ = "FizzBuzz"
    FIZZ = "Fizz"

    @classmethod
    def get_representation_for(cls, number):
        if cls.is_fizz(number) and cls.is_buzz(number):
            return cls.FIZZ_BUZZ

        if cls.is_buzz(number):
            return cls.BUZZ

        if cls.is_fizz(number):
            return cls.FIZZ

        return number

    @classmethod
    def is_fizz(cls, number):
        return number % 3 == 0 or str(number).__contains__("3")

    @classmethod
    def is_buzz(cls, number):
        return number % 5 == 0 or str(number).__contains__("5")
