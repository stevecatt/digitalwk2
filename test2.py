class Store:
    def __init__(self,store_name,store_description):
        self.store = store_name
        self.desc = store_description
        self.list= []

    def print_store(self):
        print(self.store, self.desc, self.list)

    def add_item(self):
        self.list.append()

    


class Produce:
    def __init__(self,item,price,quantity,store):
        self.item=item
        self.price=price
        self.quantity=quantity
        self.store = store

    def print_grocery(self):
        print(f"{self.store} {self.item} $ {self.price} Qty {self.quantity}")
        #print(self.item)


def show_menu():
    print("press 1 to enter store name")
    print("press 2 to enter add grocery to a Store ")
    print("press 3 to display list")
    print("press q to end list")


#def view_all_lists():



def view_lists():
    for i in range (len(store_names)):
        
        print(f"{i+1} - {store_names[i]}")

#def select_store():
    
#def select_store():
   # view_lists()
    
    
    #store_list= int(store_names[store_id -1])
    


#store_list = 1
    



#create an empty list of stores 
show_menu()


while menu_entry != "q":
    menu_entry = input("Please enter choice   ")
    if menu_entry == "1":
        store_name = input("Please enter store name    "   )
        store_desc = input("Please enter store description   ")
        grocery_store_name = Store(store_name,store_desc)
        list_of_stores.append(grocery_store_name)
        store_names.append(store_name)
    
        view_lists()
        show_menu()
        #list(of stores)


    elif menu_entry == "2":
        
        view_lists()
        #select_store()
        store_id= int(input("Please input number of store  from list "))
        store_list= (store_names[store_id -1])
   

        produce_item = input("please enter item ")
        produce_cost = input("please enter product cost  ")
        produce_quantity = input("please enter product quantity  ")
        grocery_item = Produce(produce_item,produce_cost,produce_quantity,store_list)
        grocery_item.print_grocery()
        grocery_list.append(grocery_item)
        #store.add_item()
        

        show_menu()



for grocery in grocery_list:

    grocery.print_grocery()


for store in list_of_stores:
    store.print_store()




#meat.print_grocery()

#print("please enter store name")

#store_name = Store(store_name)
#list_of_stores.append(store_name)

#print (list_of_stores)
#print(store_name.store)
#view_lists()