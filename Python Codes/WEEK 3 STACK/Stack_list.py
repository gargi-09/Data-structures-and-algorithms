#Stack Implementation

class Stack:
    
    def __init__(self,stacklst):
        self.stacklst=stacklst
        self.top=self.stacklst[-1]

    def __str__(self):
        if self.stacklst==[]:
            return "Empty stack!"
        
        return f"TOP: {self.top}.\nLIST: {self.stacklst}"

    def push(self,data):
        
        self.stacklst.append(data)
        self.top=self.stacklst[-1]


    def pop(self):
        if self.stacklst==[]:
            print("Stack underflow. Insert first!")
            return
        self.top=self.stacklst[-2]
        self.stacklst.pop()

    def display(self):
        if self.stacklst==[]:
            print("stack underflow. Insert first!")
            return
        print("TOP-->",end=" ")
        for x in self.stacklst[::-1]:
            print(x)
            print("       ",end="")
        print()

    def search(self):
        pass

    def update(self,data):
        if self.stacklst==[]:
            print("Stack underflow.Insert first!")
            return
        self.stacklst[-1]=data
        self.top=self.stacklst[-1]


stack=Stack([7,8,9])
print(stack)
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)
stack.display()
stack.pop()
stack.pop()
stack.display()
stack.update(10)
stack.display()