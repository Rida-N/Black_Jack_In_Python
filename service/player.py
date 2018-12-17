from service import common_util


class Player():

    def __init__(self, balance=0):
        self.balance = 0
        self.curr_bet = 0
        self.hand_cards = []
        self.sum_point = 0

    def deposite(self, money):
        if common_util.check_int(money) and int(money) > 0:
            self.balance = self.balance + int(money)
            return True
        else:
            print('Incorrect money number!')
            return False

    def withdraw(self, money):
        if common_util.check_int(money) and int(money) > 0:
            self.balance = self.balance - int(money)
            if self.balance < 0:
                print('Your balance is insufficient，only ' + str(self.balance) + ' left.')
                return False
            print('Your current total balance: ' + str(self.balance))
            return True
        else:
            print('Incorrect money number!')
            return False

    def reset(self):
        self.curr_bet = 0
        self.hand_cards = []
        self.sum_point = 0
