import pytest

from poker.card import Card
from poker.deck import Deck
from poker.card_map import CARD_VALUES, CARD_SUITS
from poker.poker import Poker


@pytest.fixture(scope='function')
def poker_client():
    card_array = [Card(value, suit) for suit in CARD_SUITS for value in CARD_VALUES]
    deck = Deck(card_array)
    poker_game = Poker(deck)

    yield poker_game
