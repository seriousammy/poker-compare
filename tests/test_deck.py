from poker.card import Card
from poker.deck import Deck
from poker.card_map import CARD_VALUES, CARD_SUITS


def test_deck_initialize():
    card_1 = Card('2', 'hearts')
    card_2 = Card('3', 'clubs')
    deck = Deck([card_1, card_2])
    assert card_1 in deck.deck
    assert card_2 in deck.deck


def test_deck_initalize_with_card_map():
    card_array = [Card(value, suit) for suit in CARD_SUITS for value in CARD_VALUES]
    deck = Deck(card_array)
    for card in card_array:
        assert card in deck.deck
