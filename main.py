from poker.card import Card
from poker.deck import Deck
from poker.card_map import CARD_VALUES, CARD_SUITS
from poker.poker import Poker
from poker.hand import Hand


def main():
    print('Welcome to Poker Scorer')
    card_array = [Card(value, suit) for suit in CARD_SUITS for value in CARD_VALUES]
    deck = Deck(card_array)
    poker_game = Poker(deck)
    hand_1 = Hand([Card('3', 'hearts'), Card('4', 'hearts'), Card('5', 'diamonds'), Card('4', 'clubs'), Card('2', 'hearts')])
    hand_2 = Hand([Card('2', 'spades'), Card('4', 'spades'), Card('5', 'diamonds'), Card('4', 'diamonds'), Card('2', 'hearts')])

    poker_game.add_single_hand_to_game(hand_1)
    poker_game.add_single_hand_to_game(hand_2)
    print(poker_game.compare_two_hands())


if __name__ == '__main__':
    main()
