from poker.card_map import CARD_VALUE_SCORING_MAP, CARD_VALUE_RANK


class Hand:
    hand = []

    def __init__(self, _hand):
        self.hand = _hand

    def convert_card_to_value_dict(self):
        card_dict = {}
        for card in self.hand:
            try:
                card_dict[card.value] += 1
            except KeyError:
                card_dict.update({card.value: 1})
        return card_dict

    def convert_card_to_suit_dict(self):
        card_dict = {}
        for card in self.hand:
            try:
                card_dict[card.suit] += 1
            except KeyError:
                card_dict.update({card.suit: 1})
        return card_dict

    def convert_card_to_value_score_list(self):
        card_list = []
        for card in self.hand:
            card_list.append(CARD_VALUE_SCORING_MAP[card.value])
        return card_list

    def get_first_card_suit(self):
        return self.hand[0].suit

    def get_hand_high_card(self):
        card_value_score_list = self.convert_card_to_value_score_list()
        card_value_score_list_max = max(card_value_score_list)
        for k, v in CARD_VALUE_SCORING_MAP.items():
            if v == card_value_score_list_max:
                return v

    def is_four_of_a_kind(self):
        card_value_dict = self.convert_card_to_value_dict()
        if sorted(list(card_value_dict.values())) == [1, 4]:
            return True
        return False

    def is_three_of_a_kind(self):
        card_value_dict = self.convert_card_to_value_dict()
        if sorted(list(card_value_dict.values())) == [1, 1, 3]:
            return True
        return False

    def is_pair(self):
        card_value_dict = self.convert_card_to_value_dict()
        if sorted(list(card_value_dict.values())) == [1, 1, 1, 2]:
            return True
        return False

    def is_two_pair(self):
        card_value_dict = self.convert_card_to_value_dict()
        if sorted(list(card_value_dict.values())) == [1, 2, 2]:
            return True
        return False

    def is_full_house(self):
        card_value_dict = self.convert_card_to_value_dict()
        if sorted(list(card_value_dict.values())) == [2, 3]:
            return True
        return False

    def is_flush(self):
        card_suit_dict = self.convert_card_to_suit_dict()
        if len(card_suit_dict) == 1:
            return True
        return False

    def is_straight(self):
        card_value_score_list = self.convert_card_to_value_score_list()
        card_value_score_list_max = max(card_value_score_list)
        card_value_score_list_min = min(card_value_score_list)
        if sorted(card_value_score_list) == [x for x in range(card_value_score_list_min, card_value_score_list_max + 1)]:
            return True
        elif sorted(card_value_score_list) == [CARD_VALUE_SCORING_MAP['2'], CARD_VALUE_SCORING_MAP['3'], CARD_VALUE_SCORING_MAP['4'], CARD_VALUE_SCORING_MAP['5'], CARD_VALUE_SCORING_MAP['A']]:
            return True
        return False

    def is_royal_flush(self):
        card_value_score_list = self.convert_card_to_value_score_list()
        if sorted(card_value_score_list) == [x for x in range(CARD_VALUE_SCORING_MAP['10'], CARD_VALUE_SCORING_MAP['A'] + 1)] and self.is_flush():
            return True
        return False

    def get_score(self):
        card_score = CARD_VALUE_RANK['high_card']
        if self.is_royal_flush():
            card_score = CARD_VALUE_RANK['royal_flush']
        elif self.is_straight() and self.is_flush():
            card_score = CARD_VALUE_RANK['straight_flush']
        elif self.is_four_of_a_kind():
            card_score = CARD_VALUE_RANK['four_of_a_kind']
        elif self.is_full_house():
            card_score = CARD_VALUE_RANK['full_house']
        elif self.is_flush():
            card_score = CARD_VALUE_RANK['flush']
        elif self.is_straight():
            card_score = CARD_VALUE_RANK['straight']
        elif self.is_three_of_a_kind():
            card_score = CARD_VALUE_RANK['three_of_a_kind']
        elif self.is_two_pair():
            card_score = CARD_VALUE_RANK['two_pair']
        elif self.is_pair():
            card_score = CARD_VALUE_RANK['one_pair']
        return card_score
