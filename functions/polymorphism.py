import functools


@functools.singledispatch
def printer(value):
    print('other: {}'.format(value))


@printer.register(str)
def str_printer(value):
    print(value)


@printer.register(int)
def int_printer(value):
    printer('int: {}'.format(value))


@printer.register(dict)
def dict_printer(value):
    printer('dict:')
    for k, v in sorted(value.items()):
        printer('	key: {}, value: {}'.format(k, v))


printer('spam')
printer([1, 2, 3])
printer(123)
printer({'a': 1, 'b': 2, 'c': 3, 'd': 4})
