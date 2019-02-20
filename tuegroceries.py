#groceries lists, creat a shop class
#store = 1 #placeholder 

stores = []
store_names = []
#grocery_items = []
total = []

menu_entry = " "


class Store:
    def __init__(self,store_name,store_description):
        self.store = store_name
        self.desc = store_description
        #putting the lists made from produce entry into here with add_item()
        self.grocery_items = []
        #self.grocery_items = [] 

    def print_store(self):
        print(f"{self.store}, {self.desc}")
        #for i in range(len(self.list)):
             #print(f"{self.list[i]}")
    def price_total(self):
        list_price_total = 0
        for grocery_item in self.grocery_items:
        #for item in self.grocery_items.price():
            list_price_total += grocery_item.price
        print(list_price_total)    


       
      


    


class Produce:
    def __init__(self,item,price,quantity,):

        self.item=item
        self.price=price
        self.quantity=quantity
        # maybe take this out once i have it right just a poiter for now 
        #self.store = store

    def print_grocery(self):
        print(f"{self.item} ${self.price} Qty X{self.quantity}")
        #y= f"{self.store} this is tha funct{self.item} ${self.price} Qty X{self.quantity}"
        #print(y)

        #print(self.item)


def price_total_outside():
    #this seems to work need to add totals of totals and fancy multipliers to sum total 
    
    for index in range (0,len(stores)):
        shop = stores[index]
        
       
        print(f"Total for {index+1} - {shop.store} - {shop.desc}=")
        shop.price_total()
        #for grocery_item in shop.grocery_items:
         #   print(f"  {grocery_item.item} - {grocery_item.price} - {grocery_item.quantity} ")
          #  total.append(grocery_item.price)
           # print(total)
            
    #print(total)


def sum_total():
    sum = 0
    for s in range(0,len(total)):
        sum = sum + total[s]
    print(sum)    






def show_menu():
    print("press 1 to enter store name")
    print("press 2 to enter add grocery to a Store ")
    print("press 3 to display list")
    print("press q to end list")


def view_shop():
    for index in range (0,len(stores)):
        shop = stores[index]
        print(f"{index+1} - {shop.store} - {shop.desc}")
    #for shop in stores:
        #print(f" {shop.store} {shop.desc}")
        #for prod in grocery_store_name.gro_list:
         #   print(f"{prod.list}")

  

def view_stores():
    for index in range (0,len(stores)):
        shop = stores[index]
        print(f"{index+1} - {shop.store} - {shop.desc}")
        for grocery_item in shop.grocery_items:
            print(f"  {grocery_item.item} - {grocery_item.price} - {grocery_item.quantity} ")
            #sum_price = grocery_item.price += grocery_item.price
    #for l in range(list_of_stores):
        #print(grocery_store_name.list(l))
    #for l in  grocery_store_name.gro_list:
        #print(l)

def add_store():
    store_name = input("Please enter store name    "   )
    store_desc = input("Please enter store description   ")
    shop = Store(store_name,store_desc)
    stores.append(shop)
    #this is a little superfluous but i needed it before i figured out index
    #store_names.append(grocery_store_name)


def add_produce():
    view_stores()
    try:
        store_id= int(input("Please input number of store  from list "))
        shop = (stores[store_id -1])
    
        if store_id > (len(stores)):
            print("please enter a valid list number")
        #view_stores()


        
        else:
    
    
       
            produce_item = input("please enter item ")
         
            produce_cost = float(input("please enter product cost  "))
            
            produce_quantity = int(input("please enter product quantity  "))

            grocery_item = Produce(produce_item,produce_cost,produce_quantity)
            shop.grocery_items.append(grocery_item)
            show_menu()
    except ValueError: 
        print("You need to enter a Number ")
show_menu()

while menu_entry != "q":
    menu_entry = input("Please enter choice   ")
    if menu_entry == "1":
        view_stores()
        add_store()
        #store_name = input("Please enter store name    "   )
        #store_desc = input("Please enter store description   ")
        #grocery_store_name = Store(store_name,store_desc)
        #stores.append(grocery_store_name)
        #store_names.append(store_name)
        view_shop()
        show_menu()
    
        
        
        


    elif menu_entry == "2":
       
        add_produce()
        view_stores()
        show_menu()

    elif menu_entry == "3":
        view_stores()
        
        show_menu()
#should put all the rest of this in a function 
        #produce_item = input("please enter item ")
        #produce_cost = input("please enter product cost  ")
        #produce_quantity = input("please enter product quantity  ")
        #grocery_item = Produce(produce_item,produce_cost,produce_quantity,store_list)
        #grocery_item.print_grocery()
        #grocery_store_name.grocery_items.append(grocery_item)
        #grocery_store_name.add_item(grocery_item)
        #grocery_store_name.store = store_list
        #grocery_store_name.add_item()

        

    elif menu_entry == "3":
        view_stores()
    #show_menu()



price_total_outside()
#sum_total()
#print(total)

#view_shop()
#view_stores()