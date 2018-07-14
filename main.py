from distribute_cards import player1, player2, player3, player4
import random as rnd


def get_the_biggest_card(running_pit):

    card_precedence = {'2': 2,
                       '3': 3,
                       '4': 4,
                       '5': 5,
                       '6': 6,
                       '7': 7,
                       '8': 8,
                       '9': 9,
                       '10': 10,
                       'joker': 11,
                       'queen': 12,
                       'king': 13,
                       'ace': 14
                       }

    biggest_nmbr = 0
    running_biggest_card = ()

    for card in running_pit:
        if card_precedence.get(card[1]) > biggest_nmbr and running_pit[0][0] == card[0]:
            biggest_nmbr = card_precedence.get(card[1])
            running_biggest_card = card

    if running_pit[0][0] != 'spades':
        biggest_nmbr = 0
        for card in running_pit:
            if 'spades' in card:
                if card_precedence.get(card[1]) > biggest_nmbr:
                    biggest_nmbr = card_precedence.get(card[1])
                    running_biggest_card = card

    return running_biggest_card


def get_perfect_card(avilable_cards):
    pass


def get_card_from_players(plyr, card):

    for item in plyr:
        if card in item:
            plyr.remove(item)
            return item

    c = rnd.choice(plyr)
    plyr.remove(c)
    return c


this_pit = list()

for _ in range(13):
    rnd.shuffle(player1)
    running_card = rnd.choice(player1)
    player1.remove(running_card)
    this_pit.append(running_card)

    this_pit.append(get_card_from_players(player2, running_card[0]))
    this_pit.append(get_card_from_players(player3, running_card[0]))
    this_pit.append(get_card_from_players(player4, running_card[0]))

    print('-----------')
    print(this_pit)

    biggest_card = get_the_biggest_card(this_pit)
    print("Winner is Player-{} with Cards {}".format(this_pit.index(biggest_card) + 1, biggest_card))
    this_pit.clear()


# TODO: 1. Trump Card (Done!) , 2. Card sacrificing ( smaller in case no bigger card is available )
