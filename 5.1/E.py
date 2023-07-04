class Rectangle:

    def __init__(self, cord1, cord2):
        self.cord1 = cord1
        self.cord2 = cord2

    def perimeter(self):
        self.d = round(0.5 ** ((self.cord1[0] - self.cord2[0]) ** 2 + (self.cord1[1] - self.cord2[1])), 2)
        self.a = abs(self.cord1[0] - self.cord2[0])
        self.p = 2 * (self.a * (0.5 ** (self.d ** 2 - self.a ** 2)))
        return self.p


rect = Rectangle((3.2, -4.3), (7.52, 3.14))
print(rect.perimeter())
