class Poker:
    poker_deck = None
    hands = []

    def __init__(self, _deck):
        self.poker_deck = _deck

    def add_single_hand_to_game(self, hand):
        self.hands.append(hand)

    def get_score(self):
        hand_score = ''
        for hand in self.hands:
            hand_score += hand.get_score()
        print(hand_score)
        return hand_score
