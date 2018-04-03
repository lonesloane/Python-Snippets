import os
import string


def read_file():
    file_path = os.path.join("c:/", "temp/", "DotStatConfigurationLoader.log")
    print("file path: " + file_path)
    with open(file_path,'r') as myFile:
        for currLine in myFile:
            print(currLine)


def read_lines():
    with open("sample_file.txt") as fin:
        lines = fin.readlines()
        for line in lines:
            words = line.split()
            for word in words:
                word = word.strip()
                word = word.translate(None, string.punctuation)
                word = word.lower()
                print(word)
