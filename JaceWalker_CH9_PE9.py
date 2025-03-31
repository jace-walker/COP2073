#           Jace Walker Programming Exercise 9

# This program creates a generic bank account class and some functions to change the account's details. This program
#    also contains a test function to test the account detail changing functions.


# create bank account class
class BankAcct:
    def __init__(self, name, account_num, balance, interest):
        self.name = name
        self.account_num = account_num
        self.balance = balance
        self.interest = interest

# changes interest rate
    def new_interest_rate(self, new):
        self.interest = new
        print(f'New interest rate is: {self.interest}')

# adds amount chosen to balance
    def deposit(self, amount):
        self.balance += amount
        print(f'Successful deposit. New balance is: {self.balance}')

# withdrawal function. if taking out more than in account, denied.
    def withdrawal(self, amount):
            if amount <= self.balance:
                self.balance -= amount
                print(f'Successful withdrawal. New balance is: {self.balance}')
            else:
                print("Insufficient funds.")

# simple interest formula to calculate interest
    def calculate_interest(self, days):
        interest = (self.balance * self.interest * days) / (100 * 365)
        return interest

# finds balance. but needs an f string to display it
    def get_balance(self):
       return self.balance

# __str__ method to display account details in an organized way
    def __str__(self):
        return (f"Account Member: {self.name}\n"
                f"Account Number: {self.account_num}\n"
                f"Balance: ${self.balance}\n"
                f"Current Interest rate: {self.interest}%\n")



def test_bank_account():
# create user's bank account
    account = BankAcct("Mike Green", "34937623", 25000, 4)

# print their account details before anything is done
    print(account)

# start changing account details
    account.new_interest_rate(10)
    account.deposit(7140)
    account.withdrawal(1769)

# interest over 365 days
    interest = account.calculate_interest(365)
    print(f'Your interest earned over one year is: ${interest:.2f}')

# print user's updated account details
    print('-----------------------')
    print(account)

# just cosmetics
print()
print('Welcome to Python Bank.')
print('-----------------------')

# call test function
test_bank_account()

print('Thanks for banking with us.')