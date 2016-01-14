"""
Created on 26 mai 2014

@author: varin_s

Split xml files and create multiple text files in subdirectory
based on file name
"""

import os
import xml.etree.cElementTree as Et

xml_file_folder = ""


def split_xml_file():
    xml_file = "9789264202733-en.xml"
    tree = Et.ElementTree(file=os.path.join(xml_file_folder, xml_file))
    root = tree.getroot()
    # Loop over xml structure
    for child_of_root in root:
        print child_of_root.tag, child_of_root.attrib
        folder = xml_file.split(".")[0]
        # Create folder based on xml file name
        if not os.path.exists(os.path.join(xml_file_folder, folder)):
            os.makedirs(os.path.join(xml_file_folder, folder))
        # Create new file to store xml text content
        with open(os.path.join(xml_file_folder, folder, child_of_root.attrib["id"]+".txt"), 'wb') as xml_result:
            if child_of_root.text:
                xml_result.write(child_of_root.text.encode("utf-16"))

if __name__ == '__main__':
    xml_file_folder = "Y:"
    split_xml_file()
