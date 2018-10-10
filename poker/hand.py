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

    def is_pair(self):
        card_dict = self.convert_card_to_value_dict()
        if sorted(list(card_dict.values())) == [1, 1, 1, 2]:
            return True
        return False

    def is_two_pair(self):
        card_dict = self.convert_card_to_value_dict()
        if sorted(list(card_dict.values())) == [1, 2, 2]:
            return True
        return False

    def is_full_house(self):
        card_dict = self.convert_card_to_value_dict()
        if sorted(list(card_dict.values())) == [2, 3]:
            return True
        return False

    def get_score(self):
        if self.is_pair():
            return "1 Pair"
        elif self.is_two_pair():
            return "2 Pair"
        elif self.is_full_house():
            return "Full House"
        else:
            return "No Score"
