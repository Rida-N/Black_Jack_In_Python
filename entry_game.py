from service import bank_account
from service import deal_out

class Black_Jack():
    def __init__(self):
        print('Welcome to Black Jack!')
        self.user_bankroll = bank_account.Bank_Account(1000)
        while True:
            self.user_bankroll.withdraw = input('Please input your first bet')
            if self.user_bankroll.withdraw:
                break
