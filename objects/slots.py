class Hand:

    __slots__ = ('hand', 'bet')

    def __init__(self, bet, hand=None):
        self.hand = hand or []
        self.bet = bet

    def __repr__(self):
        return "{class_}({bet}, {hand})".format_map(class_=self.__class__.__name__, **vars(self))


h1 = Hand(3)
print(h1)
