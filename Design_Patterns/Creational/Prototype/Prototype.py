from copy import deepcopy
import uuid


class Car:

    def __init__(self):
        self.__uuid = uuid.uuid4()
        self.__wheels = list()
        self.__engine = None
        self.__body = None

    def set_body(self, body):
        self.__body = body

    def attach_wheel(self, wheel):
        self.__wheels.append(wheel)

    def set_engine(self, engine):
        self.__engine = engine

    def specification(self):
        print('Identifier: %s' % self.__uuid)
        print('Body: %s' % self.__body.shape)
        print('Engine horsepower: %s' % self.__engine.horsepower)
        print('Tire size: %s' % self.__wheels[0].size)

    def clone(self):
        clone = deepcopy(self)
        clone.__uuid = uuid.uuid4()
        return clone

# === Car Parts ===


class Wheel:
    size = None

    def __init__(self, size):
        self.size = size


class Engine:
    horsepower = None

    def __init__(self, horsepower):
        self.horsepower = horsepower


class Body:
    shape = None

    def __init__(self, shape):
        self.shape = shape


class Director:
    __builder = None

    def set_builder(self, builder):
        self.__builder = builder

    def get_car(self):
        car = Car()

        body = self.__builder.get_body()
        car.set_body(body)

        engine = self.__builder.get_engine()
        car.set_engine(engine)

        for i in range(0, 3):
            wheel = self.__builder.get_wheel()
            car.attach_wheel(wheel)

        return car


class IBuilder:

    def get_wheel(self): pass

    def get_body(self): pass

    def get_engine(self): pass


class JeepBuilder(IBuilder):

    def get_wheel(self):
        return Wheel(22)

    def get_body(self):
        return Body('SUV')

    def get_engine(self):
        return Engine(400)


class NissanBuilder(IBuilder):

    def get_wheel(self):
        return Wheel(16)

    def get_body(self):
        return Body('HatchBack')

    def get_engine(self):
        return Engine(100)


# === Usage ===

director = Director()
director.set_builder(JeepBuilder())
jeep = director.get_car()  # called only once if very costly (i.e. requires access to db or file system)
print('Jeep 1 specifications:')
jeep.specification()
print('-'*15)
jeep2 = jeep.clone()  # much less costly than invoking the director to build another instance
print('Jeep 2 specifications:')
jeep2.specification()
print('-'*15)
jeep3 = jeep.clone()
print('Jeep 3 specifications:')
jeep3.specification()
