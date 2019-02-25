

def perform_math_operation(): 
  print(1/1)
  no = int(input("Enter ONLY numbers: ")) 
  a = 10 
  b = 10 

#Exceptions 
try:
  perform_math_operation()  
  #print(1/1)
  #no = int(input("Enter ONLY numbers: ")) 
  #a = 10 
  #b = 10 
except ZeroDivisionError:
  print("You are diving by ZERO")
except ValueError: 
  print("Please input only numbers..")
except: 
  print("Opps somthing bad happened...")
# else and finally blocks are optional 
else: 
  print("No exception occured..")
  # finally is fired when there is an exception 
  # finally is fired when there is NO exception
  # finally block is usually used to clean up the resources 
finally: 
  print("finally block is fired no matter what.") 

print("No exception occured..")

# Most languages call it try catch block 

