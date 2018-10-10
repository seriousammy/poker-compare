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
    hand = Hand([Card('3', 'hearts'), Card('4', 'hearts'), Card('5', 'diamonds'), Card('4', 'hearts'), Card('2', 'hearts')])
    poker_game.add_single_hand_to_game(hand)
    poker_game.get_score()


if __name__ == '__main__':
    main()
