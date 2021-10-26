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

    def __init__(self, number, balance):

        self.number = number
        self.balance = balance

        self.number = random_number_for_account()

        def add_money(amount):
            if amount >= 0:
                return amount + self.balance

        def withdraw(amount):
            if amount >= 0 and amount >= self.balance:
                return self.balance - amount


class Bank:

    def __int__(self, name, clients):

        self.name = name
        self.clients = []

        def add_clients(clientName):
            self.clients.append(clientName)

        def get_total_deposits():
            print()


class Client:




