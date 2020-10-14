def f(a, b):
    return a is b

class Square:

    def __init__(self, s):
        self.side = s

sq1 = Square(10)
sq2 = Square(20)
sq3 = sq1

print(f(sq1, sq2))
print(f(sq1, sq3))