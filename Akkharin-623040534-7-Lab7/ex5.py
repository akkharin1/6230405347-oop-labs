import math

class Circle:

    def __init__(self, radius):
        self.radius = radius


    def circlr_aera(self):
        a = math.pi  * math.pow(self.radius,2)
        return round(a, 2)


    def perimeter(self):
        b = 2 * math.pi  * self.radius
        return round(b, 2)

number1 = 3
number2 = 4

if __name__ == '__main__':
    print(f"The circle with radius {number1} has the area as {Circle(number1).circlr_aera()} \nand the perimeter as {Circle(number1).perimeter()}")
    print(f"The circle with radius {number2} has the area as {Circle(number2).circlr_aera()} \nand the perimeter as {Circle(number2).perimeter()}")









