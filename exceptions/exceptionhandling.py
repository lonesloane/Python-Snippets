__author__ = 'stephane'


class ExceptTest(object):
    def __init__(self):
        pass

    @staticmethod
    def tryexcept():
        print'\n**********************'
        print "Try Except block:"
        print'**********************\n'
        try:
            fsock = open("/notexistent")
        except IOError:
            print "File does not exist"
            return 1
        else:
            print "this is run if no exception is raised"
            return 2
        finally:
            print "This is run whether there is an exception or not"

        print "This will be run if except or finally are not returning..."


def main():
    excepttest = ExceptTest()

    returncode = excepttest.tryexcept()
    print "returncode: %d" % returncode

if __name__ == '__main__':
    main()