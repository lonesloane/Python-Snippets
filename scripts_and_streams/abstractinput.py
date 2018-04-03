__author__ = 'stephane'

from xml.dom import minidom
import urllib
import StringIO


class ParseXml(object):

    def __init__(self):
        pass

    @staticmethod
    def test_parse_xml():
        print('\n**********************')
        print("Parse xml from file:")
        print('**********************')
        with open("binary.xml") as fsock:  # this creates a 'file' object
            xmldoc = minidom.parse(fsock)
            print(xmldoc.toxml())

    @staticmethod
    def test_from_url():
        print('\n**********************')
        print("Parse xml from url:")
        print('**********************')
        urlsock = urllib.urlopen("http://slashdot.org/slashdot.rdf")
        xmldoc = minidom.parse(urlsock)
        urlsock.close()
        print(xmldoc.toxml())

    @staticmethod
    def test_from_string():
        print('\n**********************')
        print("Parse xml from string the hard way:")
        print('**********************')
        contents = "<grammar><ref id='bit'><p>0</p><p>1</p></ref></grammar>"
        xmldoc = minidom.parseString(contents)  # why not use minidom.parse ?!?
        print(xmldoc.toxml())

    @staticmethod
    def test_from_string_file_like():
        print('\n**********************')
        print("Parse xml from string the good way:")
        print('**********************')
        contents = "<grammar><ref id='bit'><p>0</p><p>1</p></ref></grammar>"
        ssock = StringIO.StringIO(contents)
        xmldoc = minidom.parse(ssock)
        ssock.close()
        print(xmldoc.toxml())


def main():
    parseXml = ParseXml()
    parseXml.test_parse_xml()
    parseXml.test_from_url()
    parseXml.test_from_string()
    parseXml.test_from_string_file_like()


if __name__ == "__main__":
    main()