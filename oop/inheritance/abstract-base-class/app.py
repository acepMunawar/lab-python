from circle import Circle
from rectangle import Rectangle

if __name__ == "__main__":
    shape_list = [
        Rectangle(10, 20),
        Circle(10)
    ]

for shape in shape_list:
    print(shape.area())