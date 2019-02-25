


class Calculator:
    def __init__(self):
        self.input1 =  1
        self.input2 = 1
        self.operator = ""

    def calculator(self):

        if self.operator == "+":
            print(self.input1 + self.input2)
        elif self.operator == "-":
            print(self.input1 - self.input2)
        elif self.operator == "*":
            print(self.input1 * self.input2)
        elif self.operator == "/":
            print(self.input1 / self.input2)
        else:
            print("Sorry invalid input!")
            
    def add(self):
        return self.input1 + self.input2 

    def input_functions(self):
        self.input1 =  int(input("Enter first number: "))
        self.input2 =  int(input("Enter second number: "))
        self.operator = input("Enter operator (+,-,*,/): ")




    
times=Calculator
times.input_functions()
times.calculator()