from abc import ABC, abstractmethod

class Image(ABC):
    def save_image(self):
        pass

    def load_image(self):
        pass


class Bitmap(Image):
    def save_image(self, p1):
        print(f"saving bit map file {p1}")

    def load_image(self, p2):
        print(f"loading bit map file {p2}")


class Jpeg(Image):
    def save_image(self, p3):
        print(f"saving bit map file {p3}")
    def load_image(self, p4):
        print(f"loading bit map file {p4}")

if __name__ == '__main__':
    bitmap1 = Bitmap()
    bitmap1.save_image("kku.bmp")
    bitmap1.load_image("kku.bmp")
    jpeg1 = Jpeg()
    jpeg1.save_image("en.jpg")
    jpeg1.load_image("en.jpg")