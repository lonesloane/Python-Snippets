import random


def forLoop():
    for i in range(100):
        d1 = random.randrange(6)+1
        d2 = random.randrange(6)+1
        print("d1+d2: ",d1+d2)


def whileLoop():
    s,r=0,0
    while r != 100:
        d1,d2 = random.randrange(6)+1, random.randrange(6)+1
        s,r = s+d1+d2, r+1
    print("average dice roll: ", s/r)

if __name__ == "__main__":
    forLoop()
    whileLoop()