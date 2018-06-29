import datetime
import pytz


class Account(object):

    @staticmethod
    def _curent_time():
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)

    def __init__(self, name, balance):
        self._name = name
        self._balance = balance
        self._transaction = []
        self._transaction.append((Account._curent_time(), balance))
        print('Account created for ' + self._name)

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            self.show_balance()
            self._transaction.append((Account._curent_time(), amount))

    def withdraw(self, amount):
        if amount >= 0 and amount < self._balance:
            self._balance -= amount
            self._transaction.append((Account._curent_time(), -amount))
        elif amount < 0:
            print("Please enter a positive amount")
        else:
            print("You do not have enough money in your account")
        self.show_balance()

    def show_balance(self):
        print("balance is {}".format(self._balance))

    def show_transaction(self):
        for (date, amount) in self._transaction:
            if amount > 0:
                tran_type = "deposited"
            else:
                tran_type = "withdrawn"
                amount *= -1
            print("{:6} on {} (local time was {})".format(amount, tran_type, date, date.astimezone()))


if __name__ == '__main__':
    tim = Account('tim', 500)
    tim.deposit(250)
    tim.deposit(50)
    tim.withdraw(34)
    tim.show_transaction()
    steph = Account('steph', 800)
    steph.deposit(200)
    steph.withdraw(50)
    steph.show_transaction()
