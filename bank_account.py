import random
account_number = list(range(10000000,100000000))
print("account numbers have been generated")
random.shuffle(account_number)
print("numbers have been shuffled")
class BankAccount:
    routing_number = 123456789
    def __init__(self, full_name):
        self.full_name = full_name
        self.account_number = account_number.pop(len(account_number)-1)
        self.balance = 0

    def sensitize_account_number(self):
        return "****" + str(self.account_number)[4:]

    def deposit(self, amount):
        """ add amount to balance"""
        self.balance += amount
        print ("Amount Deposited: $", amount)
        

    def withdraw(self, amount):
        """subtract from balance and overdraft"""
        if amount > self.balance:
            self.balance-= 10
            print ("Insufficient Funds")
        elif self.balance >= amount:
            self.balance -= amount
            print ("Amount Withdrawn: $", amount)
        
       

    def get_balance(self):
        """print a friendly balance message and return account balance"""
        print ("your account balance is: $", self.balance)
        return self.balance
        

       
    def monthly_interest(self):
        """helper function calculating interest"""
        return self.balance * 0.00083
        

    def add_interest(self):
        """adds monthly interest to the balance"""
        self.balance += self.monthly_interest()
        
    

    def print_receipt2(self):
        """print the receipt with Full Name, Accountnumber routing number and Balance"""
        print ('{}\n Account No.:{}\n Routing No.:{}\n Balance: ${}'.format(self.full_name, self.sensitize_account_number(), self.routing_number, self.balance))
        

account = BankAccount("Andrea-Graziosi")

account.deposit(55)
account.withdraw(5)
account.get_balance()
account.add_interest()
print("---------------------------")
account.print_receipt2()
print("---------------------------")
account2 = BankAccount("Lea-Smith")
account2.deposit(600)
account2.withdraw(300)
account2.get_balance()
account2.add_interest()
print("---------------------------")
account2.print_receipt2()
print("---------------------------")
account3 = BankAccount("Thais-DaSilva")
account3.deposit(200)
account3.withdraw(400)
account3.get_balance()
account3.add_interest()
print("---------------------------")
account3.print_receipt2()


