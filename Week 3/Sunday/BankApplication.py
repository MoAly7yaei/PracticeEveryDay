import datetime

"""
Bank application
"""
class BankAccount:
    def __init__(self,customer_name ,account_number, balance, date_of_opening):
        
        self.customer_name = customer_name
        self.account_number = account_number
        self.balance = balance
        self.date_of_opening = date_of_opening
        
    def deposit(self, amount):
        self.balance = self.balance + amount
        return self.balance
    
    def withdraw(self, amount):        
        if self.balance - amount <= 0:
            print("No enough balance")
        else:
            self.balance = self.balance - amount
    
    def __str__(self):
        return f"Dear Mr/Ms {self.customer_name} Your Balance is {self.balance} OMR"
    
ahmed = BankAccount("Ahmed", "0379324588321234" , 5464.200 , str(datetime.datetime(2020, 5, 17)))

ahmed.withdraw(6000)

print(ahmed.__str__())

        