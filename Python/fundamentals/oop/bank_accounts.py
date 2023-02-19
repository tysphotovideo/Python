class BankAccount:
    def __init__(self, int_rate, balance):
         self.int_rate = int_rate
         self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdrawl(self, amount):
        if(self.balance - amount) >= 0:
            self.balance -= amount
        else:
            print(f"Insufficient funds: Charging a $5 fee")
            self.balance -= amount
        return self
    def display_account_info(self):
        print(f"Balance: {self.balance}")
        return self
    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
        return self

tyler_savings = BankAccount(.04, 1000)
tyler_checking = BankAccount(.002, 2500)

tyler_savings.deposit(100).deposit(80).deposit(40).withdrawl(1000).yield_interest().display_account_info()
tyler_checking.deposit(100).deposit(80).withdrawl(40).withdrawl(1000).withdrawl(100).withdrawl(50).yield_interest().display_account_info()

class User:
    
    def __init__(self, name, email):
         self.name = name
         self.email = email
         self.account = BankAccount(.04, 25000)
    
    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self
    
    def make_withdrawl(self, amount):
        self.account.withdrawl(amount)
        return self
    
    def display_user_balance(self):
        self.account.display_account_info()
        return self
        
lyndi_sav = User(Lyndi,L@sellers.com) 

lyndi_sav.make_deposit      
    

 