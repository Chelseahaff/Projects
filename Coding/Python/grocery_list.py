




grocery_item = {}
#^^^defines an empty dictionary
grocery_history = list()
#^^defines an empty list


stop = 'go'
#^^ we set stop as the variable to check if the statement is true

while stop != 'q': 
#^^creation of a while loop as long as stop doesn't equal quit


   
    item_name = input('Item name: ') #created user input for item name
   
    quantity = input('Quantity purchased: ') #Create user input for item quantity
   
    cost = input('Price per item: ')#create user input for each item price
   
    grocery_item['name'] = item_name
    grocery_item['number'] = int(quantity) #using int() makes it an number instead of a string
    grocery_item['price'] = float(cost)# using float adds a decimal for price
  
    grocery_history.append(grocery_item.copy())
    #^this statement copies the user input and adds the the dictionary via append() function
    
    stop = input("Would you like to enter another item?  \nType \'c\' for continue or \'q\' to quit :")
    #this is our break statement that will stop the cycle if stop is proven to be false

grand_total = 0 #here we defined the grand total by setting it to 0


for index, item in enumerate(grocery_history):#the enumerate() function allows us to continually loop through each item
  
  
  item_total= item['number'] * item['price']#this equation allows us to multiply the price by quantity
 
  grand_total += item_total #this will total all the separate item_totals together 
 
  print('%d %s  @ $%.2f ea $%.2f' % (item['number'], item['name'], item['price'], item_total))
  #the % is used as a space for the various dictionary values
  #%d is for a 'number' placeholder, %s holds for a string'name', the $%.2f is used twice to give a price and total with 2 decimals
  
  item_total= 0#here we set the item total to 0 to start


print('Grand total: $%.2f' % grand_total)# we made it display Grand Total: and the previous grand_total will populate