from poker.card import Card
from poker.hand import Hand


def test_hand_initialize():
    hand = Hand([Card('3', 'hearts'), Card('6', 'hearts'), Card('5', 'diamonds'), Card('4', 'hearts'), Card('2', 'hearts')])
    hand_score = hand.get_score()
    assert hand_score == 'High Card'


def test_one_pair_hand():
    hand = Hand([Card('3', 'hearts'), Card('4', 'hearts'), Card('5', 'diamonds'), Card('4', 'hearts'), Card('2', 'hearts')])
    hand_score = hand.get_score()
    assert hand_score == '1 Pair'


def test_two_pair_hand():
    hand = Hand([Card('3', 'hearts'), Card('4', 'diamonds'), Card('2', 'diamonds'), Card('4', 'hearts'), Card('2', 'hearts')])
    hand_score = hand.get_score()
    assert hand_score == '2 Pair'


def test_three_of_a_kind():
    hand = Hand([Card('3', 'hearts'), Card('4', 'diamonds'), Card('4', 'spades'), Card('4', 'hearts'), Card('2', 'hearts')])
    hand_score = hand.get_score()
    assert hand_score == '3 of a Kind'


def test_flush():
    hand = Hand([Card('3', 'hearts'), Card('4', 'hearts'), Card('2', 'hearts'), Card('7', 'hearts'), Card('8', 'hearts')])
    hand_score = hand.get_score()
    assert hand_score == 'Flush'


def test_four_of_a_kind():
    hand = Hand([Card('3', 'hearts'), Card('3', 'diamonds'), Card('3', 'clubs'), Card('3', 'spades'), Card('2', 'hearts')])
    hand_score = hand.get_score()
    assert hand_score == 'Four of a Kind'
