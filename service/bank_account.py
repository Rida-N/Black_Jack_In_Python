from service import common_util


class Bank_Account():
    def __init__(self, balance=0):
        self.balance = 0

    def deposite(self, money):
        if int(money) and money > 0:
            self.balance = self.balance + money
            return True
        else:
            return False

    def withdraw(self, money):
        if not common_util.check_int(money):
            return False
        if int(money) and money > 0:
            self.balance = self.balance - money
            if self.balance < 0:
                print('Your balance is insufficient，only ' + str(self.balance) + ' left.')
                return False
            print('Your current total balance: ' + str(self.balance))
            return True
        else:
            print('Incorrect money number!')
            return False
