__author__ = 'stephane'


class TupleTest(object):
    def __init__(self):
        pass

    @staticmethod
    def define_tuple():
        print('\n**********************')
        print("Define tuple:")
        print('**********************')
        tu = ("server", "pilgrim", "database", "master", "user", "stephane")
        print(tu)
        print("t[0]: ")
        print(tu[0])
        print("t[-1]: ")
        print(tu[-1])
        print("t[0:3]: ")
        print(tu[0:3])
        print("\nonly method available: master in tu ")
        print("master" in tu)

    @staticmethod
    def assignment():
        print('\n**********************')
        print("tuple assignement:")
        print('**********************')
        addr = 'monty@python.org'
        uname, domain = addr.split('@')
        print("uname: ", uname)
        print("domain: ", domain)

    @staticmethod
    def return_tuple(arg1, arg2, arg3):
        print('\n**********************')
        print("Function return tuple:")
        print('**********************')
        return arg1, arg1+arg2, arg1+arg2+arg3

    @staticmethod
    def gather(arg1, arg2, *args):
        print('\n**********************')
        print("Gathers arguments into a tuple:")
        print('**********************')
        print(arg1)
        print(arg2)
        print(args)

    @staticmethod
    def scatter(arg1):
        print('\n**********************')
        print("Scatters arguments from a tuple:")
        print('**********************')
        try:
            for elem in arg1:
                print(elem)
        except TypeError:
            print(arg1)

    @staticmethod
    def zipit(t1, t2, t3):
        print('\n**********************')
        print("zip sequences into list of tuples:")
        print('**********************')
        zipped = zip(t1, t2, t3)
        return zipped


def main():
    tupletest = TupleTest()
    tupletest.define_tuple()
    tupletest.assignment()
    print(tupletest.return_tuple(1, 2, 3))
    tupletest.gather("hello", "world", "La nature", "est un temple", "ou de vivants piliers")
    t = (1, 2, 3, 4, 5)
    tupletest.scatter(t)
    tupletest.scatter("hello")
    tupletest.scatter(1)
    t1 = "Hello"
    t2 = [1, 2, 3, 4, 5]
    t3 = ['a', 'b', 'c', 'd', 'e']
    zipped = tupletest.zipit(t1, t2, t3)
    print(zipped)
    for elem1, elem2, elem3 in tupletest.zipit(t1, t2, t3):
        print(elem1, elem2, elem3)

if __name__ == '__main__':
    main()
