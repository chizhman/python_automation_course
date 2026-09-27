import math

from src.figure import Figure


class Circle(Figure):
    def __init__(self, radius):
        self.radius = radius

        if type(radius) not in (int, float):
            raise TypeError('Radius must be integer or float type')

        if radius < 0:
            raise ValueError('Radius must be positive')

    def perimeter(self):
        return 2 * math.pi * self.radius

    def area(self):
        return math.pi * self.radius ** 2

