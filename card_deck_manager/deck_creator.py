import itertools
import random as rnd

def create_new_deck():
    cards_of_each_type = ['joker', 'king', 'queen', 'ace', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    card_types = ['spades', 'hearts', 'diamonds', 'clubs']
    all_cards_combination = list(itertools.product(card_types, cards_of_each_type))
    return all_cards_combination

def create_new_shuffled_deck():
    new_deck = create_new_deck()
    rnd.shuffle(new_deck)
    return new_deck
