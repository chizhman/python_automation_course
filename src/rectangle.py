from src.figure import Figure


class Rectangle(Figure):
    def __init__(self, side_a, side_b):
        self.side_a = side_a
        self.side_b = side_b

        if any(type(a) not in (int, float) for a in (side_a, side_b)):
            raise TypeError('Rectangle sides must be integer or float type')

        if any(a < 0 for a in (side_a, side_b)):
            raise ValueError('Rectangle side must be positive')

    def perimeter(self):
        return (self.side_a + self.side_b) * 2

    def area(self):
        return self.side_a * self.side_b
