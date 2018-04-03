def iter_a_tort():
    my_dict = {
               "Name": "Lone Sloane",
               "Class": "Badass",
               "Age": 42,
               "Awesome": True
               }

    print('old fashioned way...')
    for key in my_dict:
        print(key, ":", my_dict[key])

    print('\nbetter way...')
    for k, v in my_dict.items():
        print('{k}: {v}'.format(k=k, v=v))

    print('\nKeys: {k}'.format(k=my_dict.keys()))
    print('Values: {v}'.format(v=my_dict.values()))


list = [1, 2, 3, 4, 5, 6, 7, 8, 9]


iter = list.__iter__()

print(iter.__next__())
print(iter.__next__())
print(iter.__next__())
print(iter.__next__())

# TODO: fix this
iter_a_tort()
