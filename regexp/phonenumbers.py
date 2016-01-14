__author__ = 'stephane'

import re

class PhoneNumberTest(object):
    def __init__(self):
        pass

    @staticmethod
    def findnumbers():
        print'\n**********************'
        print "Find numbers in phone number:"
        print'**********************\n'
        pattern = re.compile(r'^(\d{3})-(\d{3})-(\d{4})$')
        print "800-555-1212"
        print pattern.search("800-555-1212").groups()

    @staticmethod
    def findextension():
        print'\n**********************'
        print "Find extension in phone number:"
        print'**********************\n'
        pattern = re.compile(r'^(\d{3})-(\d{3})-(\d{4})-(\d+)$')
        print "800-555-1212-1234"
        print pattern.search("800-555-1212-1234").groups()
        print "800 555 1212 1234"
        print pattern.search("800 555 1212 1234")
        print "800-555-1212"
        print pattern.search("800-555-1212")

    @staticmethod
    def handleseparators():
        print'\n**********************'
        print "Find extension in phone number:"
        print'**********************\n'
        pattern = re.compile(r'^(\d{3})\D+(\d{3})\D+(\d{4})\D+(\d+)$')
        print "800-555-1212-1234"
        print pattern.search("800-555-1212-1234").groups()
        print "800 555 1212 1234"
        print pattern.search("800 555 1212 1234").groups()
        print "80055512121234"
        print pattern.search("80055512121234")
        print "800-555-1212"
        print pattern.search("800-555-1212")

    @staticmethod
    def noseparatornoextension():
        print'\n**********************'
        print "Find extension in phone number:"
        print'**********************\n'
        pattern = re.compile(r'^(\d{3})\D*(\d{3})\D*(\d{4})\D*(\d*)$')
        print "800-555-1212-1234"
        print pattern.search("800-555-1212-1234").groups()
        print "800.555.1212 x1234"
        print pattern.search("800.555.1212 x1234").groups()
        print "800 555 1212 1234"
        print pattern.search("800 555 1212 1234").groups()
        print "80055512121234"
        print pattern.search("80055512121234").groups()
        print "800-555-1212"
        print pattern.search("800-555-1212").groups()
        print "(800)5551212 x1234"
        print pattern.search("(800)5551212 x1234")

    @staticmethod
    def handleleadingchars():
        print'\n**********************'
        print "Handle leading characters:"
        print'**********************\n'
        pattern = re.compile(r'^\D*(\d{3})\D*(\d{3})\D*(\d{4})\D*(\d*)$')
        print "(800)5551212 x1234"
        print pattern.search("(800)5551212 x1234").groups()

        print "work 1(800)5551212 x1234"
        print pattern.search("work 1(800)5551212 x1234")

    @staticmethod
    def completephonenumberextractor():
        print'\n**********************'
        print "Final version:"
        print'**********************\n'
        pattern = re.compile(r'(\d{3})\D*(\d{3})\D*(\d{4})\D*(\d*)$')
        print "(800)5551212 x1234"
        print pattern.search("(800)5551212 x1234").groups()
        print "work 1(800)5551212 x1234"
        print pattern.search("work 1(800)5551212 x1234").groups()

    @staticmethod
    def verboseextractor():
        print'\n**********************'
        print "Final version (verbose):"
        print'**********************\n'
        pattern = re.compile(r"""
                    # don't match beginning of line
        (\d{3})     # area code is 3 digits
        \D*         # optional separator
        (\d{3})     # trunk is 3 digits
        \D*         # optional separator
        (\d{4})     # rest of number if 4 digits
        \D*         # optional separator
        (\d*)       # optional extension
        $          # end of string
        """, re.VERBOSE)
        print "(800)5551212 x1234"
        print pattern.search("(800)5551212 x1234").groups()
        print "work 1(800)5551212 x1234"
        print pattern.search("work 1(800)5551212 x1234").groups()

def main():
    phonenumbertest = PhoneNumberTest()

    phonenumbertest.findnumbers()
    phonenumbertest.findextension()
    phonenumbertest.handleseparators()
    phonenumbertest.noseparatornoextension()
    phonenumbertest.handleleadingchars()
    phonenumbertest.completephonenumberextractor()
    phonenumbertest.verboseextractor()

if __name__ == '__main__':
    main()