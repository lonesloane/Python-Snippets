class ISocket:
    def voltage(self): pass

    def live(self): pass

    def neutral(self): pass


# Adaptee (Source) interface
class IEuropeanSocket(ISocket):

    def earth(self): pass


# Target interface
class IUSASocket(ISocket):
    pass


# Adaptee
class EuropeanSocket(IEuropeanSocket):

    def voltage(self):
        return 230

    def live(self):
        return 1

    def neutral(self):
        return -1

    def earth(self):
        return 0


# Client
class AmericanKettle:

    __power = None

    def __init__(self, power: ISocket):
        self.__power = power

    def boil(self):
        if self.__power is not None and self.__power.voltage() > 110:
            print('Kettle on fire!!!')
        else:
            if self.__power.live() == 1 and self.__power.neutral() == -1:
                print('Coffee time :-)')
            else:
                print('No power :-(')


# Adapter
class SocketAdapter(IUSASocket):
    __socket = None

    def __init__(self, socket: IEuropeanSocket):
        self.__socket = socket

    def voltage(self):
        return 110

    def live(self):
        return self.__socket.live()

    def neutral(self):
        return self.__socket.neutral()


# === usage ===


eu_socket = EuropeanSocket()
kettle = AmericanKettle(eu_socket)
kettle.boil()

socket_adapter = SocketAdapter(eu_socket)
kettle = AmericanKettle(socket_adapter)
kettle.boil()
