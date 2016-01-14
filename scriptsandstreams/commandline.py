__author__ = 'stephane'

import sys

class CommandLine(object):

    def __init__(self):
        pass

    @staticmethod
    def test_argv():
        print'\n**********************'
        print "sys.argv :"
        print'**********************'
        for argv in sys.argv:
            print argv

def main():
    commandline = CommandLine()
    # in the console, run commandline.py arg1 arg2
    commandline.test_argv()

if __name__ == "__main__":
    main()