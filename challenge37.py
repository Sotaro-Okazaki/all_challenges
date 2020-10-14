import math

class Circle:
    def __init__(self, r):
        self.radius = r
        print("created!!")

    def area(self):
        return self.radius ** 2 * math.pi

circle1 = Circle(2)
print(circle1.area())
