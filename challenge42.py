class Shape:
    def what_am_i(self):
        print("I am a shape")

class Rectangle(Shape):
    def __init__(self, w, l):
        self.width = w
        self.len = l

class Square(Shape):
    def __init__(self, s):
        self.side = s

rc1 = Rectangle(10, 8)
sq1 = Square(10)

rc1.what_am_i()
sq1.what_am_i()
