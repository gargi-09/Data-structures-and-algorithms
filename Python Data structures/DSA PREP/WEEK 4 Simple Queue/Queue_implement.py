#Queue implementation
#Using List
from collections import deque

front = rear = None
def enqueue(q,ele):                 #Time complexity : O(1)
    q.append(ele)
    
    rear = q[-1]
    print(f"{q[-1]} has been inserted.")

def dequeue(q):                     #Time complexity : O(n)
    p=q.pop(0)
    front = q[0]
    print(f"{p} has been deleted from the queue.")

def front_rear(q):
    if front and rear:
        print(f"{front} is front.")
        print(f"{rear} is rear.")




#Using colections module
class Queue:

    def __init__(self):
        self.buffer = deque()

    def enqueue(self,val):
        self.buffer.appendleft(val)

    def dequeue(self):
        self.buffer.pop()

    def is_empty(self):
        return len(self.buffer) == 0
    
    def size(self):
        return len(self.buffer)
    
    def print_queue(self):
        
        for q in self.buffer:
            print(f"{q} ",end="")
        print()


q = Queue()

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)

q.print_queue()

q.dequeue()
q.dequeue()
q.dequeue()

q.print_queue()