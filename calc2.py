#calculator app
#need three inputs from user in one statement
# better with num1 = int(input("enter number"))
# decided to create functions that could be called later but for this exercise it was too wordy 

class Calculator:

    
    def __init__(self):
        
        self.num1 = 0
        self.num2 = 0
        self.operator = ""

    def menu(self):

        self.num1 = input("Please enter a number: ")
        self.oper = input("please enter operand +,-,/ or *: ")
        self.num2 = input ("please enter second number: ")

#set up functions
    def add(self):
         print (int(self.num1) + int(self.num2))

    def sub(self):
        print(int(self.num1) - int(self.num2))

    def divide(self):
        print(int(self.num1) / int(self.num2))


    def mult(self):
        print(int(self.num1) * int(self.num2))

# check the operand to see which function to use elifs would use less resources
# could have done all this in one go
    def calculate(self):
        if self.oper == "+":
            add(self)
    
        elif self.oper == "*":
            mult(self)

        elif self.oper == "-":
            sub(self)

        elif self.oper == "/":
            divide(self)

times = Calculator()
times.menu()
times.calculate()
