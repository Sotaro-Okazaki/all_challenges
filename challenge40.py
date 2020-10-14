class Rectangle:
    def __init__(self, w, l):
        self.width = w
        self.len = l

    def calculate_perimeter(self):
        return self.width * 2 + self.len * 2

class Square(Rectangle):
    pass

rc1 = Rectangle(10, 3)
sq1 = Square(10, 10)

print(rc1.calculate_perimeter())
print(sq1.calculate_perimeter())
    