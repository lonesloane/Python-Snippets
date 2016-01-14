# -*- coding: utf-8 -*-

__author__ = 'stephane'


class FormatStrings(object):

    def __init__(self):
        pass

    @staticmethod
    def tabulating():
        fat_cat = """
        I'll do a list:
        \t* Cat food
        \t* Fishies
        \t* Catnip\n\t* Grass
        """
        print fat_cat

    @staticmethod
    def format():
        print'\n**********************'
        print "format strings:"
        print'**********************'
        x = "nature"
        y = "temple"
        print "La %s est un %s" % (x, y)

    @staticmethod
    def formatter():

        formatter = "%s %s %s %s"

        print formatter % (1, 2, 3, 4)
        print formatter % ("one", "two", "three", "four")
        print formatter % (True, False, True, False)
        print formatter % (formatter, formatter, formatter, formatter)
        print formatter % (
            "La nature est un temple",
            "où de vivants piliers",
            "laissent parfois sortir",
            "de confuses paroles"
        )

    @staticmethod
    def format_full(date, time, workflow_name, workflow_part, nb_docs, nb_failed_docs, nb_characters, time_elapsed):
        _logLine = \
            "{_date}|{_time}|{_workflowName}|{_workflowPart}|{_nbDocs}|{_nbFailedDocs}|{_nbCharacters}|{_timeElapsed}" \
            .format(
                _date=date,
                _time=time,
                _workflowName=workflow_name,
                _workflowPart=workflow_part,
                _nbDocs=nb_docs,
                _nbFailedDocs=nb_failed_docs,
                _nbCharacters=nb_characters,
                _timeElapsed=time_elapsed)

        print _logLine

    @staticmethod
    def format_not_concat():
        print'\n**********************'
        print "format or concat:"
        print'**********************'
        s = "Nous partimes"
        cinqcent = 500
        print "Format"
        print "%s %d" % (s, cinqcent,)

        print "Concat"
        try:
            print s + cinqcent
        except Exception as exc:
            print "Ouch! " + exc.message

    @staticmethod
    def format_number():
        print'\n**********************'
        print "format numbers:"
        print'**********************'
        print "Ceci est un nombre decimal: %f" % 3.14159
        print "Ceci est un nombre decimal arrondi: %.2f" % 3.14159
        print "Ceci est un nombre decimal arrondi positif: +%.2f" % 3.14159

    @staticmethod
    def split():
        print'\n**********************'
        print "split and join strings:"
        print'**********************'
        str = "je fais souvent ce reve etrange et penetrant d'une femme inconnue et que j'aime et qui m'aime"
        li = str.split(" ")
        print li
        anotherstring = "-".join(li)
        print anotherstring

    @staticmethod
    def replace():
        print'\n**********************'
        print "replace patterns in strings:"
        print'**********************'
        str = "je fais souvent ce reve etrange et penetrant d'une femme inconnue et que j'aime et qui m'aime"
        print str
        pattern = "aime"
        replacement = "adore"
        str = str.replace(pattern, replacement)
        print str

    @staticmethod
    def string_as_sequence():
        print'\n**********************'
        print "Strings are sequences:"
        print'**********************'
        s = "spam"
        print "string length: %d" % len(s)
        print "First letter: %s" % s[0]
        print "Last letter: %s" % s[3]
        # backward indexing:
        print "First letter: %s" % s[-4]
        print "Last letter: %s" % s[-1]
        # slices
        print "Middle letters: %s" % s[1:3]
        # and ranges
        print "s[1:]: %s" % s[1:]
        print "s[0:3]: %s" % s[0:3]
        print "s[:3]: %s" % s[:3]
        print "s[:-1]: %s" % s[:-1]
        # top level copy
        print "s[:]: %s" % s[:]
        # concat
        print "s+'xyz': %s" % s+'xyz'
        # repetition
        print "s*5: %s" % (s*5)

    @staticmethod
    def immutable():
        print'\n**********************'
        print "Strings are immutable objects:"
        print'**********************'
        s = 'La nature est un temple'
        print "s: %s" % s
        try:
            s[0] = 'l'
        except Exception as exc:
            print "Ouch! " + exc.message
        # Only way is by creating a partial copy
        s = 'l' + s[1:]
        print s

def main():
    testformatstrings = FormatStrings()

    testformatstrings.format()
    testformatstrings.format_not_concat()
    testformatstrings.format_number()
    testformatstrings.split()
    testformatstrings.replace()
    testformatstrings.string_as_sequence()
    testformatstrings.immutable()

if __name__ == "__main__":
    main()
