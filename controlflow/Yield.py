

def count_reds(a_list):
    count = 0
    for color, number in a_list:
        if color == 'black':
            yield count
            count = 0
        else:
            count += 1
    yield count

if __name__ == "__main__":
    my_list = {"red": 1, "blue": 2, "white": 3, "black": 4}
    print count_reds(my_list)
