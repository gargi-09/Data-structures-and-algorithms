#Priority Queue Implementation using Heaps

class Item:
    def __init__(self,val,prior):
        self.val = val
        self.prior = prior

class PriorityQueueHeap:
    def __init__(self,maxsize):
        self.maxsize = maxsize
        self.arr = [None]*maxsize
        self.heapsize=0

    def parent(self,ind):
        return (ind-1)//2
    
    def l_child(self,ind):
        return (2*ind+1)
    
    def r_child(self,ind):
        return (2*ind+2)
    
    def max_heapify(self,ind):
        if self.heapsize==0:
            return None
        largest = ind
        l = self.l_child(ind)
        r = self.r_child(ind)

        if l<self.heapsize and self.arr[largest].prior<=self.arr[l].prior:
            largest = l
        
        if r<self.heapsize and self.arr[largest].prior<=self.arr[r].prior:
            largest = r
        
        if largest!=ind:
            temp = self.arr[ind]
            self.arr[ind] = self.arr[largest]
            self.arr[largest] = temp
            self.max_heapify(largest)
    def enqueue(self,val,prior):
        temp = Item(val,prior)
        self.heapsize+=1
        i = self.heapsize-1
        self.arr[i] = temp

        while i!=0 and self.arr[self.parent(i)].prior<self.arr[i].prior:
            node = self.arr[i]
            self.arr[i] = self.arr[self.parent(i)]
            self.arr[self.parent(i)] = node

            i = self.parent(i)
    
    def peek(self):
        if self.heapsize==0:
            return None
        return self.arr[0].val

    def dequeue(self):
        if self.heapsize == 0:
            return None
        if self.heapsize==1:
            self.heapsize-=1
            return self.arr[0]
        root = self.arr[0].val
        self.arr[0] = self.arr[self.heapsize-1]
        self.heapsize-=1
        self.max_heapify(0)
    
    def print_heap(self):
        if self.heapsize == 0:
            return None
        
        for i in range(self.heapsize):
            l = self.l_child(i)
            r = self.r_child(i)

            if l<self.heapsize or r<self.heapsize:
                print(f"{self.arr[i].val},{self.arr[i].prior}")
            if l<self.heapsize:
                print(f"--{self.arr[l].val}, {self.arr[l].prior}")
            
            if r<self.heapsize:
                print(f"--{self.arr[r].val}, {self.arr[r].prior}")

pq = PriorityQueueHeap(10)

pq.enqueue(1,4)
pq.enqueue(2,5)
pq.enqueue(0,5)
pq.enqueue(0,6)
pq.enqueue(4,6)
pq.print_heap()