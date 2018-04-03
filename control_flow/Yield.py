
def count_reds(a_list):
    count = 0
    for color in a_list:
        if color == 'black':
            yield count
            count += 0
        else:
            count += 1
    yield count


if __name__ == "__main__":
    my_list = ["red", "black", "blue", "white", "black"]
    print(count_reds(my_list).__next__())
    print(count_reds(my_list).__next__())
