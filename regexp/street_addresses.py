__author__ = 'stephane'

import re

class RegExTest(object):
    def __init__(self):
        pass

    @staticmethod
    def endofstring():
        print'\n**********************'
        print "change end of string:"
        print'**********************\n'
        s1 = "100 NORTH MAIN ROAD"
        s2 = "100 NORTH BROAD ROAD"
        print "s1: %s" % s1
        print "s2: %s" % s2

        print "Replace..."
        print s1.replace("ROAD", "RD.")
        print s2.replace("ROAD", "RD.")

        print "RegExp..."
        print re.sub("ROAD$", "RD.", s1)  # $ is symbol for end of string
        print re.sub("ROAD$", "RD.", s2)

    @staticmethod
    def middleofstring():
        print'\n**********************'
        print "change a word in middle of string:"
        print'**********************\n'
        s1 = "100 BROAD ROAD APT. 3"
        print "s1: %s" % s1

        print "RegExp..."
        print re.sub(r"\bROAD\b", "RD.", s1)  # r indicates raw string, i.e. no "python" escape characters
                                              # \b indicates word boundary


def main():
    regextest = RegExTest()

    regextest.endofstring()
    regextest.middleofstring()

if __name__ == '__main__':
    main()