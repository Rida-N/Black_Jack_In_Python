from service.player import Player
from service.dealer import Dealer
from colorama import Fore, Style
from service import common_util


class Black_Jack():
    def __init__(self):
        print('Welcome to Black Jack!')
        self.player = Player(1000)
        print('Your initial bankroll is: ' + self.player.balance)
        while True:
            self.player.curr_bet = input('Please input your first bet : ')
            if self.player.withdraw(self.player.curr_bet):
                break
        print('Your current bet: ' + self.player.curr_bet)
        self.dealer = Dealer()
        self.hit('player')
        self.hit('player')
        self.hit('dealer')
        self.hit('dealer', hide=True)
        self.print_cards(first=True)
        self.gambling()

    def print_cards(self, first=False):
        print('Your card : ' + Fore.RED + str(self.player.hand_cards) + Style.RESET_ALL)
        print("Dealer's card : " + Fore.BLUE + str((['*'] + self.dealer.hand_cards[1:]) if first else self.dealer.hand_cards))

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
            if not common_util.check_int(self.player_choice) or (self.player_choice != '1' and self.player_choice != '2'):
                print('Please input 1 or 2 and try again')
            else:
                break

    def hit(self, player, hide=False):
        while not self.game_over():
            self.new_card = self.dealer.deal()
            self.sum_cards(player)
            if not hide:
                print(player + ' new card : ' + str(self.new_card))
                print(player + ' new point : ' + str(self.dealer.sum_point if player == 'dealer' else self.player.sum_point))

    '''check if there is a winner'''

    def game_over(self):
        if self.dealer.sum_point > 21:
            print('You Win! Dealer is busted! Game Over!')
            return True
        elif self.player.sum_point > 21:
            print('You Lost! You are busted! Game Over!')
            return True
        elif self.dealer.sum_point > self.player.sum_point:
            print('You Lost! Dealer won! Game Over!')
            return True
        else:
            return False

    '''sum point of the player and the dealer's cards'''

    def sum_cards(self, player):
        new_card = self.new_card
        sum_point = self.dealer.sum_point if player == 'dealer' else self.player.sum_point
        if common_util.check_int(new_card):
            new_point = int(new_card)
        elif new_card in ['J', 'Q', 'K']:
            new_point = 10
        elif abs(sum_point + 1 - 21) < abs(sum_point + 11 - 21):
            new_point = 1
        else:
            new_point = 11
        sum_point = sum_point + new_point
        if player == 'dealer':
            self.dealer.sum_point = sum_point
            self.dealer.hand_cards.append(new_card)
        else:
            self.player.sum_point = sum_point
            self.player.hand_cards.append(new_card)
