#Pool table app

import time
import datetime
import json

pool_tables = []

localtime = time.asctime( time.localtime(time.time()) )
print ("Local current time :", localtime)
print((datetime.datetime.now()))



class Pooltable:
    def __init__(self,table_number):
        self.table_number = table_number
        self.occupied = False
        self.start_time= datetime.datetime.now()
        self.end_time = datetime.datetime.now()
        self.elapsed_time = 0
        self.float_start_time = time.time()
        self.float_end_time = time.time()
        self.use_count = 0
        self.total_use_time = 0
    

    def assign_table(self):
        #self.check_table() gets overridden so ignoring for now 
        self.occupied = True
        print(f"Table {self.table_number} is Now Assigned")
        start_time = datetime.datetime.now()    
        self.float_start_time = time.time()#time.asctime( time.localtime(time.time()) )
        print(f"start time is {start_time}")
        self.start_time = start_time
        

    def release_table(self):
        #self.check_table()# this is being overridden when in assign table 
        self.occupied = False
        print(f"Table {self.table_number} is Now Available")
        self.end_time = datetime.datetime.now()#time.asctime( time.localtime(time.time()) )
        self.float_end_time = time.time()#time.asctime( time.localtime(time.time()) )
        print(f" Table free at {self.end_time}")
        self.time_occupied()
        self.total_use_time += self.elapsed_time
        self.use_count += 1


    

            

    def time_occupied(self):
        int_elapsed_time = (self.float_end_time - self.float_start_time)/60
        self.elapsed_time = round(int_elapsed_time ,2) #seems like an unnecessary stap
        #print(f" Table has been in use for {round(self.elapsed_time/60 , 2)} minutes ")
        print(f" Table {self.table_number} has been in use since {self.start_time} for {self.elapsed_time} Minutes")
        #print(f' Table {self.table_number} has been used {self.use_count} times for a total of {self.total_use_time} minutes')
    def as_string(self):
        return "\nTable #: {0}\nStart time: {1}\nEnd time: {2}\nTotal time: {3} minutes\n #Times used {4}" .format(self.table_number,self.start_time,self.end_time,self.total_use_time, self.use_count)

    def use_counter(self):
        self.time_occupied()


    
def check_table():# this is being overridden when in assign table forgetting about it for now
    for index in range(0, len(pool_tables)):
        
        table = pool_tables[index]
       
    table_id= int(input("Please input number of Table from list "))
    table = (pool_tables[table_id -1])
    if table.occupied == True: 
        print("The table is already occupied")
        show_menu()
            
            

def show_menu():
    print("press 1 to view  table status")
    print("press 2 to assign table ")
    print("press 3 to release table ")
    print("press 4 to view in use time ")
    print("press q ")        
              
def select_table_assign():
    try:
        for index in range(0, len(pool_tables)):
        
            table = pool_tables[index]
       
        table_id= int(input("Please input number of Table from list "))
        table = (pool_tables[table_id -1])
        #add the check function in here 
        if table.occupied == True:
            print ("That table is already assigned")
    except ValueError:
        print("Enter a number") 

    else :

        table.assign_table()
    #print(f"Please select table - ")

def select_table_release():
    for index in range(0, len(pool_tables)):
        
        table = pool_tables[index]
       
    table_id= int(input("Please input number of Table from list "))
    table = (pool_tables[table_id -1])
    if table.occupied == False:
        print ("That table is already Open")
        

    else :
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
                        
def write_all_out():
    for table in pool_tables:
        print(f' Table {table.table_number} has been used {table.use_count} times for a total of {table.total_use_time} minutes')#if table.occupied == False:
        #print(f"Table Number {table.table_number}   {table.elapsed_time}'     '  {table.start_time} is Free")
        with open ("pool1.txt ","a") as file_object:
            #writes the table out to text file 
            file_object.write(table.as_string())
        
            #json.dump(x,file_object)


def view_update_in_use_time():
    for table in pool_tables:
        if table.occupied == True :
            table.float_end_time = time.time()
            table.time_occupied()


def clear_all_tables_release():
    for table in pool_tables:

        if table.occupied == True:
            table.release_table()
            print ("closing all tables")


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
        #check_table()
        view_table_status_free()
        select_table_assign()
        #view_table_status()

    elif menu_entry == "3":
        view_table_status_occupied()
        select_table_release()
        view_table_status()
        #view_all_out(
    elif menu_entry == "4":
        view_update_in_use_time()
    
    


clear_all_tables_release()
view_update_in_use_time()
#table.as_string()  

write_all_out()      











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


