class Apple:
    def __init__(self, c, w, p, d):
        #placeは産地
        #daysは収穫されてからの日数
        self.color = c
        self.weight = w
        self.place = p
        self.days = d
        print("created!!")

app1 = Apple("red", 100, "青森", "10")
print(app1)