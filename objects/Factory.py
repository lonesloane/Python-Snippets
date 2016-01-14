class Card(object):
    """A standard playing card for Blackjack."""
    def __init__(self, r, s):
        self.rank, self.suit = r, s
        self.pval = r

    def __str__(self):
        return "%2d%s" % (self.rank, self.suit)

    def get_hard_value(self):
        return self.pval

    def get_soft_value(self):
        return self.pval


class FaceCard(Card):
    """A 10 points face card: J, Q, K."""
    def __init__(self, r, s):
        Card.__init__(r, s)
        self.pval = 10

    def __str__(self):
        label = ("J", "Q", "K")[self.rank-11]
        return "%2s%s" % (label, self.suit)


class Ace(Card):
    """An Ace: either 1 or 11 points."""
    def __str__(self):
        return "%2s%s" % ("A", self.suit)

    def get_hard_value(self):
        return 1

    def get_soft_value(self):
        return 11


class CardFactory(object):
    @staticmethod
    def new_card(rank, suit):
        if rank == 1:
            return Ace(rank, suit)
        elif rank in [11, 12, 13]:
            return FaceCard(rank, suit)
        else:
            return Card(rank, suit)


class CardDealer(object):
    def __init__(self):
        self.cards = []

    def deal(self):
        for c in self.shuffle():
            yield c

    def shuffle(self):
        raise NotImplementedError


class Deck(CardDealer):
    """A deck of cards."""
    def __init__(self):
        CardDealer.__init__(self)
        factory = CardFactory()
        self.cards = [factory.new_card(rank+1, suit)
                      for suit in ("C", "D", "H", "S")
                      for rank in range[13]
                      ]
        """
        for suit in ("C", "D", "H", "S"):
            self.cards += [Card(r,suit) for r in range(2,11)]
            self.cards += [FaceCard(r, suit) for r in range(11, 14)]
            self.cards += [Ace(1,suit)]
        """
