import random


def random_choice():
    sequence = ["bleu", "blanc", "rouge"]
    for i in range(1, 10):
        print((random.choice(sequence)))


def random_range():
    for i in range(1, 10):
        print(random.randrange(0, 100, 5))


def random_sample():
    print(random.sample(range(1, 50), 15))


if __name__ == "__main__":
    random_choice()
    random_range()
    random_sample()
