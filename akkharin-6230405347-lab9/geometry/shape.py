from abc import abstractmethod
import random

class Shape:
    def __init__(self, colors):
        self.colors = colors

    @abstractmethod
    def draw(self):
        pass

class Circle(Shape):
    num = 0
    def __init__(self, colors, radius):
        self.radius = radius
        Circle.num += 1
        super(Circle, self).__init__(colors)

    def set_radius(self, radius):
        self.radius = radius

    @classmethod
    def get_num_circles(cls):
        return cls.num

    def draw(self):
        print("Drawing a circle with radius", self.radius)

class Rectangle(Shape):
    num = 0
    def __init__(self, colors, width, height):
        self.width = width
        self.height = height
        Rectangle.num += 1
        super(Rectangle, self).__init__(colors)

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def print_area(self):
        print(f"Rectangle width {self.width} height {self.height} has area as {self.width * self.height}")

    def draw(self):
        print(f"Drawing a rectangle with width {self.width} hieght {self.height}")

    @classmethod
    def get_num_rectangle(cls):
        return cls.num


if __name__ == '__main__':
    circles = []
    rectangles = []
    NUM_OBJECTS = 3
    MIN = 10
    MAX = 20
    colors = ["green", "yellow", "blue", "red", "pink"]
    for i in range(NUM_OBJECTS):
        colors = random.choice(colors)
        radius = random.randint(MIN, MAX)
        circles.append(Circle(colors, radius))
        circles[i].draw()
    print(f"Num circles is {Circle.get_num_circles()}")

    for i in range(NUM_OBJECTS):
        colors = random.choice(colors)
        width = random.randint(MIN, MAX)
        height = random.randint(MIN, MAX)
        rectangles.append(Rectangle(colors, width, height))
        rectangles[i].draw()
        rectangles[i].print_area()