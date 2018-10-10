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

    def get_score(self):
        # TODO: Royal Flush
        # TODO: Straight Flush
        if self.is_four_of_a_kind():
            return "Four of a Kind"
        elif self.is_full_house():
            return "Full House"
        elif self.is_flush():
            return "Flush"
        # TODO: Straight
        elif self.is_three_of_a_kind():
            return "3 of a Kind"
        elif self.is_two_pair():
            return "2 Pair"
        elif self.is_pair():
            return "1 Pair"
        elif self.is_flush():
            return "Flush"
        else:
            return "High Card"
