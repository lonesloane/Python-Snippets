__author__ = 'stephane'

import os

class DirectoryTest(object):
    def __init__(self):
        pass

    @staticmethod
    def joinpathnames():
        print'\n**********************'
        print "Join pathnames:"
        print'**********************\n'
        print os.path.join("/home/stephane/Documents", "Python")
        print os.path.expanduser("~")
        print os.path.join(os.path.expanduser("~"), "Python")

    @staticmethod
    def splitpathnames():
        print'\n**********************'
        print "Split pathnames:"
        print'**********************\n'
        print os.path.split("/home/stephane/Documents/Python.pdf")
        (filepath, filename) = os.path.split("/home/stephane/Documents/Python.pdf")
        print "filepath: %s" % filepath
        print "filename: %s" % filename
        (shortname, extension) = os.path.splitext(filename)
        print "shortname: %s" % shortname
        print "extension: %s" % extension

    @staticmethod
    def listdirectories():
        print'\n**********************'
        print "List directories:"
        print'**********************\n'
        print os.listdir("/home/stephane")
        dirname = "/home/stephane/Documents"
        print os.listdir(dirname)

        print [
            f for f in os.listdir(dirname)
            if os.path.isfile(os.path.join(dirname, f))
        ]

        print [
            f for f in os.listdir("/home/stephane")
            if (os.path.isdir(os.path.join("/home/stephane", f)) and ('.' not in f) )
        ]

def main():
    dirtest = DirectoryTest()

    dirtest.joinpathnames()
    dirtest.splitpathnames()
    dirtest.listdirectories()

if __name__ == '__main__':
    main()