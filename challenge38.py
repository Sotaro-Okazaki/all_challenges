class Triangle:
    def __init__(self, h, b):
        self.height = h
        self.bottom_line = b
        print("created!!")
    
    def area(self):
        return self.height * self.bottom_line / 2

triangle1 = Triangle(10, 6)
print(triangle1.area())