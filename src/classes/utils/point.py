import math
class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self, b):
        return Point(self.x + b.x, self.y + b.y)

    def subtract(self, b):
        return Point(self.x - b.x, self.y - b.y)

    def multiply(self, b):
        return Point(self.x * b.x - self.y * b.y, self.x * b.y + self.y * b.x)

    def multiply_scalar(self, b):
        return Point(self.x * b, self.y * b)

    def conjugate(self):
        return Point(self.x, -self.y)

    def mod(self):
        return math.sqrt(self.x**2 + self.y**2)

    def arg(self):
        return math.atan2(self.y, self.x)

    def polar(self, r, theta):
        return Point(r * math.cos(theta), r * math.sin(theta))

    def rotate(self, p, q, theta):
        return (p.subtract(q)).multiply(Point(math.cos(theta), math.sin(theta))).add(q)

    # Function used to display X and Y coordinates of a point
    def display_point(self, p):
        print(f"({p.x}, {p.y})")