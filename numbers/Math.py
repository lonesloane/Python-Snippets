import math


def print_constants():
    print("pi is: ", math.pi)
    print("e is: ", math.e)


def odd(spin):
    if spin % 2 == 1:
        print(True)
        return
    print(False)


def run():
    odd(7)
    odd(4)
    rndm(10)


if __name__ == '__main__':
    print_constants()
    run()
