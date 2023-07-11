class Rectangle:
    def __init__(self, xy1, xy2):
        self.xy1 = xy1
        self.xy2 = xy2
        self.a = round(abs(self.xy1[0] - self.xy2[0]), 2)
        self.b = round(abs(self.xy1[1] - self.xy2[1]), 2)
        self.p = 2 * self.a + 2 * self.b

    def perimeter(self):
        return round(self.p, 2)

    def area(self):
        return round(self.a * self.b, 2)
