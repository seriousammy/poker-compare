CARD_VALUES = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
CARD_SUITS = ['spades', 'hearts', 'clubs', 'diamonds']
CARD_VALUE_SCORING_MAP = {
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'J': 11,
    'Q': 12,
    'K': 13,
    'A': 14
}
CARD_SUITS_SCORING_MAP = {
    'diamonds': 0,
    'clubs': 1,
    'hearts': 2,
    'spades': 3
}
CARD_VALUE_RANK = {
    'high_card': {
        'value': 0,
        'name': 'High Card'
    },
    'one_pair': {
        'value': 1,
        'name': '1 Pair'
    },
    'two_pair': {
        'value': 2,
        'name': '2 Pair'
    },
    'three_of_a_kind': {
        'value': 3,
        'name': '3 of a Kind'
    },
    'straight': {
        'value': 4,
        'name': 'Straight'
    },
    'flush': {
        'value': 5,
        'name': 'Flush'
    },
    'full_house': {
        'value': 6,
        'name': 'Full House'
    },
    'four_of_a_kind': {
        'value': 7,
        'name': 'Four of a Kind'
    },
    'straight_flush': {
        'value': 8,
        'name': 'Straight Flush'
    },
    'royal_flush': {
        'value': 9,
        'name': 'Royal Flush'
    }
}
