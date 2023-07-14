class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, x1, y1):
        self.x = self.x + x1
        self.y = self.y + y1
    
    def length(self, second):
        return round(((self.x - second.x) ** 2 + (self.y - second.y) ** 2) ** 0.5, 2)


class PatchedPoint(Point):

    def __init__(self, *args):
        if not args:
            self.x, self.y = 0, 0
        elif len(args) == 1:
            self.x, self.y = args[0]
        else:
            self.x, self.y = args  
    
    def __str__(self):
        return f"({self.x}, {self.y})"
    
    def __repr__(self):
        return f"PatchedPoint({self.x}, {self.y})"
