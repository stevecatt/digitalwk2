



class Store:
    def __init__(self,store_name,store_description):
        self.store = store_name
        self.desc = store_description
        self.grocery_item= []

    def print_store(self):
        print(self.store, self.desc, self.grocery_item)

    def add_item(self):
        self..append()

    def price_total(self):
        list_price_total = 0
        for grocery_item in self.grocery_items:
        #for item in self.grocery_items.price():
            list_price_total += grocery_item.price
        print(list_price_total)    



heb = Store("heb","tex")
heb.print_store()


class Produce:
    def __init__(self,item,price,quantity,store):
        self.item=item
        self.price=price
        self.quantity=quantity
        self.store = store

    def print_grocery(self):
        print(f"{self.store} {self.item} $ {self.price} Qty {self.quantity}")
        #print(self.item)


 
grocery_item = Produce("produce_item","produce_cost","produce_quantity","store_list")
for grocery_item in heb.grocery_items:
      print(f"  {grocery_item.name} - {grocery_item.price} - {grocery_item.quantity}")
#heb.add_item(grocery_item)
