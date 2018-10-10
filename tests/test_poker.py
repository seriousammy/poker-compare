from poker.card import Card
from poker.hand import Hand


def test_poker_game_get_score(poker_client):
    poker_client.hands = []
    hand = Hand([Card('3', 'hearts'), Card('4', 'hearts'), Card('5', 'diamonds'), Card('4', 'diamonds'), Card('2', 'hearts')])
    poker_client.add_single_hand_to_game(hand)
    hand_score = poker_client.get_score()
    assert hand_score[0]['name'] == '1 Pair'


def test_poker_game_compare_hands_second_hand_wins(poker_client):
    poker_client.hands = []
    first_hand = Hand([Card('3', 'hearts'), Card('4', 'hearts'), Card('5', 'diamonds'), Card('4', 'diamonds'), Card('2', 'hearts')])
    second_hand = Hand([Card('3', 'hearts'), Card('4', 'hearts'), Card('3', 'diamonds'), Card('4', 'hearts'), Card('2', 'hearts')])
    poker_client.add_single_hand_to_game(first_hand)
    poker_client.add_single_hand_to_game(second_hand)
    result = poker_client.compare_two_hands()
    assert result == 'Second Hand Wins'


def test_poker_game_compare_hands_first_hand_wins(poker_client):
    poker_client.hands = []
    first_hand = Hand([Card('3', 'hearts'), Card('4', 'hearts'), Card('5', 'diamonds'), Card('4', 'diamonds'), Card('2', 'hearts')])
    second_hand = Hand([Card('3', 'hearts'), Card('4', 'hearts'), Card('7', 'diamonds'), Card('9', 'hearts'), Card('2', 'hearts')])
    poker_client.add_single_hand_to_game(first_hand)
    poker_client.add_single_hand_to_game(second_hand)
    result = poker_client.compare_two_hands()
    assert result == 'First Hand Wins'


def test_poker_game_compare_hands_high_card(poker_client):
    poker_client.hands = []
    first_hand = Hand([Card('3', 'hearts'), Card('4', 'hearts'), Card('7', 'diamonds'), Card('8', 'diamonds'), Card('2', 'hearts')])
    second_hand = Hand([Card('3', 'hearts'), Card('4', 'hearts'), Card('7', 'diamonds'), Card('9', 'hearts'), Card('2', 'hearts')])
    poker_client.add_single_hand_to_game(first_hand)
    poker_client.add_single_hand_to_game(second_hand)
    result = poker_client.compare_two_hands()
    assert result == 'Second Hand Wins'


def test_poker_game_compare_hands_flush(poker_client):
    poker_client.hands = []
    first_hand = Hand([Card('3', 'hearts'), Card('4', 'hearts'), Card('7', 'hearts'), Card('8', 'hearts'), Card('2', 'hearts')])
    second_hand = Hand([Card('3', 'spades'), Card('4', 'spades'), Card('7', 'spades'), Card('9', 'spades'), Card('2', 'spades')])
    poker_client.add_single_hand_to_game(first_hand)
    poker_client.add_single_hand_to_game(second_hand)
    result = poker_client.compare_two_hands()
    assert result == 'Second Hand Wins'


def test_poker_game_compare_hands_flush_tie_breaker_high_card(poker_client):
    poker_client.hands = []
    first_hand = Hand([Card('3', 'hearts'), Card('4', 'hearts'), Card('7', 'hearts'), Card('8', 'hearts'), Card('2', 'hearts')])
    second_hand = Hand([Card('3', 'hearts'), Card('4', 'hearts'), Card('7', 'hearts'), Card('9', 'hearts'), Card('2', 'hearts')])
    poker_client.add_single_hand_to_game(first_hand)
    poker_client.add_single_hand_to_game(second_hand)
    result = poker_client.compare_two_hands()
    assert result == 'Second Hand Wins'


def test_poker_game_compare_hands_tie_breaker_royal_flush(poker_client):
    poker_client.hands = []
    first_hand = Hand([Card('A', 'hearts'), Card('K', 'hearts'), Card('Q', 'hearts'), Card('J', 'hearts'), Card('10', 'hearts')])
    second_hand = Hand([Card('A', 'spades'), Card('K', 'spades'), Card('Q', 'spades'), Card('J', 'spades'), Card('10', 'spades')])
    poker_client.add_single_hand_to_game(first_hand)
    poker_client.add_single_hand_to_game(second_hand)
    result = poker_client.compare_two_hands()
    assert result == 'Second Hand Wins'
