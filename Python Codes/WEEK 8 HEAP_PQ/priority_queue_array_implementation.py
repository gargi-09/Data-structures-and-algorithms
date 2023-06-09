#Priority Queue Implementation
#Using Arrays
import sys

class item:
    def __init__(self,value,priority):
        self.value = value
        self.priority = priority

class PriorityQueueArray:
    def __init__(self):
        self.arr = [None]*100000
        self.size = -1
    
    def enqueue(self,val,priority):
        self.size+=1
        self.arr[self.size] = item(val,priority)

    def peek(self):
        if self.size==-1:
            return None
        highest_p = -sys.maxsize
        ind = -1
        i=0
        while i<=self.size:
            if highest_p==self.arr[i].priority and ind>-1 and self.arr[ind].value<self.arr[i].value:
                highest_p = self.arr[i].priority
                ind = i
            elif highest_p<self.arr[i].priority:
                highest_p=self.arr[i].priority
                ind = i
            i+=1
        return ind
    
    def dequeue(self):
        if self.size==-1:
            return None
        
        ind = self.peek()

        while ind<=self.size:
            self.arr[ind]=self.arr[ind+1]
            ind+=1
        self.size-=1
    def print_pq(self):
        
        for item in self.arr[:self.size+1]:
            print(f"Value:{item.value} Priority:{item.priority}")
pq = PriorityQueueArray()
pq.enqueue(1,4)
pq.enqueue(2,5)
pq.enqueue(0,5)
pq.enqueue(0,6)
pq.print_pq()
print(pq.arr[pq.peek()].value)

pq.dequeue()
pq.print_pq()
print(pq.arr[pq.peek()].value)