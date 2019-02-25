user_input = "" 
stores = [] 

class Store: 
  def __init__(self,name, address): 
    self.name = name 
    self.address = address

def show_menu(): 
  print("Press 1 to add store: ")
  print("Press 2 to add item to a store: ")
  print("Press 3 to view all stores: ")
  print("Press q to quit: ")

def add_store(): 
  name = input("Enter store name: ")
  address = input("Enter store address: ")
  # 1200 Richmond Ave Houston, TX 
  store = Store(name,address)
  stores.append(store)

def view_all_stores(): 
  for store in stores: 
    print(f"{store.name} - {store.address}")


show_menu() 

while user_input != 'q': 
  user_input = input("Enter your choice: ")

  if user_input == "1": 
    add_store() 
  elif user_input == "3": 
    view_all_stores() 




