# //////////////////////////////////////////////////////////
# Subj: Coding Dojo > Python Stack > Python > OOP: Bank Account 
# By: Virgilio D. Cabading Jr
# //////////////////////////////////////////////////////////

import utl

# //// CLASSES /////////////////////////////////////////////

class BankAccount:
    def __init__(self, int_rate=10, balance=0):                 # Construct an instance of the bank account class
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):                                  # Add amount to the bank account balance
        self.balance += amount
        return self

    def withdraw(self, amount):                                 # Subtract amount from the bank account
        if (self.balance-amount) >= 0:
            self.balance -= amount
        else:
            print(f"{f'Insufficient funds to withdraw ${amount} from account balance of ${self.balance} ':*<100}")
            self.balance -= 5
            print(f"{f' Charging $5 due to insufficient balance, new account balance is ${self.balance}':*>100}")
        return self
    
    def display_account_info(self):
        utl.print_desc_center("bank account info")
        print(f"{f' balance : ${self.balance} ::: interest rate : {self.int_rate} ':^100}\n")
        return self

    def yield_interest(self):
        pass

# //// FUNCTIONS ///////////////////////////////////////////

# //// MAIN EXECUTABLE SECTION /////////////////////////////

account_1 = BankAccount(6,1000)
account_1.display_account_info()

utl.print_desc("Depositing $10")
account_1.deposit(10).display_account_info()

utl.print_desc("Withdrawing $20")
account_1.withdraw(20).display_account_info()

utl.print_desc("attempting to withdraw $2000")
account_1.withdraw(2000).display_account_info()
