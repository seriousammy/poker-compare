class Card:
    value = None
    suit = None

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __str__(self):
        return '{}, {}'.format(self.value, self.suit)