class Rectangle:
    def __init__(self, width, height):
        self.__private_width = width
        self.__private_height = height

    def __str__(self):
        return "This rectangle has width as "  + str(self.__private_width)  +  " height as " + str(self.__private_height)

    def set_width(self, new_width):
        self.__private_width = new_width

    def get_width(self):
        return self.__private_width

    def set_height(self, new_hight):
        self.__private_height = new_hight

    def get_height(self):
        return self.__private_height

if __name__ == '__main__':
    rect1 = Rectangle(3,4);
    print(rect1);
    print(f"Width is {rect1.get_width()}")
    rect1.set_height(5)
    print(f"Height is {rect1.get_height()}")



