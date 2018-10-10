from poker.card import Card
from poker.hand import Hand


def poker_game_get_score(poker_client):
    hand = Hand([Card('3', 'hearts'), Card('4', 'hearts'), Card('5', 'diamonds'), Card('4', 'hearts'), Card('2', 'hearts')])
    poker_client.add_single_hand_to_game(hand)
    hand_score = poker_client.get_score()
    assert hand_score == '1 Pair'
