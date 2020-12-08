import sys
'''

# the rentalCode allows users to determine the type of rental
rentalCode = input('(B)udget, (D)aily, or (W)eekly rental?\n') #a break statement \n is used here to create a new line
# once the user inputs the value of the variable^^ the if/ else loop will respond by asking the next question
if rentalCode == 'B' or rentalCode == 'D': 
  rentalPeriod = int(input("Number of Days Rented:\n")) #here we gave the value of the variable and integer value by using int()
# both "B" and "D" fall under the days category and can be combined, as they will prompt the same user input
else:
  rentalPeriod = int(input("Number of Weeks Rented:\n"))
#this else statement will only be used if the if statement is proven false and the user needs the car for weeks not days

# this next section assigns a value to each variable
BudgetCharge = 40.00
DailyCharge = 60.00
WeeklyCharge = 190.00
#next we will use an if/ elif loop to create the variable for the basecharge of each rentalCode

if rentalCode == 'B': #if user inputs 'B' than this line is proven true
  baseCharge = float(rentalPeriod * BudgetCharge)# the baseCharge is the rentalPeriod multiplied by the budgetCharge
  #^^^^the float function was used in the equation to turn the value of the variable to an integer with decimals
elif rentalCode == 'D': #if the first statement is false this statement will be checked
  baseCharge = float(rentalPeriod * DailyCharge) #here the base charge is the rentalPeriod multiplied by the DailyCharge 
  #the float function is used here to make the value an integer with decimals
elif rentalCode == 'W': # if the first two statements are proven false than this statement will be true 
  baseCharge = float(rentalPeriod * WeeklyCharge)#here the basecharge is the rentalPeriod multiplied by WeeklyCharge
  #the float is also used here to create an integer value with decimals

# format the print output to 2 decimals with ,.2f
odoStart = input('Starting Odometer Reading:\n') #this tells the user to input the starting odometer reading
odoEnd = input('Ending Odometer Reading:\n')# this tells the user to input the ending odometer reading
# convert customer input to integers by using int() in the following statement
totalMiles = int(odoEnd) - int(odoStart) # the totalMiles variable is found by subtracting the odoEnd by the odoStart

mileCharge= 0  #here I assigned a starting value to the mileCharge variable

#based on the customers input one of these if statements will be triggered and executed if it proves to be true
#each rentalCode has its own if/elif loop 
if rentalCode == 'B':
  mileCharge = 0.25 * totalMiles 

if rentalCode == 'D':
  averageDayMiles = (totalMiles/rentalPeriod)# for daily we need to figure out the averageDayMiles
  #this next statement determines if the average is less than or equal to 100 
  if averageDayMiles <= 100:
    totalMiles = 0 #if proven true there is no charge so the value of the varible totalMiles equals 0
  elif averageDayMiles > 100: #if the previous statement is false than this statement is true
    extraMiles = averageDayMiles - 100 # for this rentalCode it only charges for the average miles over 100, so we subtract 100 of the averageDayMiles
    mileCharge = 0.25 * extraMiles #this determines the cost of the mileCharge

if rentalCode == 'W': #if user inputs "W" this loop will be ran
  averageWeekMiles= totalMiles/rentalPeriod #here we find the value of averageWeekMiles by dividing totalMiles by rentalPeriod
  
  if averageWeekMiles <= 900: #this statement tests to see if the value of the above variable is equal or less than 900
    mileCharge = 0 #here we set a value of the above statement to 0
  elif averageWeekMiles > 900: #if the above statement is proven false than this one must be true
    mileCharge = 100 * rentalPeriod 

#this string will determine the amount that is due based off of the customers inputs  
amtDue = baseCharge + mileCharge

#Make sure to use str() to convert values from the previous code blocks to their own strings
#this final print section will be what the customer sees
print('Rental Summary')
print('Rental Code: '+str(rentalCode))
print('Rental Period: '+str(rentalPeriod))
print('Starting Odometer: '+str(odoStart))
print('Ending Odometer: '+str(odoEnd))
print('Miles Driven:  '+str(totalMiles))
print('Amount Due:  ','${0:.2f}'.format(amtDue))
#^^^we want the amount to appear with 2 decimals so we use the .2f 
