import random

SUITS = '\u2660\u2661\u2662\u2663'
Spades, Hearts, Diamonds, Clubs = SUITS


class Card:

    __slots__ = ('rank', 'suit')

    def __init__(self, rank, suit):
        super().__init__()
        self.rank = rank
        self.suit = suit

    def __repr__(self):
        return "{rank:2d} {suit}".format(rank=self.rank, suit=self.suit)


# Inherited classes
class AceCard(Card):

    def __repr__(self):
        return " A {suit}".format(rank=self.rank, suit=self.suit)


class FaceCard(Card):

    def __repr__(self):
        names = {11: 'J', 12: 'Q', 13: 'K'}
        return " {name} {suit}".format(rank=self.rank, suit=self.suit,name=names[self.rank])


# Mixin superclass
class CribbagePoints:
    def points(self):
        return self.rank


# Mixin subclasses
class CribbageFacePoints(CribbagePoints):
    def points(self):
        return 10


# Actual class definitions(inheritance + mixin)
class CribbageAce(AceCard, CribbagePoints):
    pass


class CribbageCard(Card, CribbagePoints):
    pass


class CribbageFace(FaceCard, CribbageFacePoints):
    pass


# Factory
def make_card(rank, suit):
    if rank == 1: return CribbageAce(rank, suit)
    if 2 <= rank < 11: return CribbageCard(rank, suit)
    if 11 <= rank: return CribbageFace(rank, suit)


deck = [make_card(rank+1, suit) for rank in range(13) for suit in SUITS]
random.shuffle(deck)
print(deck[:5])
print('points: {}'.format(sum(c.points() for c in deck[:5])))