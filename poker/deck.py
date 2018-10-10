class Deck:
    deck = []

    def __init__(self, cards):
        self.deck = cards
    
    def __str__(self):
        return str(self.deck)