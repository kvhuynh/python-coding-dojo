class BankAccount():

    all_accounts = []

    def __init__(self, interest_rate=0.01, balance=0):
        self.balance = balance
        self.interest_rate = interest_rate
        BankAccount.all_accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance < amount:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        else:
            self.balance -= amount
        return self

    def display_account_info(self):
        print(self.balance)
        return self

    def yield_interest(self):
        self.balance += self.balance * self.interest_rate
        return self

    @classmethod
    def print_bank_account(cls):
        for account in cls.all_accounts:
            account.display_account_info()
        

bank_1 = BankAccount()
bank_1.deposit(500).deposit(100).deposit(300).yield_interest().display_account_info()

bank_2 = BankAccount().deposit(500).deposit(100).withdraw(200).withdraw(100).withdraw(100).withdraw(100).yield_interest().display_account_info()

print(bank_2.print_bank_account())