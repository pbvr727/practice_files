"""3. Bank Account System

Scenario:
Users can deposit, withdraw, and check balance.

Question:

Create a class BankAccount
Prevent direct access to balance
Ensure withdrawal cannot exceed balance
👉 Use encapsulation + private variables"""
class BankAccount:
    bank="SBI Bank"
    def __init__(self):
        self.balance=0
    def deposit(self,deposit1):
        self.balance=self.balance+deposit1
        print(BankAccount.bank)
        print("Account balancec is",self.balance)
    def withdraw(self,withdr):
        if self.balance<withdr:
            print("insufficien funds")
        else:
            self.balance=self.balance-withdr
            print(self.balance,"succseefully withdaw")
       
    # 
b=BankAccount()
b.deposit(10006)
b.withdraw(250)