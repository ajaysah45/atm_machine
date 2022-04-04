#! /usr/bin/python3

def main():
     count=0
     while True:
          if count>=3:
              time.sleep(3)
              print("\nyour card has been blocked")
              print("please visit to nearest branch of AKS Bank")
              time.sleep(2)
              quit()
          pin_code=int(input("enter your 4-digit Pin code:\n\t"))
          if pin_code==4545:
             class Account:
                 def __init__(self,name,balance,min_bal):
                    self.name=name
                    self.balance=balance
                    self.min_bal=min_bal
                 def account_info(self):
                    print("Name of Account_holder:",self.name)
                    print("Balance available:",self.balance)
                 def deposit(self,amount):
                    self.balance=self.balance+amount
                    print("Total balance:",self.balance)
                 def withdraw(self,amount):
                    if self.balance-amount>self.min_bal:
                           self.balance=self.balance-amount
                           print("Available balance:",self.balance)
                           time.sleep(1)
                           print("Collect the Cash")
                    else:
                           print("Insufficient fund")
             class Current_account(Account):
                 def __init__(self,name,balance):
                    super().__init__(name,balance,min_bal=-1000)
                 def __str__(self):
                    return "current name:{} and balance available:{}".format(self.name,self.balance)
             class Saving_account(Account):
                 def __init__(self,name,balance):
                   super().__init__(name,balance,min_bal=0)
                 def __str__(self):
                   return "current name:{} and balance available:{}".format(self.name,self.balance)
             c=Current_account('ajay',20000)
             s=Saving_account('ajay',10000)
             account_type=input("enter type of account [Saving or Current]\n")
             if account_type.lower()=='saving':
                 while True:
                    option=int(input(''' Select Your Option:
                    1. Deposit
                    2. Withdraw
                    3. Account_Info \n'''))
                    if option==1:
                           amount=int(input('enter amount to deposit:  '))
                           print(s.deposit(amount))
                    elif option==2:
                           amount=int(input('enter amount to withdraw:  '))
                           print(s.withdraw(amount))
                    elif option==3:
                           print(s.account_info())
                    else:
                        print("Wrong Option")
                        continue
                    break
             if account_type.lower()=='current':
                while True:
                    option = int(input(''' Select Your Option:
                              1. Deposit
                              2. Withdraw
                              3. Account_Info \n'''))
                    if option == 1:
                             amount = int(input('enter amount to deposit:  '))
                             print(s.deposit(amount))
                    elif option == 2:
                             amount = int(input('enter amount to withdraw:  '))
                             print(s.withdraw(amount))
                    elif option == 3:
                             print(s.account_info())
                    else:
                             print("Wrong Option")
                             continue
                    break
          else:
              print("Incorrect Pin code\n")
              count=count+1
              if count>=3:
                  print("entered wrong pin code 3 times ")
              continue

          time.sleep(3)
          print("Please take your ATM card")
          time.sleep(3)
          print("Thanks for using our service")
          break

import time
print("\nWelcome to AKS Bank\n")
time.sleep(1)
card = input("Insert your ATM card: ")
if card == "ok":
    language = input("Select your Language [English | Nepali]:  ")
    main()
else:
    quit()
