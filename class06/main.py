# public    >>> set default
# private   >>> __ (double underscore)
# protected >>> _ (single underscore)

class BankAccount:
    # __init__ is a constructor
    def __init__(self, account_holder: str, balance: float):
        self.account_holder = account_holder
        self.__balance = balance
        
    def deposit(self, amount: float):
        if amount <= 0:
            print(f"Deposit amount must be positive. You entered: {amount} \n")
        else:
            self.__balance += amount
            print(f"Deposited {amount} to {self.account_holder}'s account. New balance: {self.__balance} \n")
        
    def withdraw(self, amount: float):
        if amount > self.__balance:
            print(f"Insufficient funds for withdrawal of {amount} from {self.account_holder}'s account. \n")
        else:
            self.__balance -= amount
            print(f"Withdrew {amount} from {self.account_holder}'s account. New balance: {self.__balance} \n")
            
    def checkbalance(self):
        print(f"{self.account_holder}'s account balance: {self.__balance} \n")
        return self.__balance

# Only run this code if this file is run directly, not when imported
if __name__ == "__main__":
    # ======================================================= #
    
    account01 = BankAccount("Ali", 10000.0)
    account01.deposit(24000.0)
    # account01.__balance()  # This line causes an error - __balance is an attribute, not a method
    
    # ======================================================= #
    
    account02 = BankAccount("Rizwan", 243000.0)
    account02.withdraw(300000.0)
    account02.withdraw(20000.0)
    
    # ======================================================= #
    
    account03 = BankAccount("Baqir", 50000.0)
    account03.checkbalance()