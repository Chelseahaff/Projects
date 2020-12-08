import sys


account_balance = float(500.25)

def balance():
  
  print('Your current balance:\n %.2f' % account_balance)

def deposit(amount):

  print('Deposit was $%.2f, current balance is $%.2f' % (amount, account_balance + amount)) 

def withdraw(amount): 
  
  if amount > account_balance: 
  
  print('$%.2f is greater than your account balance of $%.2f' % (amount, account_balance))
     
  else:
  
  print('Withdrawal amount was $%.2f, current balance is $%.2f' % (amount, account_balance - amount))
   
          
userchoice = input ("What would you like to do?\n")
if (userchoice == 'D'): 
    deposit_amount= float(input("How much would you like to deposit today?\n"))
        deposit (deposit_amount)

elif (userchoice == 'W'): 
    withdrawal_amount = float(input("How much would you like to withdraw today?\n"))
  
    withdraw(withdrawal_amount)

elif (userchoice == 'B'): 
    balance(account_balance)

elif (userchoice == "Q"):
  print('Thank you for banking with us.')

