class MakeMeal:

    def buy_ingredients(self, money):
        if money < self.cost:
            assert 0, 'Not enough money to buy ingredients!!!'

    def prepare(self):
        pass

    def cook(self):
        pass

    def go(self, money):
        self.buy_ingredients(money)
        self.prepare()
        self.cook()


class MakePizza(MakeMeal):

    def __init__(self):
        self.cost = 5

    def prepare(self):
        print('Prepare pizza - make the dough and add toppings')

    def cook(self):
        print('Cook pizza - cook in the oven on mark 8 for 10 minutes')


class MakeCake(MakeMeal):

    def __init__(self):
        self.cost = 5

    def prepare(self):
        print('Prepare cake - mix ingredients together and pour into cake tin')

    def cook(self):
        print('Cook cake - bake in the oven on mark 6 for 20 minutes')


# === usage ===
p = MakePizza()
p.go(5)

c = MakeCake()
c.go(5)

c.go(2)
