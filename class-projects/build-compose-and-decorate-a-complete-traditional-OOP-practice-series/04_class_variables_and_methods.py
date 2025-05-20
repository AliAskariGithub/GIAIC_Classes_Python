class Bank:
    bank_name = "Default Bank"
    
    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name
    
    def __init__(self, branch):
        self.branch = branch

# Example usage
if __name__ == "__main__":
    bank1 = Bank("Branch 1")
    bank2 = Bank("Branch 2")
    print(Bank.bank_name)
    Bank.change_bank_name("New Bank")
    print(Bank.bank_name)