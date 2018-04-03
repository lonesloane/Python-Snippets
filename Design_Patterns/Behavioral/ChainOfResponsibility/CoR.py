class Car:
    def __init__(self, name, water, fuel, oil):
        self.name = name
        self.water = water
        self.fuel = fuel
        self.oil = oil

    def is_fine(self):
        if self.water >= 20 and self.fuel >= 5 and self.oil >= 10:
            print('Car is good to go.')
            return True
        else:
            return False


class Handler:
    def __init__(self, successor=None):
        self._successor = successor

    def handle_request(self, car: Car):
        if not car.is_fine() and self._successor is not None:
            self._successor.handle_request(car)


class WaterHandler(Handler):
    def handle_request(self, car: Car):
        if car.water < 20:
            car.water = 100
            print('Added water')
        super().handle_request(car)


class FuelHandler(Handler):
    def handle_request(self, car: Car):
        if car.fuel < 5:
            car.fuel = 100
            print('Added fuel')
        super().handle_request(car)


class OilHandler(Handler):
    def handle_request(self, car: Car):
        if car.oil < 10:
            car.oil = 100
            print('Added oil')
        super().handle_request(car)


# === usage ===
garage_handler = OilHandler(FuelHandler(WaterHandler()))
bad_car = Car('piece of rust', 1, 1, 1)
garage_handler.handle_request(bad_car)
garage_handler.handle_request(bad_car)

less_bad_car = Car('piece of dust', 5, 5, 5)
garage_handler.handle_request(less_bad_car)
