#Implementing Queue using Deque

class Node:

    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
    
class QueueDeque:

    def __init__(self):
        self.head = self.tail = None
    
    def is_empty(self):
        return True if not self.head else False
    
    def enqueue(self, x):
        temp = Node(x)
        if self.is_empty():
            self.head = self.tail = temp
            return
        temp.prev = self.tail
        self.tail.next = temp
        self.tail = temp
    
    def dequeue(self):

        if self.is_empty():
            return "Queue is empty!"
        p = self.head
        self.head = self.head.next
        self.head.prev = None
        data = p.data
        del p
        return data
    
    def peek(self):

        if self.is_empty():
            return "Queue is empty!"
        return self.head.data
    
    def display(self):
        q = self.head

        while q:
            print(f"{q.data} ",end="")
            q = q.next
        print()
    
q = QueueDeque()
print(q.is_empty())
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)

q.display()

print(q.dequeue())
print(q.dequeue())

q.display()

print(-1,q.peek())