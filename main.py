from poker.card import Card
from poker.deck import Deck
from poker.card_map import CARD_VALUES, CARD_SUITS


def main():
    print('Welcome to Poker Scorer')
    card_array = [Card(value, suit) for suit in CARD_SUITS for value in CARD_VALUES]
    deck = Deck(card_array)

if __name__ == '__main__':
    main()