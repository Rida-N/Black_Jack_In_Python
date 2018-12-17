from random import shuffle
class Dealer():
    cards = []

    def __init__(self):
        self.cards = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']*3
        print('Cards being initialized!')
        shuffle(self.cards)

    def deal(self):
        return self.cards.pop()