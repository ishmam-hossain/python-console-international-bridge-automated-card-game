import itertools
import random as rnd


def make_all_combination_of_cards():
    all_unq_cards = ['joker', 'king', 'queen', 'ace', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    card_types = ['spades', 'hearts', 'diamonds', 'clubs']
    all_combination = list(itertools.product(card_types, all_unq_cards))
    rnd.shuffle(all_combination)
    return all_combination


def distribute_cards(all_cards_combo):
    player1 = all_cards_combo[:13]
    player2 = all_cards_combo[13:26]
    player3 = all_cards_combo[26:39]
    player4 = all_cards_combo[39:52]

    return player1, player2, player3, player4


all_cards_combination = make_all_combination_of_cards()
player1, player2, player3, player4 = distribute_cards(all_cards_combination)




