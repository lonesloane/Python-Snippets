def iter_a_tort():
    my_dict = {
               "Name": "Lone Sloane",
               "Class": "Badass",
               "Age": 42,
               "Awesome": True
               }
    for key in my_dict:
        print key, ":", my_dict[key]

    print my_dict.keys()
    print my_dict.values()

iter_a_tort()
