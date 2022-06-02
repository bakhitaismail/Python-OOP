class Account:
    bank="Equity Bank"
    
    def __init__(self,name, deposit,withdrawal, balance):
        self.name=name
        self.deposit=deposit
        self.withdrawal=withdrawal
        self.balance=balance 
        
    def depo(self):
        return f"Hello {self.name} you have deposited {self.deposit} your new balance is {self.balance}"    
    def withdraw(self):
        return f"Dear {self.name} you have withdrawn kshs {self.withdrawal}"