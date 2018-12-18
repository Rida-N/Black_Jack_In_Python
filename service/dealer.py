from random import shuffle


class Dealer():
    card_decks = []

    def __init__(self):
        self.shuffle_cards()
        self.hand_cards = []
        self.sum_point = 0

    def shuffle_cards(self):
        Dealer.card_decks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'] * 4 * 2
        print('Card decks being initialized!')
        shuffle(Dealer.card_decks)

    def deal(self):
        return Dealer.card_decks.pop()

    def reset(self):
        self.check_shuffle()
        self.hand_cards = []
        self.sum_point = 0

    def check_shuffle(self):
        if len(Dealer.card_decks) < 52:
            self.shuffle_cards()
