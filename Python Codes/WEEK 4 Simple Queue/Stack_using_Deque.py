#Implementing stack using Deque 

class Node:
    
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class StackDeque:

    def __init__(self):
        self.head = self.tail = None
    
    def is_empty(self):
        return True if not self.head else False

    def push(self,x):
        temp = Node(x)
        if not self.head:
            self.head = self.tail = temp
        else:
            temp.prev = self.tail
            self.tail.next = temp
            self.tail = temp
        print(f"{self.tail.data} pushed")

    def pop(self):
        
        if self.is_empty():
            return "Stack underflow!"
        p = self.tail
        self.tail = self.tail.prev
        self.tail.next = None
        data = p.data
        del p
        return data
    
    def top(self):
        if self.is_empty():
            return "Stack underflow!"
        return self.tail.data
    
    def display(self):
        q = self.tail
        print("show")
        while q!=None:
            print(f"{q.data} ",end="")
            q = q.prev
        print()
s = StackDeque()

s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.display()
print(-1,s.pop())
print(-1,s.pop())
s.display()
print(s.top())

    

