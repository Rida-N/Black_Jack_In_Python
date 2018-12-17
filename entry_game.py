from service import bank_account
from service.dealer import Dealer
from colorama import Fore, Style


class Black_Jack():
    def __init__(self):
        print('Welcome to Black Jack!')
        self.player_bankroll = bank_account.Bank_Account(1000)
        print('Your initial bankroll is: ' + self.player_bankroll)
        while True:
            self.player_curr_bet = input('Please input your first bet : ')
            if self.player_bankroll.withdraw(self.player_curr_bet):
                break
        print('Your current bet: ' + self.player_curr_bet)
        self.dealer = Dealer()
        self.player_cards = []
        self.dealer_cards = []
        self.player_cards.append(self.dealer.deal())
        self.player_cards.append(self.dealer.deal())
        self.dealer_cards.append(self.dealer.deal())
        self.dealer_cards.append(self.dealer.deal())
        self.print_cards('first'=True)
        self.gambling()

    def print_cards(self, first=false):
        print('Your card : ' + Fore.RED + str(self.player_cards) + Style.RESET_ALL)
        print("Dealer's card : " + Fore.BLUE + str((['*'] + self.dealer_cards[1:]) if first else self.dealer_cards))

    def gambling(self):
        while not self.game_over():
            self.make_option()
            if int(self.player_choice) == 1:
                self.hit('dealer')
            else:
                self.hit('player')

    def make_option(self):
        print("What's your choice ?")
        print(Fore.RED + "1. STAND" + Fore.BLUE + "2. HIT")
        print(Style.RESET_ALL)
        while True:
            self.player_choice = input('Please input your choice (1 or 2): ')
            if self.player_choice != '1' and self.player_choice != '2':
                print('Please input 1 or 2 and try again')
            else:
                break

    def hit(player):
        while not self.game_over():
            if player == 'dealer':
                self.dealer_cards.append(self.dealer.deal())
            else:
                self.player_cards.append(self.dealer.deal())

    def game_over():
        # sum point of the player and the dealer's cards
        player_cards_copy = self.player_cards;
        for card in player_cards_copy:
            if 
        # check if there is a winner
