from service import common_util


class Player():

    def __init__(self, balance=0):
        self.__balance = balance
        self.curr_bet = 0
        self.hand_cards = []
        self.sum_point = 0

    def get_balance(self):
        return self.__balance

    def deposite(self, money):
        if common_util.check_int(money) and int(money) > 0:
            self.__balance = self.__balance + int(money)
            return True
        else:
            print('Incorrect money number!')
            return False

    def withdraw(self, money):
        if common_util.check_int(money) and int(money) > 0:
            self.__balance = self.__balance - int(money)
            if self.__balance < 0:
                print('Your bankroll is insufficient，only ' + str(self.__balance) + ' left.')
                return False
            self.curr_bet = int(money)
            print('Your current total bankroll: ' + str(self.__balance))
            return True
        else:
            print('Incorrect money number!')
            return False

    def reset(self):
        self.curr_bet = 0
        self.hand_cards = []
        self.sum_point = 0
