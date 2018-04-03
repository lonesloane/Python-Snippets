from collections import namedtuple
from typing import *
import random

Card = namedtuple('Card', ('rank', 'suit'))

SUITS = '\u2660\u2661\u2662\u2663'
Spades, Hearts, Diamonds, Clubs = SUITS

domain = [Card(r+1,s) for r in range(13) for s in SUITS]


# Extension (aggregation here, but could be composition)
# aggregation => The objects being wrapped have an independent
# existence from the wrapper.
class Deck_Wrapper:

    def __init__(self, cards:List[Card]):
        self.cards = cards.copy()
        self.deal_iter = iter(self.cards)

    def shuffle(self):
        random.shuffle(self.cards)
        self.deal_iter = iter(self.cards)

    def deal(self) -> Card:
        return next(self.deal_iter)


# Inheritance
class Deck_Inherit(list):

    def shuffle(self):
        random.shuffle(self)
        self.deal_iter = iter(self)

    def deal(self) -> Card:
        return next(self.deal_iter)


#print(Card(2, Hearts))
#print(domain)
deck = Deck_Wrapper(domain)
deck.shuffle()
print([deck.deal() for _ in range(5)])

deck = Deck_Inherit(Card(r+1, s) for r in range(13) for s in SUITS)
deck.shuffle()
print([deck.deal() for _ in range(5)])