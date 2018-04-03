__author__ = 'stephane'

import sys


class Pipes(object):

    def __init__(self):
        pass


def test_stdout_and_stderr():
    print('\n**********************')
    print("Standard output and standard error:")
    print('**********************')
    for i in range(3):
        sys.stdout.write("Dive in\n")
    for i in range(3):
        sys.stderr.write("Dive out\n")


def main():
    pipes = Pipes()
    test_stdout_and_stderr()


if __name__ == "__main__":
    main()