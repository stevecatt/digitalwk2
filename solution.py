
# from filename import class name 
#from shopping_list import ShoppingList

# seperate the classes into other files

user_input = ""
shopping_lists = [] 


class ShoppingList: 
  def __init__(self,name, address): 
    self.name = name 
    self.address = address
    self.grocery_items = [] 
  
  def display(self): 
    pass 

class GroceryItem: 
  def __init__(self,name,price,quantity): 
    self.name = name 
    self.price = price 
    self.quantity = quantity 

def show_menu(): 
  print("Enter 1 to add shopping list: ")
  print("Enter 2 to add grocery item: ")
  print("Enter 3 to view all shopping lists: ")
  print("Enter q to quit")


def add_shopping_list(): 
  name = input("Enter name of shopping list: ")
  address = input("Enter address of shopping list: ")
  shopping_list = ShoppingList(name, address)
  # adding a shopping list object to shopping lists array
  shopping_lists.append(shopping_list)
  
def view_all_shopping_lists(): 

  for index in range(0,len(shopping_lists)): 
    shopping_list = shopping_lists[index]
    print(f"{index+1} - {shopping_list.name} - {shopping_list.address}")
    for grocery_item in shopping_list.grocery_items:
      print(f"  {grocery_item.name} - {grocery_item.price} - {grocery_item.quantity}")

  #for shopping_list in shopping_lists:
   # print(shopping_list) 
    #print(f"{shopping_list.name} - {shopping_list.address}")
    
def add_grocery_item(): 
  view_all_shopping_lists() 
  shopping_list_number = int(input("Enter shopping list number to add the grocery item: "))
  # get the selected shopping list 
  shopping_list = shopping_lists[shopping_list_number - 1]
  name = input("Enter name of grocery item: ")
  price = float(input("Enter price of grocery item")) 
  quantity = int(input("Enter quantity of grocery item: ")) 
  grocery_item = GroceryItem(name,price,quantity)

  # adding grocery item to shopping list 
  shopping_list.grocery_items.append(grocery_item)

while user_input != 'q': 
  show_menu() 
  user_input = input("Enter your choice: ")

  if user_input == "1": 
    add_shopping_list() 
  elif user_input == "2": 
    add_grocery_item() 
  elif user_input == "3": 
    view_all_shopping_lists() 
  