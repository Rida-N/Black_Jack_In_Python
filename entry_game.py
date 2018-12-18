from service.player import Player
from service.dealer import Dealer
from colorama import Fore, Style
from service import common_util


class Black_Jack():
    def __init__(self):
        print('Welcome to Black Jack!')
        self.player = Player(1000)
        print('Your initial bankroll is: ' + self.player.get_balance())
        self.dealer = Dealer()
        self.turn = 'player'
        self.init_game()

    def bet(self):
        while True:
            if self.player.withdraw(input('Please input your first bet : ')):
                break
        print('Your current bet: ' + self.player.curr_bet)

    def init_game(self, reset=False):
        self.bet()
        if reset:
            self.dealer.reset()
            self.player.reset()
        self.hit(self.turn, onetime=True)
        self.hit(self.turn, onetime=True)
        self.turn='dealer'
        self.hit(self.turn, onetime=True)
        self.hit(self.turn, onetime=True, hide=True)
        self.print_cards(first=True)
        self.turn='player'
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
                self.hit('player', onetime=True)

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

    def hit(self, player, onetime=False, hide=False):
        while not self.game_over():
            self.new_card = self.dealer.deal()
            self.sum_cards(player)
            if not hide:
                print(player + ' new card : ' + str(self.new_card))
                print(player + ' new point : ' + str(self.dealer.sum_point if player == 'dealer' else self.player.sum_point))
            if onetime == True:
                break

    '''
    check if there is a winner
    '''

    def game_over(self):
        if self.dealer.sum_point > 21:
            print('You Win! Dealer is busted!')
            self.player.deposite(self.player.curr_bet*2)
            self.check_replay()
            return True
        elif self.player.sum_point > 21:
            print('You Lost! You are busted! Game Over!')
            self.check_replay()
            return True
        elif self.player.sum_point == 21:
            if self.dealer.sum_point == 21:
                print('This is a TIE! Game Over!')
            else:
                self.player.deposite(self.player.curr_bet+self.player.curr_bet/2*3)
                print("You Win! It's a Black Jack !")
            self.check_replay()
            return True
        elif self.turn=='dealer' and self.dealer.sum_point > 16:
            if self.dealer.sum_point == self.player.sum_point:
                print('This is a TIE! Game Over!')
                self.check_replay()
                return True
            elif self.dealer.sum_point > self.player.sum_point:
                print('You Lost! Dealer won! Game Over!')
                self.check_replay()
                return True
            else:
                print('You Win! Dealer is busted!')
                self.player.deposite(self.player.curr_bet*2)
                self.check_replay()
                return True
        return False

    '''
    sum point of the player and the dealer's cards
    '''

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

    def check_replay(self):
        if self.player.get_balance() <= 0:
            print('Your deposit balance has been exhausted!')
        else:
            print('Your current bankroll is: ' + self.player.get_balance())
            print('Do you want to replay?')
            replay = input(' Yes or No:')
            if replay == 'Yes' or replay == 'yes' or replay == 'y':
                self.init_game(reset=True)
