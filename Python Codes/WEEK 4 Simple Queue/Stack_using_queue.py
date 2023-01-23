#Stack implementation using Queues

from collections import deque

class StackQueueMethodOne:

    def __init__(self):
        self.queue1 = deque()
        self.queue2 = deque()

    def push(self,x):           #Time complexity : O(N)

        self.queue2.append(x)

        while self.queue1:
            self.queue2.append(self.queue1.popleft())
        
        self.queue1, self.queue2 = self.queue2, self.queue1

        print(self.queue1)

    def pop(self):          #Time complexity : O(1)

        if self.queue1:
            return self.queue1.popleft()
    
    def top(self):
        if self.queue1:
            return self.queue1[0]
        
class StackQueueMethodTwo:

    def __init__(self):
        self.queue1 = deque()
        self.queue2 = deque()

    def push(self,x):          #Time complexity : O(1)
        self.queue1.append(x)
        print(self.queue1)

    def pop(self):              #Time complexity : O(N)

        while len(self.queue1) != 1:
            self.queue2.append(self.queue1.popleft())
        
        x = self.queue1.popleft()

        self.queue1, self.queue2 = self.queue2, self.queue1

        return x
    
    def top(self):           #Time Complexity : O(N)
        
        while len(self.queue1) != 1:
            self.queue2.append(self.queue1.popleft())
        
        top = self.queue1[0]
        self.queue2.append(self.queue1.popleft())

        self.queue1, self.queue2 = self.queue2, self.queue1

        return top
    
    def size(self):
        return len(self.queue1)
    
q = StackQueueMethodTwo()

q.push(1)
q.push(2)
q.push(3)
q.push(4)

print(q.pop())
print(q.pop())
print(q.pop())
