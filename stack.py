stacks=[]

stacks_as_dict=[]

class Stack:
    def __init__(self,):
        self.stack = []
        

    def push(self,value):
        self.stack.append(value)
        for value in self.stack:
            #print(value)
            print(self.stack)


    def pop(self):
        #this just deletes the value not much use really
        for id in range(0, len(self.stack)):
            print(len(self.stack))
            id = len(self.stack)-1
            del self.stack[id]
            print(self.stack)


    def pop1(self):
        x =self.stack.pop()
        print(x)
       
        print(self.stack)
for index in range(1,4):
    
    stack = Stack(index)
    stacks.append(stack)
    stacks_as_dict.append(stack.__dict__)






test = Stack()

test.push(3)
test.push(4)

#test.pop()
#test.pop()

test.pop1()
test.pop1()



class Queue:
    def __init__(self):
        self.queue = []

    def enque(self,value):
        
        self.queue.insert(0,value)
        for value in self.queue:
            print(value)
            print(self.queue)

    def deque(self):
        x =self.queue.pop()
        print(x)
       
        print(self.queue)

for index in range (1,3):
    stack = Queue(index)
    stacks.append(stack)
    stacks_as_dict.append(stack.__dict__)
test2 = Queue()
test2.enque(1)
test2.enque(2)
test2.enque(3)
test2.enque(4)

test2.deque()
test2.deque()
test2.deque()
test2.deque()
