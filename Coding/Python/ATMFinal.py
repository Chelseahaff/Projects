import sys

#Here the account_balance is defined as a float so that it will have decimals and gives the user a starting variable
account_balance = float(500.25)

def print_balance():
  
  print('Your current balance:\n %.2f' % account_balance)
#here we define the print_balance function and have it return a printed string along with the account_balance 
#the %.2f is a two decimal place holder for the account_balance

def deposit(amount): # here we define the deposit function

  print('Deposit was $%.2f, current balance is $%.2f' % (amount, account_balance + amount)) #we add the amount deposited to the account_balance
  #here we print the deposited amount along with the new balance.
  #adding the strings along with the variables cleans it up for the user

def withdraw(amount): #here we define the withdraw function

  #we set the withdrawal_amount amount as an integer using the float() function
  #we use the input() to allow the user to pick an amount to withdraw, and insert a string value to direct the user
  
  if amount > account_balance: #the user cannot take more than the balance and this if statement checks for this
  
  print('$%.2f is greater than your account balance of $%.2f' % (amount, account_balance))
    #if the ^^ if statement is true and the withdrawal_amount is more than account_balance this will print saying just that
  
  else:# the else statement provides another option if the ^^if statement is proven false
  
  print('Withdrawal amount was $%.2f, current balance is $%.2f' % (amount, account_balance - amount))
    #here we state the amount withdrawn with 2 decimals and the balance after subraction of the withdrawal_amount with 2 decimals.

#now the we have defined our functions we can write the program to interact with user input        
userchoice = input ("What would you like to do?\n")
#we will use if, elif loop to give the user their options
if (userchoice == 'D'): #this allows the user to select the deposit function
    deposit_amount= float(input("How much would you like to deposit today?\n"))
    deposit (deposit_amount)#here we sent in the deposit_amount , defined above^^ as the parameter for this function

elif (userchoice == 'W'): #this allows the user to select the withdraw function
    withdrawal_amount = float(input("How much would you like to withdraw today?\n"))
  #we use the input() to allow the user to pick an amount to withdraw, and insert a string value to direct the user
  #we define withdrawal_amount amount here^^^
    withdraw(withdrawal_amount)#here we set the withdrawal_amount, defined above, as the parameter for the withdraw() function

elif (userchoice == 'B'): #this allows the user to select the balance function
    balance(account_balance)# the parameterfor the balance() function is the account_balance

elif (userchoice == "Q"): #this allows the user to break the loop and quit
  print('Thank you for banking with us.')

