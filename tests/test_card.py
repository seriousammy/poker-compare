from poker.card import Card


def test_card_initialize():
    card = Card('2', 'heart')
    assert card.value == '2'
    assert card.suit == 'heart'


def test_card_str():
    card = Card('3', 'clubs')
    assert str(card) == '3, clubs'
