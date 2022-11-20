print("Welcome to the shopping cart program! ")
print()

items = []
prices = []

cart = []

start_input = int
  
#used with main_menu function
option_menu = []
option_menu.append("1. Add item")
option_menu.append("2. View cart")
option_menu.append("3. Remove Item")
option_menu.append("4. Compute Total")
option_menu.append("5. Quit")

#used with main_or_quit function
moq_list = []
moq_list.append("1. Yes")
moq_list.append("2. Quit")


#This function is used when user is finished using current option
def main_or_quit():
  print("Would you like to go back to the main menu?")
  print(*moq_list, sep = "\n")
  moq_input = int(input())
  if moq_input == 1:
    main_menu()
  elif moq_input == 2:
    print("Thank you, goodbye. ")
  else:
    print()
    print("Please select a valid option ")
    print("Would you like to go back to the main menu? ")
    print(*moq_list, sep = "\n")
    main_or_quit() 
    
  
#main menu options
def main_menu():
  print("Please select one of the following: ")
  print(*option_menu, sep = "\n")
  start_input = int(input())
  if start_input == 1:
    add_menu()
    main_or_quit()
  elif start_input == 2:
    print_cart()
    main_or_quit()
  elif start_input == 3:
    remove_items()
  elif start_input == 4:
    print("Still working on this option, stay tuned for update.")
  elif start_input == 5: 
    print("Thank you, goodbye. ")
  else:
    print()
    print("Please select a valid option ")
    main_menu()


#This function is used when user selects option 1 from main menu    
def add_menu():
  item_input = ""
  price_input = float
  while item_input != "end":
    item_input = input("What item would you like to add? (Type END when finished) ")
    if item_input != "end":
      #adds item to items list
      items.append(item_input)
      price_input = float(input("What is the price of the item? "))
      #adds price to prices list
      prices.append(price_input)
      print(f'{item_input} has been added to your cart. ')
      
      print()
    elif item_input == "end":
      #zips index, items and prices and appends to cart list
      for i, (item,price) in enumerate(zip(items,prices)):
        cart_list = (f'{items[i]} ${prices[i]:.2f}')
        cart.append(cart_list)
      print_cart()
            
      print()
      #prints main or quit menu
      main_or_quit()

      
#This function prints index, items and prices in cart
def print_cart():
  print("The contents in your shopping cart are: ")
  for (i, item) in enumerate(cart, start =1):
    print(i, item)

    
def remove_items():
  print_cart()
  print("Which item number would you like to remove? ")
  
  remove_input = int(input())
  del cart[remove_input - 1]
  
  print_cart()
  
          
#Calls main_menu function to start the program
main_menu()
