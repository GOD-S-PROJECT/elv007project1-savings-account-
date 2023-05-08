class SavingsAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposit successful. New balance is:", self.balance)

    def withdraw(self, amount):
        if amount > self.balance:
            print("Withdrawal failed. Insufficient balance.")
        else:
            self.balance -= amount
            print("Withdrawal successful. New balance is:", self.balance)


# Sample usage of the SavingsAccount class
account = SavingsAccount(1000)
account.deposit(500)
account.withdraw(200)