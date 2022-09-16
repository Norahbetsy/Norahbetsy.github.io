#  Using classes ,creat basic banking application with the following features:
# # create aclass called BankAccount with the following attributes:
# account_number-a string, balance_a float, type_string, name _string

class BankAccount:
      def __init__(self, account_number, balance, owner, type):
        self.account_number = str(account_number)
        self.balance = float(balance)
        self.owner = str(owner)
        self.type = str(type)

BankAccount1 =BankAccount("0121345678","30000", "Norah", "Savings")
#print the BankAccount object
print(BankAccount1.account_number)
print(BankAccount1.balance)
print(BankAccount1.owner)
print(BankAccount1.type" \n")

BankAccount2 =BankAccount("0621345678","430000", "Betsy", "CurrentAccount")


#print the BankAccount object
print(BankAccount2.account_number)
print(BankAccount2.balance)
print(BankAccount2.owner)
print(BankAccount2.type)

BankAccount3 =BankAccount("0127345678","330000", "BetsyNorah", "Fixed")
#print the BankAccount object
print(BankAccount3.account_number)
print(BankAccount3.balance)
print(BankAccount3.owner)
print(BankAccount3.type)


# create aclass called Bank with the following attributes:
# name_string, account alist of Bank Account

class Bank:
      def __init__(self, name, accounts):
        self.name = str(name)
        self.accounts = list(accounts)
BankAccountlist = [BankAccount1, BankAccount2,BankAccount3 ]
#print the bank
Bank1 =JinjaBank
JinjaBank=Bank("Jinja Bank",BankAccountlist)

print(name(BankAccountlist))


  
# create aclass called Customer with the following attributes:
# name_a string
# accounts_alist of BankAccounts

class customer:
      def __init__(self, name, accounts):
        self.name = str(name)
        self.accounts = list(accounts)

BankAccountlist = [BankAccount1, BankAccount2,BankAccount3 ]  
#print customer
BettyCustomer =Customer("Betty Customer",BankAccountlist)    

    



#creat aclass called Transactions with the following attribute:
#'account'-a 'Bank
#'amount'_a float
#'type'_a a string

class Transactions :
      def __init__(self, account, amount, owner, type):
        self.account_number = Bank(account)
        self.amount = float(amount)
        self.type = str(type)







































