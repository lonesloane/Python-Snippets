__author__ = 'stephane'

count = 0  # global variable
known = {0: 0, 1: 1}


def modify_count_wrong():
    for i in range(10):
        count += 1  # WRONG ==> local declaration "shadows" the global variable


def modify_count_correct():
    global count  # declare locally the global variable
    for i in range(10):
        count += 1


def modify_known_correct():
    known[0] = 2  # correct since the value is mutable, we are not re-assigning it
    print known
    global known  # and we can also access the global variable
    known = {0: 'a', 1: 'b'}
    print known


def modify_known_wrong():
    known = dict()  # a local known dictionary is created, but the global one is not affected
    print known


if __name__ == '__main__':
    print count  # global variable is accessible to __main__
    count += 1
    print count
    modify_count_correct()
    print count
    print known
    modify_known_correct()
    modify_known_wrong()
    print known
