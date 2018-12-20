from service.player import Player
from service.dealer import Dealer
from colorama import Fore, Style
from service import common_util
from time import sleep


class Black_Jack():
    def __init__(self):
        print('Welcome to Black Jack!')
        self.player = Player(1000)
        print('Your initial bankroll is: ' + Fore.BLUE + str(self.player.get_balance()) + Style.RESET_ALL)
        self.dealer = Dealer()
        self.init_game()

    def bet(self):
        while True:
            if self.player.withdraw(input(Fore.GREEN + 'Please input your bet : ' + Style.RESET_ALL)):
                break
        print('Your current bet: ' + str(self.player.curr_bet))

    def init_game(self, reset=False):
        self.game_over = None
        if reset:
            self.dealer.reset()
            self.player.reset()
        self.bet()
        self.hit('dealer', print_stat='none')
        self.hit('dealer', print_stat='none')
        self.hit('player', print_stat='none')
        self.hit('player', print_stat='init')
        self.gambling()

    def print_status(self, first_time=False):
        print(Fore.GREEN + '----------------------------------------------------------' + Style.RESET_ALL)
        print(f'Your card : {Fore.RED + str(self.player.hand_cards) + Style.RESET_ALL} Your points: '
              + Fore.RED + str(self.player.sum_point) + Style.RESET_ALL)
        print("Dealer's card : " + Fore.BLUE + str((['*'] + self.dealer.hand_cards[1:]) if first_time else self.dealer.hand_cards) + (
              (Style.RESET_ALL + ' Dealer points: ' + Fore.BLUE + str(self.dealer.sum_point)) if not first_time else ''))
        print(Fore.GREEN + '----------------------------------------------------------' + Style.RESET_ALL)

    def gambling(self):
        while not self.is_game_over():
            self.make_option()
            if int(self.player_choice) == 1:
                while not self.is_game_over():
                    self.hit('dealer')
            else:
                self.hit('player')

    def make_option(self):
        print(Fore.GREEN + "What's your choice ?")
        print(Fore.BLUE + "1. STAND " + Fore.RED + "2. HIT")
        print(Style.RESET_ALL)
        while True:
            self.player_choice = input('Please input your choice (1 or 2): ')
            if not common_util.check_int(self.player_choice) or (self.player_choice != '1' and self.player_choice != '2'):
                print('Please input 1 or 2 and try again')
            else:
                break

    def hit(self, player, print_stat='norm'):
        self.turn = player
        if self.turn == 'player':
            self.player.hand_cards.append(self.dealer.deal())
        else:
            self.dealer.hand_cards.append(self.dealer.deal())
        cards = list(self.dealer.hand_cards if player == 'dealer' else self.player.hand_cards)
        ['Ace']*(cards.count('Ace') )+list(filter(lambda a:a !='Ace',cards))
        sum_point = self.sum_cards(cards)
        if player == 'dealer':
            self.dealer.sum_point = sum_point
        else:
            self.player.sum_point = sum_point
        if print_stat == 'norm':
            sleep(.5)
        print(player + ' Hitted once!')
        if not print_stat == 'none':
            self.print_status(first_time=(print_stat == 'init'))

    '''
    check if there is a winner
    '''

    def is_game_over(self):
        if self.game_over is not True:
            if self.dealer.sum_point > 21:
                print(Fore.GREEN + 'You Win! Dealer is busted!' + Style.RESET_ALL)
                self.player.deposite(self.player.curr_bet * 2)
                self.game_over = True
            elif self.player.sum_point > 21:
                print(Fore.RED + 'You Lost! You are busted! Game Over!' + Style.RESET_ALL)
                self.game_over = True
            elif self.player.sum_point == 21 or self.dealer.sum_point == 21:
                if self.player.sum_point == self.dealer.sum_point:
                    print(Fore.LIGHTCYAN_EX + 'This is a TIE! You both got a ' + 'natural' if self.game_over ==
                          None else '' + 'Black Jack! Game Over!' + Style.RESET_ALL)
                    self.player.deposite(self.player.curr_bet)
                else:
                    if self.player.sum_point == 21:
                        print(Fore.GREEN + "You Win! It's a " + 'natural' if self.game_over == None else '' + 'Black Jack !' + Style.RESET_ALL)
                        self.player.deposite(self.player.curr_bet + self.player.curr_bet / 2 * 3)
                    else:
                        print(Fore.RED + "You Lost! Dealer got a " + 'natural' if self.game_over ==
                              None else '' + 'Black Jack !' + Style.RESET_ALL)
                self.game_over = True
            elif self.turn == 'dealer' and self.dealer.sum_point > 16:
                if self.dealer.sum_point == self.player.sum_point:
                    print(Fore.LIGHTCYAN_EX + 'This is a TIE! Game Over!' + Style.RESET_ALL)
                    self.player.deposite(self.player.curr_bet)
                    self.game_over = True
                elif self.dealer.sum_point > self.player.sum_point:
                    print(Fore.RED + 'You Lost! Dealer won! Game Over!' + Style.RESET_ALL)
                    self.game_over = True
                else:
                    self.game_over = False
            if self.game_over:
                print('The final score is as below :')
                self.print_status()
                self.check_replay()
        return self.game_over

    '''
    Sum point of the player and the dealer's cards
    Do sum cards recursively
    '''

    def sum_cards(self, cards, sum_point=0):
        if cards:
            new_card = cards.pop()
            if common_util.check_int(new_card):
                new_point = int(new_card)
            elif new_card in ['J', 'Q', 'K']:
                new_point = 10
            elif sum_point + 11 <= 21:
                new_point = 11
            else:
                new_point = 1
            sum_point = sum_point + new_point
            return self.sum_cards(cards, sum_point)
        else:
            return sum_point

    def check_replay(self):
        if self.player.get_balance() <= 0:
            print('Your deposit bankroll has been exhausted!')
        else:
            print('Your current total bankroll is: ' + Fore.BLUE + str(self.player.get_balance()) + Style.RESET_ALL)
            print('Do you want to replay?')
            replay = input(Fore.RED + ' Yes ' + Fore.BLACK + 'or' + Fore.BLUE + ' No:' + Style.RESET_ALL)
            if replay == 'Yes' or replay == 'yes' or replay == 'y':
                self.init_game(reset=True)
