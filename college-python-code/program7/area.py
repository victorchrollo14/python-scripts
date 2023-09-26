import math


class Shape:
    def __init__(self):
        self.name = ""
        self.area = 0

    def showArea(self):
        print(f"The Area of {self.name}: {self.area}")


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        self.name = "Circle"

    def calArea(self):
        self.area = math.pi * self.radius * self.radius


c1 = Circle(10)
c1.calArea()
c1.showArea()
