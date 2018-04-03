__author__ = 'stephane'

import re

class PluralTest(object):
    def __init__(self):
        pass

    @staticmethod
    def plural(noun):
        if re.search('[sxz]$', noun):
            return re.sub('$', 'es', noun)
        elif re.search('[^aeioudgkprt]h$', noun):
            return re.sub('$', 'es', noun)
        elif re.search('[^aeiou]y$', noun):
            return re.sub('y$', 'ies', noun)
        else:
            return noun + 's'

def main():
    pluraltest = PluralTest()

if __name__ == '__main__':
    main()
