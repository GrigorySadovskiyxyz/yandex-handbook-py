class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, x1, y1):
        self.x = self.x + x1
        self.y = self.y + y1
    
    def length(self, second):
        return round(((self.x - second.x) ** 2 + (self.y - second.y) ** 2) ** 0.5, 2)

