# hermetyzacja

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        # private
        # name mangling
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Invalid deposit amount")


account = BankAccount("Radek", 1000)
# print(account.balance) # AttributeError: 'BankAccount' object has no attribute 'balance'
print(account.get_balance())  # 1000
