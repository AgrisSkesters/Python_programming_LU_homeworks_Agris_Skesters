import random

def random_number_for_account ():
    emtyList = []
    i = 0

    while i < 21:
        emtyList.append(random.randrange(1,9))
        i +=1
    else:
        randomNumber = "".join((str(e) for e in emtyList))

    return randomNumber


class Account:

    balanceList = [0]

    def __init__(self):
        self.personalBalanceList = []
        self.number = random_number_for_account()

    def add_money(self, amount):
        if amount >= 0:
            Account.balanceList.append(amount)
            self.personalBalanceList.append(amount)
            return print(f"added {amount}")

    def withdraw(self, amount):
        if 0 <= amount <= sum(self.personalBalanceList):
            addingSign = -amount
            Account.balanceList.append(addingSign)
            self.personalBalanceList.append(addingSign)
            return print(f"withdraw {amount}")
        else:
            print("Can't withdraw the money!")

    def balance(self):
        print(sum(self.personalBalanceList))


class Bank:

    clients = []

    def __init__(self, name):
        self.name = name

    def add_clients(self, clientName):
        Bank.clients.append(clientName)

    def get_total_deposits(self):
        print(sum(Account.balanceList))


class Client:

    def __init__(self, name):
        self.accountsList = []
        self.name = name

    def add_account(self, accountName):
        self.accountsList.append(accountName)


banka = Bank("Jauna Banka")

aldis = Client("Aldis")
zane =Client("Zane")

banka.add_clients(aldis.name)
banka.add_clients(zane.name)
print(banka.clients)

account_1 = Account()
print(account_1.number)
aldis.add_account(account_1.number)

account_1.add_money(500)
account_1.withdraw(400)
account_1.balance()

account_2 = Account()
aldis.add_account(account_2.number)
account_2.add_money(20)
account_2.balance()
print(aldis.accountsList)
banka.get_total_deposits()