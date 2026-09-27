from src.figure import Figure


class Triangle(Figure):
    def __init__(self, side_a, side_b, side_c):
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

        if any(type(a) not in (int, float) for a in (side_a, side_b, side_c)):
            raise TypeError('Triangle sides must be integer or float type')

        if any(a < 0 for a in (side_a, side_b, side_c)):
            raise ValueError('Triangle side must be positive')

        if not (side_a + side_b > side_c and side_b + side_c > side_a and side_c + side_a > side_b):
            raise ValueError(f"Such a triangle cannot exist with sides: {side_a}, {side_b}, {side_c}")

    def perimeter(self):
        return self.side_a + self.side_b + self.side_c

    def area(self):
        p = self.perimeter() / 2
        return (p * (p - self.side_a) * (p - self.side_b) * (p - self.side_c)) ** 0.5
