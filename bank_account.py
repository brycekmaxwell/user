class BankAccount:
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance
        # your code here! (remember, instance attributes go here)
        # don't worry about user info here; we'll involve the User class soon
    def deposit(self, amount):
        self.balance += amount
        return self
        # your code here
    def withdraw(self, amount):
        if(self.balance-amount) >=0:
            self.balance-=amount
        else:
            print("Insufficient Funds: Charging a $5 fee")
            self.balance -=5
        return self
        # your code here
    def display_account_info(self):
        print(f"Balance: $ {self.balance}")
        return self
        # your code here
    def yield_interest(self):
        if self.balance >0:
            self.balance += (self.balance * self.int_rate)
        return self
        # your code here
checking = BankAccount(.01, 100)
savings = BankAccount(.03, 2500)    

checking.deposit(300).deposit(256).deposit(42).withdraw(17).yield_interest().display_account_info()

savings.deposit(800).deposit(1500).withdraw(450).withdraw(50).withdraw(20).withdraw(100).yield_interest().display_account_info()