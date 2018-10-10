from poker.card import Card
from poker.hand import Hand


def test_hand_initialize():
    hand = Hand([Card('3', 'hearts'), Card('10', 'hearts'), Card('5', 'diamonds'), Card('4', 'hearts'), Card('2', 'hearts')])
    hand_score = hand.get_score()
    assert hand_score['name'] == 'High Card'


def test_one_pair_hand():
    hand = Hand([Card('3', 'hearts'), Card('4', 'hearts'), Card('5', 'diamonds'), Card('4', 'hearts'), Card('2', 'hearts')])
    hand_score = hand.get_score()
    assert hand_score['name'] == '1 Pair'


def test_two_pair_hand():
    hand = Hand([Card('3', 'hearts'), Card('4', 'diamonds'), Card('2', 'diamonds'), Card('4', 'hearts'), Card('2', 'hearts')])
    hand_score = hand.get_score()
    assert hand_score['name'] == '2 Pair'


def test_three_of_a_kind():
    hand = Hand([Card('3', 'hearts'), Card('4', 'diamonds'), Card('4', 'spades'), Card('4', 'hearts'), Card('2', 'hearts')])
    hand_score = hand.get_score()
    assert hand_score['name'] == '3 of a Kind'


def test_flush():
    hand = Hand([Card('3', 'hearts'), Card('4', 'hearts'), Card('2', 'hearts'), Card('7', 'hearts'), Card('8', 'hearts')])
    hand_score = hand.get_score()
    assert hand_score['name'] == 'Flush'


def test_four_of_a_kind():
    hand = Hand([Card('3', 'hearts'), Card('3', 'diamonds'), Card('3', 'clubs'), Card('3', 'spades'), Card('2', 'hearts')])
    hand_score = hand.get_score()
    assert hand_score['name'] == 'Four of a Kind'


def test_straight():
    hand = Hand([Card('2', 'hearts'), Card('3', 'diamonds'), Card('4', 'clubs'), Card('5', 'spades'), Card('6', 'hearts')])
    hand_score = hand.get_score()
    assert hand_score['name'] == 'Straight'


def test_straight_flush():
    hand = Hand([Card('2', 'hearts'), Card('3', 'hearts'), Card('4', 'hearts'), Card('5', 'hearts'), Card('6', 'hearts')])
    hand_score = hand.get_score()
    assert hand_score['name'] == 'Straight Flush'


def test_straight_ace_low():
    hand = Hand([Card('A', 'hearts'), Card('2', 'diamonds'), Card('4', 'clubs'), Card('5', 'spades'), Card('3', 'hearts')])
    hand_score = hand.get_score()
    assert hand_score['name'] == 'Straight'


def test_straight_ace_high():
    hand = Hand([Card('A', 'hearts'), Card('K', 'diamonds'), Card('Q', 'clubs'), Card('J', 'spades'), Card('10', 'hearts')])
    hand_score = hand.get_score()
    assert hand_score['name'] == 'Straight'


def test_royal_flush():
    hand = Hand([Card('A', 'hearts'), Card('K', 'hearts'), Card('Q', 'hearts'), Card('J', 'hearts'), Card('10', 'hearts')])
    hand_score = hand.get_score()
    assert hand_score['name'] == 'Royal Flush'
