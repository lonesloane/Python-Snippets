from collections import namedtuple

Card = namedtuple('Card', ('rank', 'suit'))

SUITS = '\u2660\u2661\u2662\u2663'

Spades, Hearts, Diamonds, Clubs = SUITS

print(Card(2, Hearts))