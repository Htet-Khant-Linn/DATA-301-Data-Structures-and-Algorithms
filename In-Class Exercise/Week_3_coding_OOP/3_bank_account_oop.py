# class BankAccount:
#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.balance = balance

#     def deposit(self, amount):
#         self.balance += amount
#         print("Deposit successful")

#     def withdraw(self, amount):
#         if amount <= self.balance:
#             self.balance -= amount
#             print(f"Withdraw successful")
#         else:
#             print("Insufficient balance")

#     def show_balance(self):
#         print(f"Current balance: {self.balance}")


# account1 = BankAccount("John", 1000)
# account1.show_balance()
# account1.deposit(500)
# account1.show_balance()
# account1.withdraw(2000)
# account1.show_balance()

# Exercise 3: Wallet class
# attributes owner and balance
# methods -> add_money(amount), spend_money(amount), check_balance()

class Wallet:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def add_money(self, amount):
        self.balance += amount
        print(f"{amount} added successfully.")

    def spend_money(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"{amount} spent successfully")
        else:
            print("Not eough money!")

    def check_balance(self):
        print(f"{self.owner}'s current balance is {self.balance}.")


wallet1 = Wallet("Miya", 500)

wallet1.add_money(200)
wallet1.check_balance()
wallet1.spend_money(300)
wallet1.check_balance()