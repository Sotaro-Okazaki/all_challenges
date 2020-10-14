class Square:

    def __init__(self, s):
        self.side = s
    
    def __repr__(self):
        r = "{} by ".format(self.side) * 4
        return r[0: -4]

sq1 = Square(10)
print(sq1)