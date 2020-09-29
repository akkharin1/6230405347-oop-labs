class Numbers:
    def __init__(self, x, y):
        self.x = x
        self.y = y


    def add(self):
        a = self.x + self.y
        return a

    def display(self):
        print(f"{self.x} {self.y}")

    @classmethod
    def get_factor(cls,x):
        cls.x = x

    @classmethod
    def display_factor(cls,x):
        if x % 2 == 0:
            lol = x / 2
            return (f"Factor of {x} is {lol} and {lol}")
        elif x % 2 > 0:
            ei = (x / 2) + 0.5
            ei2 = (x / 2) - 0.5
            return (f"Factor of {x} is {ei} and {ei2}")

    @staticmethod
    def is_valid_divisor(y):
        if y > 0:
            return ("{} is a valid divisor".format(y))
        elif y == 0:
            return ("{} is not a valid divisor".format(y))


if __name__ == "__main__":
    print(f'3 + 5 is {Numbers(3, 5).add()}')
    print(Numbers.display_factor(6))
    print(Numbers.display_factor(7))
    print(Numbers.is_valid_divisor(2))
    print(Numbers.is_valid_divisor(0))
    Numbers(3,5).display()