#METHOD - 1, Making enqueue costly
#Space Complexity : O(N)

class QueueMethodOne:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    
    def  enqueue(self,val):     #Time complexity : O(N)
        
        while len(self.stack1)!=0:
            self.stack2.append(self.stack1[-1])
            self.stack1.pop()
        
        self.stack1.append(val)

        while len(self.stack2)!=0:
            self.stack1.append(self.stack2[-1])
            self.stack2.pop()
    
    def dequeue(self):      #Time Complexty : O(1)
        if len(self.stack1) == 0:
            print("Queue is empty.")
            return
        return self.stack1.pop()
    
    def is_empty(self):
        return True if len(self.stack1)==0 else False
    
    def peek(self):
        if self.is_empty():
            print("Queue is empty.")
            return
        while len(self.stack1)!=0:
            self.stack2.append(self.stack1[-1])
            self.stack1.pop()

        peekele=self.stack2[-1]

        while len(self.stack2)!=0:
            self.stack1.append(self.stack2[-1])
            self.stack2.pop()
        return peekele
    
    def print_q(self):
        if self.is_empty():
            return
        print(self.stack1[::-1])
        return
    
class QueueMethodTwo:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self,val):
        self.stack1.append(val)
    
    def dequeue(self):
        if len(self.stack1) == 0 and len(self.stack2) == 0:
            print("Queue is empty!")
            return
        elif len(self.stack2) == 0 and len(self.stack1)>0:
            while len(self.stack1)!=0:
                self.stack2.append(self.stack1[-1])
                self.stack1.pop()
            x = self.stack2.pop()
            
            while len(self.stack2)!=0:
                self.stack1.append(self.stack2[-1])
                self.stack2.pop()
            return x
    
    def is_empty(self):
        return True if len(self.stack1) == 0 else False
    
    def peek(self):
        if self.is_empty():
            print("Queue is Empty!")
            return
        while len(self.stack1)!=0:
            self.stack2.append(self.stack1[-1])
            self.stack1.pop()
        
        x = self.stack2[-1]
        
        while len(self.stack2)!=0:
            self.stack1.append(self.stack2[-1])
            self.stack2.pop()
        return x
    
    def print_q(self):
        if self.is_empty():
            print("Queue is Empty!")
            return
        print(self.stack1[::-1])

q = QueueMethodTwo()

print(q.is_empty())
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)

print(q.dequeue())
print(q.dequeue())
print(q.dequeue())

print(q.is_empty())
print(-1,q.peek())
q.print_q()


























""""
q = QueueMethodOne()

#q.dequeue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
q.print_q()
q.dequeue()
q.peek()
q.print_q()

"""