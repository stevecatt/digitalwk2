#groceries lists, creat a shop class
#store = 1 #placeholder 

list_of_stores = []
store_names = []
grocery_list = []


menu_entry = " "


class Store:
    def __init__(self,store_name,store_description= "TX"):
        self.store = store_name
        self.desc = store_description
        #putting the lists made from produce entry into here with add_item()
        self.gro_list= []

    def print_store(self):
        print(f"{self.store}, {self.desc}")
        #for i in range(len(self.list)):
             #print(f"{self.list[i]}")

       
      # i neew to figure out the printing atuff
      #     
    def add_item(self):
        self.gro_list.append(grocery_item)
        #for x in self.list:
           #  print(f"{self.list[x]}")

    def print_lists(self):
        for l in self.gro_list:
            print (l)


    


class Produce:
    def __init__(self,item,price,quantity,store):

        self.item=item
        self.price=price
        self.quantity=quantity
        self.store = store

    def print_grocery(self):
        print(f"{self.store} {self.item} ${self.price} Qty X{self.quantity}")
        #y= f"{self.store} this is tha funct{self.item} ${self.price} Qty X{self.quantity}"
        #print(y)

        #print(self.item)



class Shopping:
    def __init__(self, store, groceries):
        self.store = []
        self.groceries = []

    def print_lists(self):
        for store in self.store:
            print (store)






def show_menu():
    print("press 1 to enter store name")
    print("press 2 to enter add grocery to a Store ")
    print("press 3 to display list")
    print("press q to end list")


def view_all_lists():
    for list in list_of_stores:
        print(f" {list.store} {list.desc}")
        for prod in grocery_store_name.gro_list:
            print(f"{prod.list}")



def view_lists():
    for index in range (len(store_names)):
        
        print(f"{index+1} - {store_names[index]}")
    #for l in range(list_of_stores):
        #print(grocery_store_name.list(l))
    for l in  grocery_store_name.gro_list:
        print(l)


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
        #need to modify this to get response if wrong number is entered
        #think a while loop is needed
        
        if store_id > (len(store_names)):
            print("please enter a valid list number")
        else:
            store_list= (store_names[store_id -1])
            print(store_list) #just checking to see what we are gonna input 
   
#should put all the rest of this in a function 
        produce_item = input("please enter item ")
        produce_cost = input("please enter product cost  ")
        produce_quantity = input("please enter product quantity  ")
        grocery_item = Produce(produce_item,produce_cost,produce_quantity,store_list)
        grocery_item.print_grocery()
        grocery_store_name.gro_list.append(grocery_item)
        #grocery_store_name.add_item(grocery_item)
        grocery_store_name.store = store_list
        grocery_store_name.add_item()

        show_menu()

    elif menu_entry == "3":
        for grocery in grocery_list:

            grocery.print_grocery()

            view_lists()
    #show_menu()





for grocery in grocery_list:
    print(f"{grocery_item.store} {grocery_item.item}")

    #grocery.print_grocery()


for store in list_of_stores:
    print (store)
    

    


#for item in store_names:
   # store.print_store
    

#meat.print_grocery()

#print("please enter store name")

#store_name = Store(store_name)
#list_of_stores.append(store_name)

#print (list_of_stores)
#print(store_name.store)
view_all_lists()