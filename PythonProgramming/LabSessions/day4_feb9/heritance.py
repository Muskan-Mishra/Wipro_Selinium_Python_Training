class SavingsAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Deposited:", amount)
            print("Balance:", self.balance)

class InterestAccount(SavingsAccount):
    def addinterest(self, rate):
        interest = self.balance * rate / 100
        self.balance += interest
        print("Interest Added:", interest)
        print("Balance:", self.balance)

obj = InterestAccount(1000)
obj.deposit(500)
obj.addinterest(7)

#multi level
class Account:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)
        print("Balance:", self.balance)


# Child class (Level 2)
class SavingsAccount(Account):
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawn:", amount)
            print("Balance:", self.balance)
        else:
            print("Insufficient Balance")


# Child class (Level 3)
class InterestAccount(SavingsAccount):
    def addinterest(self, rate):
        interest = self.balance * rate / 100
        self.balance += interest
        print("Interest Added:", interest)
        print("Balance:", self.balance)


# Main program
obj = InterestAccount(1000)
obj.deposit(500)      # from Account
obj.withdraw(300)     # from SavingsAccount
obj.addinterest(5)    # from InterestAccount