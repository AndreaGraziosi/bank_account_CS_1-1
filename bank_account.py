class BankAccount:
    def __init__(self, full_name, account_number, routing_number, balance):
        self.full_name = full_name
        self.account_number = account_number
        self.routing_number = routing_number
        self.balance = balance

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
        
       

    def get_balance():
        """print a friendly balance message and return account balance"""
        #self.deposit(50)
       # print ("Your Balance is:")
       # pass

   # def get_interest():
        """adds interest to users Balance"""
        #monthly_interest= balance * 0.00083

   # def print_receipt():
        """prints a receipt with name account number and balance"""

'{} {}'.format('one', 'two') 
#define 3 different bank account examples using the BankAccount() object. 
    
account = BankAccount("andrea Graziosi", "25872487234873", "462984", 200)
account.deposit(10)
account.withdraw(215)