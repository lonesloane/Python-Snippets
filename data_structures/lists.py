import os
import random

__author__ = 'stephane'


class ListTest(object):
    def __init__(self):
        pass

    @staticmethod
    def define_list():
        print('\n**********************')
        print("Define list:")
        print('**********************')
        li = ["server", "pilgrim", "database", "master", "user", "stephane"]
        print(li)
        print("li[0]: " + li[0])
        print("li[4]: " + li[4])
        print("li[-1]: " + li[-1])

    @staticmethod
    def shuffle():
        print('\n**********************')
        print("Shuffle list:")
        print('**********************')
        li = ["server", "pilgrim", "database", "master", "user", "stephane"]
        print(li)
        random.shuffle(li)
        print("shuffled...")
        print(li)

    @staticmethod
    def list_comprehension():
        print('\n**********************')
        print("List comprehension:")
        print('**********************')
        the_list = [i**2 for i in range(1, 11)]
        for elem in the_list:
            print(elem)

        """Return a list of the ranks, sorted with higher first."""
        mydeck = [r+s for r in '23456789TJQKA' for s in 'SHDC']
        hand = "AC 2D 4H 3D 5S".split() # Ace-Low Straight
        ranks = ['--23456789TJQKA'.index(r) for r, s in hand]
        ranks.sort(reverse=True)
        if ranks == [14, 5, 4, 3, 2]:  # special case of low-ace straight
            ranks = [5, 4, 3, 2, 1]
        print(ranks)

    @staticmethod
    def slice_list():
        print('\n**********************')
        print("Slice list:")
        print('**********************')
        li = ["server", "pilgrim", "database", "master", "user", "stephane"]
        print(li)
        print("li[1:3]: ")
        print(li[1:3])
        print("li[1:-1]: ")
        print(li[1:-1])
        print("li[0:3]: ==> lists are 0 based")
        print(li[0:3])
        print("li[:3]: ==> first 3 elements")
        print(li[:3])
        print("li[3:]: ==> last 3 elements")
        print(li[3:])
        print("li[:]: ==> another copy of the list")
        print(li[:])
        garbled = "!XeXgXaXsXsXeXmX XtXeXrXcXeXsX XeXhXtX XmXaX XI"
        print("garbled: ", garbled)
        print("garbled[::-2]: ", garbled[::-2])
        my_list = list(range(1, 11))  # List of numbers 1 - 10
        print("my_list: ", my_list)
        print("my_list[::2]: ", my_list[::2])
        backwards = my_list[::-1]
        print("backwards = my_list[::-1]: ", backwards)

    @staticmethod
    def add_elements():
        print('\n**********************')
        print("Add elements:")
        print('**********************')
        li = ["server", "pilgrim", "database", "master", "user", "stephane"]
        print(li)
        print("Append 'new'")
        li.append("new")
        print(li)
        print("Insert 'newnew'")
        li.insert(2, "newnew")
        print(li)
        print("Extend with [\"two\", \"elems\"]")
        li.extend(["two", "elems"])
        print(li)
        print("\nBeware of extend and append!!! No value is returned. Mutates the object in place")
        li = ["server", "pilgrim", "database", "master", "user", "stephane"]
        print("Extend with [\"two\", \"elems\"]")
        li.extend(["two", "elems"])
        print(li)
        li = ["server", "pilgrim", "database", "master", "user", "stephane"]
        print("Append with [\"two\", \"elems\"]")
        li.append(["two", "elems"])
        print(li)

    @staticmethod
    def search_list():
        print('\n**********************')
        print("Search elements:")
        print('**********************')
        li = ["server", "pilgrim", "database", "master", "user", "database", "stephane"]
        print(li)
        print("index of pilgrim: ")
        print(li.index("pilgrim"))
        print("\nreturns only the index of the first occurence of element in list!!!")
        print("index of database: ")
        print(li.index("database"))

    @staticmethod
    def delete_element():
        print('\n**********************')
        print("Delete elements:")
        print('**********************')
        li = ["server", "pilgrim", "database", "master", "user", "database", "stephane"]
        print(li)
        print("Delete pilgrim")
        li.remove("pilgrim")
        print(li)
        print("Delete 3rd element")
        del li[2]
        print(li)
        print("\ndeletes only the first occurence of an element in list!!!")
        print("Delete database")
        li.remove("database")
        print(li)
        print("Pop !")
        print(li.pop())
        print(li)
        print(li.pop(2))
        print(li)
        print(li.pop(li.index("server")))
        print(li)

    @staticmethod
    def list_operators():
        print('\n**********************')
        print("Operators:")
        print('**********************')
        li = ["server", "pilgrim", "database", "master", "user", "database", "stephane"]
        print(li)
        print("master in list: ")
        print("master" in li)
        print("\n!!!slower than extend!!!")
        print("li + [\"a\",\"b\",\"c\"]")
        li = li + ["a", "b", "c"]
        print(li)
        print("\n!!!equivalent to extend!!!")
        print("li += [\"d\",\"e\",\"f\"]")
        li += ["d", "e", "f"]
        print(li)
        print("\nMultiply: li = [\"1\", \"2\", \"3\"]*4")
        li = ["1", "2", "3"]*4
        print(li)

    @staticmethod
    def map():
        print('\n**********************')
        print("Map it!:")
        print('**********************')
        print("This is powerful !")
        li = [1, 3, 5, 7, 9]
        print(li)
        print([val*2 for val in li])
        print("This is poetry !")
        fragments = [
            ("La nature est un temple", "ou de vivants piliers"),
            ("Laissent parfois sortir", "de confuses paroles"),
            ("L'homme y passe a travers", "des forets de symboles"),
            ("Qui l'observent avec", "des regards familiers")
        ]
        correspondance = ["%s %s" % (s1, s2) for s1, s2 in fragments]
        for s in correspondance:
            print(s)

    @staticmethod
    def real_map():
        print('\n**********************')
        print("Built-in map function:")
        print('**********************')
        fragments = [
            "La nature est un temple", "ou de vivants piliers",
            "Laissent parfois sortir", "de confuses paroles",
            "L'homme y passe a travers", "des forets de symboles",
            "Qui l'observent avec", "des regards familiers"
        ]

        def mumble(s):
            return str.replace(s, "a", "z")
        mumbo_jumbo = map(mumble, fragments)

        for string in mumbo_jumbo:
            print(string)

    @staticmethod
    def join():
        print('\n**********************')
        print("Join it!:")
        print('**********************')
        print("This is even more powerful !")
        fragments = [
            ("La nature est un temple", "ou de vivants piliers"),
            ("Laissent parfois sortir", "de confuses paroles"),
            ("L'homme y passe a travers", "des forets de symboles"),
            ("Qui l'observent avec", "des regards familiers")
        ]
        print("\n".join(["%s %s" % (s1, s2) for s1, s2 in fragments]))

    @staticmethod
    def filter():
        print('\n**********************')
        print("Filter list:")
        print('**********************')
        li = [
            "La nature",
            "est un temple",
            "ou de vivants piliers",
            "laissent parfois sortir",
            "de confuses paroles",
            "l'homme y passe au travers",
            "des forets de symboles",
            "qui l'observent avec",
            "des regards familiers"
        ]
        print("\n".join(["%s" % elem for elem in li if "de" in elem]))

    @staticmethod
    def realfilter():
        print('\n**********************')
        print("Built-in filter function:")
        print('**********************')
        li = [
            "La nature",
            "est un temple",
            "ou de vivants piliers",
            "laissent parfois sortir",
            "de confuses paroles",
            "l'homme y passe au travers",
            "des forets de symboles",
            "qui l'observent avec",
            "des regards familiers"
        ]

        def containsi(s):
            return 'i' in s
        print('\n'.join(filter(containsi, li)))

    @staticmethod
    def sort():
        print('\n**********************')
        print("Built-in sort function:")
        print('**********************')
        li = [1, 2, 3, 3, 3, 4, 1, 2, 1, 2, 3]
        print("original:", li)
        li.sort()
        print("\nsorted:", li)
        li.sort(reverse=True)
        print("\nreverse:", li)

    @staticmethod
    def custom_sort():
        data = []
        file_path = os.path.join("c:/", "temp/", "Stocks.csv")
        with open(file_path, 'r') as qFile:
            for line in qFile:
                fields = tuple(line.strip().split(","))
                if len(fields) == 9:
                    data.append(fields)

        def price_volume(a):
            return a[1], a[8]

        data.sort(key=price_volume)
        for stock, price, date, time, change, opPrc, dHi, dLo, vol in data:
            print((stock, price, date, time, change, vol))

    @staticmethod
    def count_occurences():
        print('\n**********************')
        print("Built-in count function:")
        print('**********************')
        printed = []
        li = [1, 2, 3, 3, 3, 4, 1, 2, 1, 2, 3]
        li.sort(reverse=True)
        for elem in li:
            if elem not in printed:
                print('\nelem, nb of occurences', (elem, li.count(elem)))
                printed.append(elem)

    @staticmethod
    def traverse_list():
        print('\n**********************')
        print("Traverse list with in or range:")
        print('**********************')
        mylist = ["souvent", "pour", "s'amuser", "des", "hommes", "d'equipage"]
        for item in mylist:
            print(item,)
        print("\n")
        for i in range(len(mylist)):
            print(mylist[i],)

    @staticmethod
    def concatenate_lists():
        print('\n**********************')
        print("concatenate lists:")
        print('**********************')
        a = ["La", "Nature", "Est", "Un", "Temple"]
        b = ["Ou", "De", "Vivants", "Piliers"]
        # add lists to concatenate
        c = a + b
        print(c)
        # multiply lists
        print("\n")
        d = [a[1]]*5
        print(d)

    @staticmethod
    def enumerate_list():
        print('\n**********************')
        print("Enumerates a list:")
        print('**********************')
        mylist = ["souvent", "pour", "s'amuser", "des", "hommes", "d'equipage"]
        print(mylist)
        for index, elem in enumerate(mylist):
            print(index, elem)

    @staticmethod
    def cumulative_sum():
        print('\n**********************')
        print("Cummulative sum:")
        print('**********************')
        li = [i for i in range(21)]
        print("Original:", li)
        print("Cumulative sum:", [sum(li[0:li.index(item)+1]) for item in li])


def main():
    list_test = ListTest()

    list_test.define_list()
    list_test.shuffle()
    list_test.list_comprehension()
    list_test.slice_list()
    list_test.add_elements()
    list_test.search_list()
    list_test.delete_element()
    list_test.list_operators()
    list_test.map()
    list_test.join()
    list_test.filter()
    list_test.realfilter()
    list_test.real_map()
    list_test.sort()
    list_test.count_occurences()
    list_test.traverse_list()
    list_test.concatenate_lists()
    list_test.enumerate_list()
    list_test.cumulative_sum()

    print()
    evens_to_50 = [i for i in range(51) if i % 2 == 0]
    print(evens_to_50)

    even_squares = [i**2 for i in range(1, 11) if i % 2 == 0]
    print(even_squares)

    cubes_by_four = [i**3 for i in range(1, 11) if i**3 % 4 == 0]
    print(cubes_by_four)

    threes_and_fives = list(filter(lambda x: x % 3 == 0 or x % 5 == 0, [i for i in range(1, 16)]))
    print(threes_and_fives)


if __name__ == '__main__':
    main()
