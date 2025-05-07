# Assignment
# Inheritance
# Polymerphisum
# Incapsulation ko study kar k ana hy.

from dataclasses import dataclass

@dataclass()
class Bankacc():
    account_title: str 
    account_number: int
    balance: int = 0
    def deposit(self, amount:int):
        self.balance = self.balance + amount
        print(f"Depositing {self.balance}")
        
    def withdra(self, amount:int):
        if amount > self.balance:
            print("Insufficient Funds")
        else:
            self.balance = self.balance -amount
        self._balance = self.balance - amount
        print(f"Withdrwing {self.balance}")
    
Danish = Bankacc(f"Danish", 12345678)
Danish.deposit(100)

# @dataclass
# class Current_Account(Bankacc):
#     overdraft_limit: int = 1000
    