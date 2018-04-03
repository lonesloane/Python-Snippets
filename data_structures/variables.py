__author__ = 'stephane'

class Variables(object):

    def __init__(self):
        pass

    @staticmethod
    def assign_values():
        #assign multiple values
        v = ('a', 'b', 'e')
        (x, y, z) = v
        print("x: " + x)
        print("y: " + y)
        print("z: " + z)
        #assign consecutive values
        print("\nRange(7)")
        print(range(7))
        (Zero, Un, Deux, Trois, Quatre, Cinq, Six) = range(7)
        print("Zero: ")
        print(Zero)
        print("Deux: ")
        print(Deux)
        print("Six: ")
        print(Six)

def main():
    testvariables = Variables()
    testvariables.assign_values()

if __name__ == "__main__":
    main()