

def distribute_cards_from_full_deck(card_deck):
    player1 = card_deck[:13]
    player2 = card_deck[13:26]
    player3 = card_deck[26:39]
    player4 = card_deck[39:52]

    return player1, player2, player3, player4
