class Pet(object):
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def getName(self):
        return self.name

    def getSpecies(self):
        return self.species

    def __str__(self):
        return "%s is a %s" % (self.name, self.species)

class Dog(Pet):

    def __init__(self, name, chases_cats):
        super().__init__(name, "Dog")
        self.chases_cats = chases_cats

    def chasesCats(self):
        return self.chases_cats

    def __str__(self):
        additional_info = ''
        if self.chases_cats:
            additional_info += ' who chases cats'
        return super().__str__() + additional_info


pet = Pet('Polly', 'Parrot')
print(pet)

pup = Dog('Elsa', True)
print(pup)
print(Dog.__bases__)
print(Pet.__subclasses__())