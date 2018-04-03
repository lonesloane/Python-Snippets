__author__ = 'stephane'


class ParamTest(object):
    def __init__(self):
        pass

    @staticmethod
    def optional_named(mandatory, optional1=0, optional2=0):
        print('\n**********************')
        print("Optional parameters:")
        print('**********************\n')
        print("mandatory=%s\n optional1=%d\n optional2=%d" % (mandatory, optional1, optional2))


def main():
    paramtest = ParamTest()

    paramtest.optional_named("All parameters", 11, 22)
    paramtest.optional_named("Only mandatory")
    paramtest.optional_named("Mandatory and optional1", 11)
    paramtest.optional_named("Mandatory and optional2", optional2=22)


if __name__ == '__main__':
    main()
