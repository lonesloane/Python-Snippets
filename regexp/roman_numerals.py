__author__ = 'stephane'

import re

class RegExTest(object):
    def __init__(self):
        pass

    @staticmethod
    def checkthousands():
        print('\n**********************')
        print("checking for thousands:")
        print('**********************\n')
        pattern = r'^M?M?M?$'  # match strings composed only of 0 to 3 Ms
        print('empty string:')
        print(re.search(pattern, ''))
        print('M:')
        print(re.search(pattern, 'M'))
        print('MM:')
        print(re.search(pattern, 'MM'))
        print('MMM:')
        print(re.search(pattern, 'MMM'))
        print('MMMM:')
        print(re.search(pattern, 'MMMM'))
        print('MMXV:')
        print(re.search(pattern, 'MMXV'))

    @staticmethod
    def checkhundreds():
        print('\n**********************')
        print("checking for hundreds:")
        print('**********************\n')
        # (a|b) mutually exclusive tests
        # ^ beginning of line
        # $ end of line
        # ? optional element
        pattern = r'^M?M?M?(CM|CD|D?C?C?C?)$'
        print('empty string:')
        print(re.search(pattern, ''))
        print('MCM:')
        print(re.search(pattern, 'MCM'))
        print('MD:')
        print(re.search(pattern, 'MD'))
        print('MMMCCC:')
        print(re.search(pattern, 'MMMCCC'))
        print('MCMC:')
        print(re.search(pattern, 'MCMC'))

    @staticmethod
    def checkcompact():
        print('\n**********************')
        print("compact syntax:")
        print('**********************\n')
        pattern = r'^M{0,3}(CM|CD|D?C{0,3})$'
        print('empty string:')
        print(re.search(pattern, ''))
        print('MCM:')
        print(re.search(pattern, 'MCM'))
        print('MD:')
        print(re.search(pattern, 'MD'))
        print('MMMCCC:')
        print(re.search(pattern, 'MMMCCC'))
        print('MCMC:')
        print(re.search(pattern, 'MCMC'))

    @staticmethod
    def checkromannumber():
        print('\n**********************')
        print("full roman number validation:")
        print('**********************\n')
        pattern = r'^M{0,4}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$'
        print('empty string:')
        print(re.search(pattern, ''))
        print('MDLV:')
        print(re.search(pattern, 'MDLV'))
        print('MMDCLXVI:')
        print(re.search(pattern, 'MMDCLXVI'))
        print('MMMMDCCCLXXXVIII:')
        print(re.search(pattern, 'MMMMDCCCLXXXVIII'))
        print('I:')
        print(re.search(pattern, 'I'))

def main():
    regextest = RegExTest()

    regextest.checkthousands()
    regextest.checkhundreds()
    regextest.checkcompact()
    regextest.checkromannumber()

if __name__ == '__main__':
    main()