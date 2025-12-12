from shape import Shape

class Rectangle(Shape):
    def __init__(self, length, widht):
        self.length = length
        self.widht = widht

    def area(self):
        return self.length * self.widht
    