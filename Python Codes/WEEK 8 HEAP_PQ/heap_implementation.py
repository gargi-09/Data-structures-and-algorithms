#Heap Implementation

class MaxHeap:
    
    def __init__(self,maxSize):
        self.maxsize = maxSize
        self.arr = [None]*maxSize
        self.heapsize = 0
    
    def l_child(self,ind):
        return (2*ind+1)
    
    def r_child(self,ind):
        return (2*ind+2)
    
    def parent(self,ind):
        return (ind-1)//2
    
    def max_heapify(self,i):
        left = self.l_child(i)
        right = self.r_child(i)
        largest = i

        if left<self.heapsize and self.arr[left]>self.arr[i]:
            largest = left
        if right<self.heapsize and self.arr[right]>self.arr[i]:
            largest = right
        if largest!=i:
            temp = self.arr[i]
            self.arr[i] = self.arr[largest]
            self.arr[largest] = temp
            self.max_heapify(largest)
        
    def remove_max(self):
        if self.heapsize==0:
            return None
        if self.heapsize==1:
            self.heapsize-=1
            return self.arr[0]
        
        root = self.arr[0]
        self.arr[0] = self.arr[self.heapsize-1]
        self.heapsize-=1
        self.max_heapify(0)

        return root
    
    def update_key(self,i,new_val):
        if self.heapsize==0:
            return None
        self.arr[i] = new_val
        while i!=0 and self.arr[self.parent(i)]<self.arr[i]:
            temp = self.arr[i]
            self.ar[i] = self.arr[self.parent(i)]
            self.arr[self.parent(i)] = temp
            i = self.parent(i)
        

    def insertKey(self,x):

        if self.heapsize == self.maxsize:
            return None
        
        self.heapsize+=1
        i = self.heapsize-1
        self.arr[i] = x

        while i!=0 and self.arr[self.parent(i)]<self.arr[i]:
            temp = self.arr[i]
            self.arr[i] = self.arr[self.parent(i)]
            self.arr[self.parent(i)] = temp
            i = self.parent(i)
        
    
    def search(self,key):
        if self.heapsize==0:
            return None
        for i in range(self.heapsize):
            l = self.l_child(i)
            r = self.r_child(i)
            if self.arr[i] == key:
                ans = i
                return ans
            if l<self.heapsize and self.arr[l] == key:
                ans = l
                return ans
            if r<self.heapsize and self.arr[r] == key:
                ans = r
                return ans
        return -1
    
    def delete(self,x):
        if self.heapsize==0:
            return None
        
        i = self.search(x)

        if i!=-1:
            temp = self.arr[i]
            self.arr[i] = self.arr[self.heapsize-1]
            self.arr[self.heapsize-1] = temp
            self.heapsize-=1
            rem = self.arr.pop()
            self.max_heapify(i)
            return rem
        else:
            return None
    
    def print_heap(self):
        if self.heapsize == 0:
            return None
        
        for i in range(self.heapsize):
            l = self.l_child(i)
            r = self.r_child(i)

            if l<self.heapsize or r<self.heapsize:
                print(self.arr[i])
            if l<self.heapsize:
                print(f"--{self.arr[l]}")
            
            if r<self.heapsize:
                print(f"--{self.arr[r]}")
        
    
heap = MaxHeap(10)

heap.insertKey(3)
heap.insertKey(10)
heap.insertKey(12)
heap.insertKey(8)
heap.insertKey(2)
heap.insertKey(14)

heap.print_heap()

heap.delete(14)
print("After deletion")
heap.print_heap()