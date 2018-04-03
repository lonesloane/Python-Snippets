__author__ = 'stephane'


class BuiltInTest(object):
    def __init__(self):
        pass

    @staticmethod
    def type():
        print('\n**********************')
        print("Type introspection:")
        print('**********************\n')
        print("numbers")
        print(type(1))
        print(type(1.0))
        print(type(2+3j))
        print("list, dico, tuples")
        li = []
        print(type(li))
        dic = {}
        print(type(dic))
        tup = ()
        print(type(tup))
        print("objects")
        print(type(BuiltInTest))

    @staticmethod
    def str():
        print('\n**********************')
        print( "str function:")
        print('**********************\n')
        print("str(1): %s" % str(1))
        li = ["Souvent pour s'amuser","les hommes d'equipage","Prennent des albatros","vastes oiseaux des mers"]
        print(li)
        print("str(li): %s" % str(li))

    @staticmethod
    def dir():
        print('\n**********************')
        print("dir function:")
        print('**********************\n')
        print("list")
        li = []
        print(dir(li))
        print("dictionary")
        dic = {}
        print(dir(dic))
        print("tuple")
        tup = ()
        print(dir(tup))


def main():
    builtintest = BuiltInTest()

    builtintest.type()
    builtintest.str()
    builtintest.dir()


if __name__ == '__main__':
    main()
