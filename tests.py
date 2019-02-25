import time
import datetime
import json
from datetime import date
today = date.today()
pool_tables = []
pool_tables_as_dict = []


class Pooltable:
    def __init__(self,table_number):
        self.table_number = table_number
        self.occupied = False
        self.start_time= 0
        self.end_time = 0
        self.elapsed_time = 0
        self.float_start_time = time.time()
        self.float_end_time = time.time()
        self.use_count = 0
        self.total_use_time = 0
        self.revenue = 0

    def revenue_per_table(self):
        self.revenue = self.total_use_time * .5 



    def assign_table(self):
        #self.check_table() gets overridden so ignoring for now 
        self.occupied = True
        print("*******************************************")
        print(f"Table {self.table_number} is Now Assigned")
        print("*******************************************")
        now= datetime.datetime.now()    
        self.start_time= now.strftime("%H:%M:%S")
        self.float_start_time = time.time()#time.asctime( time.localtime(time.time()) )
        print(f"start time is {self.start_time}")
        #self.start_time = start_time
        

    def release_table(self):
        #self.check_table()# this is being overridden when in assign table 
        self.occupied = False
        print("*******************************************")
        print(f"Table {self.table_number} is Now Available")
        print("*******************************************")
        now= datetime.datetime.now()
        self.end_time = now.strftime("%H:%M:%S") #time.asctime( time.localtime(time.time()) )
        self.float_end_time = time.time()#time.asctime( time.localtime(time.time()) )
        print(f" Table free at {self.end_time}")
        self.time_occupied()
        self.total_use_time += self.elapsed_time
        self.use_count += 1
        self.revenue_per_table()


    

            

    def time_occupied(self):
        int_elapsed_time = (self.float_end_time - self.float_start_time)/60
        self.elapsed_time = round(int_elapsed_time) #seems like an unnecessary stap
        #print(f" Table has been in use for {round(self.elapsed_time/60 ,)} minutes ")
        print(f" Table {self.table_number} has been in use since {self.start_time} for {self.elapsed_time} Minutes")
        #print(f' Table {self.table_number} has been used {self.use_count} times for a total of {self.total_use_time} minutes')
    def as_string(self):
        return "\nTable #: {0}\nStart time: {1}\nEnd time: {2}\nTotal time: {3} minutes\nTimes used {4}\n\n" .format(self.table_number,self.start_time,self.end_time,self.total_use_time, self.use_count)

    def use_counter(self):
        self.time_occupied()
a= int(input("input number of tables"))+1

for index in range (1,a):
    table = Pooltable(index)
    pool_tables.append(table)
    pool_tables_as_dict.append(table.__dict__)

    print([pool_tables_as_dict])


pool_tables_as_dict.append(table.__dict__)
with open(f"{today}.json", "w") as file_object:
    json.dump(pool_tables_as_dict,file_object, indent=2)