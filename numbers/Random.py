import random


def randomChoice():
    sequence = ["bleu", "blanc", "rouge"]
    for i in range(1,10):
        print(random.choice(sequence))

def randomRange():
    for i in range(1,10):
        print(random.randrange(0,100,5))

def randomSample():
    print random.sample(xrange(1,50), 15)

if __name__ == "__main__":
    randomChoice()
    randomRange()
    randomSample()
