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
        pass

    def withdraw(self, amount):
        pass
    
    def display_account_info(self):
        pass

    def yield_interest(self):
        pass

# //// FUNCTIONS ///////////////////////////////////////////

# //// MAIN EXECUTABLE SECTION /////////////////////////////

account_1 = BankAccount(6,1000)

