import random

# random.seed(113)

def die(sides=6):
    return random.randint(1, sides)


def dice(n=2, sides=6):
    return tuple(die(sides) for _ in range(n))


def craps():
    return dice()


def zonk():
    return dice(6)


def dungeons_dragons():
    return dice(n=1, sides=24)


print('dice(): {}'.format(dice()))
print('dice(1): {}'.format(dice(1)))
print('dice(2): {}'.format(dice(2)))
print('craps: {}'.format(craps()))
print('craps: {}'.format(craps()))
print('zonk: {}'.format(zonk()))
print('dungeons & dragons: {}'.format(dungeons_dragons()))