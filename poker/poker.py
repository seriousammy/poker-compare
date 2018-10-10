from poker.card_map import CARD_VALUE_RANK, CARD_SUITS_SCORING_MAP


class Poker:
    poker_deck = None
    hands = []

    def __init__(self, _deck):
        self.poker_deck = _deck

    def add_single_hand_to_game(self, hand):
        self.hands.append(hand)

    def get_score(self):
        hand_score = []
        for hand in self.hands:
            hand_score.append(hand.get_score())
        return hand_score

    def tie_breaker_for_straight_or_high_card(self):
        first_hand_high_card = self.hands[0].get_hand_high_card()
        second_hand_high_card = self.hands[1].get_hand_high_card()
        return 'First Hand Wins' if first_hand_high_card > second_hand_high_card else 'Second Hand Wins'

    def tie_breaker_for_flush(self):
        first_hand_suit = self.hands[0].get_first_card_suit()
        second_hand_suit = self.hands[1].get_first_card_suit()
        if CARD_SUITS_SCORING_MAP[first_hand_suit] > CARD_SUITS_SCORING_MAP[second_hand_suit]:
            return 'First Hand Wins'
        elif CARD_SUITS_SCORING_MAP[first_hand_suit] < CARD_SUITS_SCORING_MAP[second_hand_suit]:
            return 'Second Hand Wins'
        else:
            return self.tie_breaker_for_straight_or_high_card()

    def tie_breaker_for_pair(self):
        first_hand_high_pair = self.hands[0].get_hand_high_pair()
        second_hand_high_pair = self.hands[1].get_hand_high_pair()
        if first_hand_high_pair > second_hand_high_pair:
            return 'First Hand Wins'
        elif first_hand_high_pair > second_hand_high_pair:
            return 'Second Hand Wins'

    def determine_tie_breaker(self, hand_score):
        if hand_score['value'] in [CARD_VALUE_RANK['straight']['value'], CARD_VALUE_RANK['high_card']['value']]:
            return self.tie_breaker_for_straight_or_high_card()
        elif hand_score['value'] in [CARD_VALUE_RANK['straight_flush']['value'], CARD_VALUE_RANK['flush']['value'], CARD_VALUE_RANK['royal_flush']['value']]:
            return self.tie_breaker_for_flush()
        elif hand_score['value'] in [CARD_VALUE_RANK['one_pair']['value'], CARD_VALUE_RANK['two_pair']['value']]:
            return self.tie_breaker_for_pair()

    def rank_score_of_two_hands(self, first_hand_score, second_hand_score):
        if first_hand_score['value'] > second_hand_score['value']:
            return 'First Hand Wins'
        elif first_hand_score['value'] < second_hand_score['value']:
            return 'Second Hand Wins'
        else:
            return self.determine_tie_breaker(first_hand_score)

    def compare_two_hands(self):
        if len(self.hands) != 2:
            return 'Two hands were not given. {}'.format(self.hands)
        first_hand = self.hands[0]
        second_hand = self.hands[1]

        first_hand_score = first_hand.get_score()
        second_hand_score = second_hand.get_score()

        result_string = self.rank_score_of_two_hands(first_hand_score, second_hand_score)
        return result_string
