__author__ = 'stephane'


class FileTest(object):
    def __init__(self):
        pass

    @staticmethod
    def openfile():
        print'\n**********************'
        print "Open a file:"
        print'**********************\n'
        with open("./TestOpenFile.txt", "rb") as f:  # use with to make sure the file is properly closed
            print f
            print f.mode
            print f.name

    @staticmethod
    def readfile():
        print'\n**********************'
        print "Read a file:"
        print'**********************\n'
        with open("./TestReadFile.txt", "rb") as f:  # use with to make sure the file is properly closed
            print f.read()

    @staticmethod
    def write():
        print'\n**********************'
        print "Write to a file:"
        print'**********************\n'
        print "First, let's write..."
        with open("./TestWriteFile.txt", "w") as f:  # 'w' keyword for write (deletes previous content)
            f.write("Sous moi donc cette troupe s'avance")
        # Let's see what we have in the file
        with open("./TestWriteFile.txt", "rb") as f:  # use with to make sure the file is properly closed
            print f.read()
        print "\nNow, let's append to the file"
        with open("./TestWriteFile.txt", "a") as f:  # 'a' keyword for append (keeps previous content)
            f.write("\nEn portant sur le front cette male assurance")
        # We should have 2 lines
        with open("./TestWriteFile.txt", "rb") as f:  # use with to make sure the file is properly closed
            print f.read()
        print "\nLet's write again, should remove previous content..."
        with open("./TestWriteFile.txt", "w") as f:  # 'w' keyword for write (deletes previous content)
            f.write("Tant a nous voir marcher avec un tel visage\n"
                    "Les plus epouvantes reprenaient de courage")
        # Let's see what we have in the file
        with open("./TestWriteFile.txt", "rb") as f:  # use with to make sure the file is properly closed
            print f.read()


def main():
    file_test = FileTest()

    file_test.openfile()
    file_test.readfile()
    file_test.write()

if __name__ == '__main__':
    main()
