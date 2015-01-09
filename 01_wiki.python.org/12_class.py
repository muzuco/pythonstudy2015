class BankAccount(object):
    def __init__(self, initial_balance=0):
        self.balance = initial_balance
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        self.balance -= amount
    def overdrawn(self):
        return self.balance <= 0

my_account = BankAccount(15)
while not my_account.overdrawn():
    my_account.withdraw(5)
    print 'balance :', my_account.balance
    
'''
my_account = BankAccount(15)
my_account.withdraw(5)
print my_account.balance
print my_account.overdrawn()
'''