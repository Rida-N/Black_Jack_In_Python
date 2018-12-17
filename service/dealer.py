from random import shuffle


class Dealer():
    card_decks = []
    hand_cards = []
    sum_point = 0

    def __init__(self):
        Dealer.card_decks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'] * 3
        print('Card decks being initialized!')
        shuffle(Dealer.card_decks)

    def deal(self):
        return Dealer.card_decks.pop()
