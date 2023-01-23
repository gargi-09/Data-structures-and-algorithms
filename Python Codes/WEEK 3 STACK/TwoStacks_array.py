#Implementing two stacks using an array
import math
class TwoStacks:

    def __init__(self,n):

        self.size = n
        self.array = [None]*n
        self.top1 = math.floor(n/2)+1
        self.top2 = math.floor(n/2)

    def push1(self, x):

        if self.top1 > 0:
            self.top1-=1
            self.array[self.top1] = x
        else:
            print("stack overflow!")

    def push2(self,x):

        if self.top2 < self.size-1:
            self.top2+=1
            self.array[self.top2] = x
        else:
            print("stack overflow!")
    
    def pop1(self):

        if self.top1<=self.size/2:
            x = self.array[self.top1]
            self.top1+=1
            return x
        else:
            print("stack underflow!")
    
    def pop2(self):

        if self.top2 >= math.floor(self.size/2)+1:
            x = self.array[self.top2]
            self.top2-=1
            return x
        else:
            print("stack underflow!")
    
    def display1(self):

        if self.top1 == math.floor(self.size/2)+1:
            print("empty")
            return
        
        for i in range(0,math.floor(self.size/2)+1):
            print(f"{self.array[i]} ",end="")
        
        print()
    
    def display2(self):
        
        if self.top2 == math.floor(self.size/2):
            print("empty")
            return
        
        for i in range(math.floor(self.size/2)+1,self.size):
            print(f"{self.array[i]} ",end="")
        
        print()

ts = TwoStacks(10)

ts.push1(1)
ts.push1(2)
ts.push1(3)
ts.push1(4)

ts.push2(10)
ts.push2(20)
ts.push2(30)
ts.push2(40)
ts.display2()
print(-1,ts.pop1())
print(-1,ts.pop1())
print(-2,ts.pop2())
print(-2,ts.pop2())

ts.display1()
ts.display2()
