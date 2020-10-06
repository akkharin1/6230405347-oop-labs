class Pet:
    def __init__(self, name):
        self.name = name

    def show_info(self):
        print(f"I'm {self.name}")

    def move(self):
        print(f"moving ...")

class Cat(Pet):
    def __init__(self, name, owner, color):
        self.owner = owner
        self.color = color
        super(Cat, self).__init__(name)

    def show_info(self):
        super(Cat, self).show_info()
        print(f"and is {self.color}")
        print(f"belonging to {self.owner}")

    def move(self):
        print(f"Cat likes to walk more than run")

class Dog(Pet):
    def __init__(self, name, owner, color):
        self.owner = owner
        self.color = color
        super(Dog, self).__init__(name)

    def show_info(self):
        super(Dog, self).show_info()
        print(f"and is {self.color}")
        print(f"belong to {self.owner}")

    def move(self):
        print("Dog likes to run more than walk")

    def eat_cat(self, cat):
        print(f"{self.name} eats cat {cat.name}")

if __name__ == '__main__':
    pet1= Pet("Thongdaeng")
    pet1.show_info()
    pet1.move()
    cat1 = Cat("Thongdee", "Manee", "White")
    cat1.show_info()
    cat1.move()
    dog1 = Dog("Thongdum", "Mana", "black")
    dog1.show_info()
    dog1.move()
    dog1.eat_cat(cat1)

