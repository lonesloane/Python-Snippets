class Observable:

    def __init__(self):
        self.observers = []

    def register(self, observer):
        if observer not in self.observers:
            self.observers.append(observer)

    def unregister(self, observer):
        if observer in self.observers:
            self.observers.remove(observer)

    def unregister_all(self):
        if self.observers:
            del self.observers[:]

    def update_observers(self, *args, **kwargs):
        for observer in self.observers:
            observer.update(*args, **kwargs)


# Abstract Observer Class
class Observer:
    def update(self, *args, **kwargs):
        pass


class AmericanStockMarket(Observer):
    def update(self, *args, **kwargs):
        print('American stock market received: {0}\n{1}'.format(args, kwargs))


class EuropeanStockMarket(Observer):
    def update(self, *args, **kwargs):
        print('European stock market received: {0}\n{1}'.format(args, kwargs))


# === usage ===
big_company = Observable()
asm_observer = AmericanStockMarket()
esm_observer = EuropeanStockMarket()
big_company.register(asm_observer)
big_company.register(esm_observer)

big_company.update_observers('important_update', msg='CEO unexpectedly resigns')
