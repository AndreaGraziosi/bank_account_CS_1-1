import random
account_numbers = list(range(10000000,100000000))

class BankAccount:
    routing_number = 123456789
    def __init__(self, full_name, account_number):
        self.full_name = full_name
        random.shuffle(account_numbers)
        self.account_number = account_numbers.pop(len(account_number))
        self.balance = 0


    def deposit(self, amount):
        """ add amount to balance"""
        self.balance += amount
        print ("Amount Deposited: $", amount)
        print (self.balance)

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
        print ("your account balance is: ", self.balance)
        return self.balance
        

       
    def monthly_interest(self):
        """helper function calculating interest"""
        return self.balance * 0.00083
        

    def add_interest(self):
        """adds monthly interest to the balance"""
        self.balance += self.monthly_interest()
        
    def print_receipt(self):
        """print the receipt with Full Name, Accountnumber routing number and Balance"""
        print ('{} {} {}'.format(self.full_name, self.account_number, self.balance))
        
 
account = BankAccount("andreaGraziosi", 200)
account.deposit(35)
account.withdraw(15)
account.balance()

account2 = BankAccount("leaSmith",300)
account3 = BankAccount("Thais DaSilva", 45)
print(account.print_receipt())