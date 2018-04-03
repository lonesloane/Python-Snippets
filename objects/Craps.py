import random


class Dice:

    def __init__(self):
        self.faces = None

    def roll(self):
        self.faces = (random.randint(1, 6), random.randint(1, 6))

    def total(self):
        return sum(self.faces)

    def hardway(self):
        return self.faces[0] == self.faces[1]

    def easyway(self):
        return self.faces[0] != self.faces[1]


d1 = Dice()
d1.roll()
print("D1 total: {}".format(d1.total()))
print("D1 hardway: {}".format(d1.hardway()))

d2 = Dice()
d2.roll()
print("D2 total: {}".format(d2.total()))
print("D2 hardway: {}".format(d2.hardway()))