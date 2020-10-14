class Horse:
    def __init__(self, name, c, s, rider):
        self.name = name
        self.color = c
        self.sex = s
        self.rider = rider

class Rider:
    def __init__(self, name):
        self.name = name


eddery = Rider("P.J.Eddery")
dancing_brave = Horse("Dancing Brave", "brown", "male", eddery)
print(dancing_brave.rider.name)
