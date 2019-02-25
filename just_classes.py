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


    def all_prices_total(self):
        



    #def add_item(self):
     #   self.grocery_items.append()
      


    


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

heb = Store("heb","tex")
heb.print_store()

grocery_item = Produce("produce_item0",11,"produce_quantity")
grocery_item3 = Produce("produce_item1",2,"produce_quantity")
grocery_item2 = Produce("produce_item2",4,"produce_quantity")
grocery_item1 = Produce("produce_item3",5,"produce_quantity")
grocery_item4 = Produce("produce_item4",4,"produce_quantity")

#print(grocery_item.price)
#test print of first privc entered

heb.grocery_items.append(grocery_item)
heb.grocery_items.append(grocery_item1)
heb.grocery_items.append(grocery_item2)
heb.grocery_items.append(grocery_item3)
heb.grocery_items.append(grocery_item4)

#print out of shoppping list
for grocery_item in heb.grocery_items:
      print(f"  {grocery_item.item} - {grocery_item.price} - {grocery_item.quantity}")

#calls function price total which totals the costs 

heb.price_total()

#print(f"{heb.grocery_items.grocery_item.price}")