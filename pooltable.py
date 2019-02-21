#Pool table app

import time
import datetime

pool_tables = []

localtime = time.asctime( time.localtime(time.time()) )
print ("Local current time :", localtime)
print((datetime.datetime.now()))



class Pooltable:
    def __init__(self,table_number):
        self.table_number = table_number
        self.occupied = False
        self.start_time= 0
        self.end_time = 0
        self.elapsed_time = 0
        self.float_start_time = 0
        self.float_end_time = 0
    

    def assign_table(self):
        #self.check_table()
        #assign_table = input(f"Do you wish to Play or End Game {self.table_number}? P/E ").lower() 
             
        
        #assign_table == "p":
        self.occupied = True
        print(f"Table {self.table_number} is Now Assigned")
        start_time = (datetime.datetime.now())
            
        self.float_start_time = time.time()#time.asctime( time.localtime(time.time()) )
        print(f"start time is {start_time}")
        #print(float_start_time)
        self.start_time = start_time
        

    def release_table(self):# this is being overridden when in assign table 
        #self.check_table()
        #assign_table == "e": #release_table =="y":
        #assign_table == "r" or release_table =="y":
        self.occupied = False
        print(f"Table {self.table_number} is Now Available")
        end_time = datetime.datetime.now()#time.asctime( time.localtime(time.time()) )
        self.float_end_time = time.time()#time.asctime( time.localtime(time.time()) )
        print(f" Table free at {end_time}")
        #print(float_end_time)
        self.end_time = end_time
        self.time_occupied()
        
            

    def time_occupied(self):
        self.elapsed_time = self.float_end_time - self.float_start_time
        print(self.elapsed_time)

    def check_table(self):# this is being overridden when in assign table 
        if self.occupied == True: 
            print("The table is occupied")
            release_table = input("do you wish to release table? Y/N").lower()
            if release_table == "y":
                float_end_time = time.time()
                self.occupied = False
                self.end_time = float_end_time
                print(self.end_time)
                print(datetime.datetime.now)
            elif release_table == "n":
                
                self.occupied = True
                #print(" This table is already vacant")
                #float_end_time = time.time()#time.asctime( time.localtime(time.time()) )
        #elif self.occupied == False:
         #   print(" This table is already vacant")

                #self.end_time = float_end_time dont reset timer in this instance

def show_menu():
    print("press 1 to view  table status")
    print("press 2 to assign table")
    print("press 3 to release table ")
    print("press q ")        
              
def select_table_assign():
    for index in range(0, len(pool_tables)):
        
        table = pool_tables[index]
       
    table_id= int(input("Please input number of Table from list "))
    table = (pool_tables[table_id -1])
    table.assign_table()
    #print(f"Please select table - ")

def select_table_release():
    for index in range(0, len(pool_tables)):
        
        table = pool_tables[index]
       
    table_id= int(input("Please input number of Table from list "))
    table = (pool_tables[table_id -1])
    table.release_table()
    #print(f"Please select table - ")

def view_table_status():
    for table in pool_tables:
        if table.occupied == False:
            print(f"Table Number {table.table_number} is Free")
        elif table.occupied == True:
            print(f"Table Number {table.table_number} is Occupied")

def view_table_status_free():
    for table in pool_tables:
        if table.occupied == False:
            print(f"Table Number {table.table_number} is Free")
        #elif table.occupied == True:
         #   print(f"Table Number {table.table_number} is Occupied")
    
def view_table_status_occupied():
    for table in pool_tables:
        #if table.occupied == False:
            #print(f"Table Number {table.table_number} is Free")
        if table.occupied == True:
            print(f"Table Number {table.table_number} is Occupied")
                        
def view_all_out():
    for table in pool_tables:
        #if table.occupied == False:
        print(f"Table Number {table.table_number} {table.elapsed_time}{table.start_time} is Free")






menu_entry = " "
print("Initializing Pool Tables")


for index in range (1,13):
    table = Pooltable(index)
    pool_tables.append(table)


while menu_entry != "q":
    show_menu()
    menu_entry = input("Please enter choice   ").lower()
    #start_day= input("Are we ready to use the app, ansewer Y for yes of q for quit.... ").lower()
    if menu_entry == "1":
        view_table_status()


    elif menu_entry == "2":
        view_table_status_free()
        select_table_assign()
        view_table_status()

    elif menu_entry == "3":
        view_table_status_occupied()
        select_table_release()
        view_table_status()
        #view_all_out()




    

view_all_out()       













#for table in pool_tables:
 #   if table.occupied == False:
  #      print(f"Table Number {table.table_number} is Free")
   # elif table.occupied == True:
    #    print(f"Table Number {table.table_number} is Occupied")



    #or table in pool_tables:
        #if table.occupied == False:
            #print(f"Table {table.table_number} is Free")
#view_table_status()
#select_table()
#view_table_status()
#select_table()
#view_table_status()
#select_table()


