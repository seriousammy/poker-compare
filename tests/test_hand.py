from poker.card import Card
from poker.hand import Hand


def test_hand_initialize():
    hand = Hand([Card('3', 'hearts'), Card('6', 'hearts'), Card('5', 'diamonds'), Card('4', 'hearts'), Card('2', 'hearts')])
    hand_score = hand.get_score()
    assert hand_score == 'No Score'


def test_one_pair_hand():
    hand = Hand([Card('3', 'hearts'), Card('4', 'hearts'), Card('5', 'diamonds'), Card('4', 'hearts'), Card('2', 'hearts')])
    hand_score = hand.get_score()
    assert hand_score == '1 Pair'


def test_two_pair_hand():
    hand = Hand([Card('3', 'hearts'), Card('4', 'diamonds'), Card('2', 'diamonds'), Card('4', 'hearts'), Card('2', 'hearts')])
    hand_score = hand.get_score()
    assert hand_score == '2 Pair'
