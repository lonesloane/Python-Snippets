__author__ = 'stephane'

import re

class RegExTest(object):
    def __init__(self):
        pass

    @staticmethod
    def checkverbose():
        print('\n**********************')
        print( "checking a verbose regular expression:")
        print('**********************\n')
        pattern = """
        ^                   # Beginning of string
        M{0,4}              # Thousands - O to 4 Ms
        (CM|CD|D?C{0,3})    # Hundreds
        (XC|XL|L?X{0,3})    # Tens
        (IX|IV|V?I{0,3})    # Units
        $                   # End of string
        """
        print( "M:")
        print( re.search(pattern, "M", re.VERBOSE))
        print( "MCMLXXXIX:")
        print( re.search(pattern, "MCMLXXXIX", re.VERBOSE))
        print( "MMMMDCCCLXXXVIII:")
        print( re.search(pattern, "MMMMDCCCLXXXVIII", re.VERBOSE))

def main():
    regextest = RegExTest()

    regextest.checkverbose()

if __name__ == '__main__':
    main()