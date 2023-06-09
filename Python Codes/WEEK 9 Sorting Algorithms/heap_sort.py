#Heap Sort Implementation

class Heap:

    def __init__(self,maxsize):
        self.maxsize = maxsize
        self.arr = [0]*self.maxsize
        self.heapsize=0
    
    def l_child(self,ind):
        return (ind*2+1)
    
    def r_child(self,ind):
        return (2*ind+2)
    
    def parent(self,ind):
        return (ind-1)//2
    
    def insert(self,val):
        self.heapsize+=1
        i = self.heapsize-1
        self.arr[i] = val

        while i!=0 and self.arr[self.parent(i)]<self.arr[i]:
            temp = self.arr[i]
            self.arr[i] = self.arr[self.parent(i)]
            self.arr[self.parent(i)] = temp

            i = self.parent(i)
    
    def heapify(self,i):
        largest = i
        l = self.l_child(i)
        r = self.r_child(i)

        if l<self.heapsize and self.arr[largest]<self.arr[l]:
            largest = l
        
        if r<self.heapsize and self.arr[largest]<self.arr[r]:
            largest=r
        
        if largest!=i:
            temp = self.arr[i]
            self.arr[i] = self.arr[largest]
            self.arr[largest] = temp

            self.heapify(largest)
    
    def remove_max(self):
        if self.heapsize == 1:
            self.heapsize-=1
            val = self.arr.pop()
            return val
        
        root = self.arr[0]
        self.arr[0]=self.arr[self.heapsize-1]
        self.heapsize-=1
        self.arr.pop()

        self.heapify(0)

        return root
    
    def heap_sort(self):
    
        output = []
        for i in range(self.maxsize):
            val = self.remove_max()
            output.append(val)
        return output[::-1]


arr = [9,1,2,5,10,0,4]
heap = Heap(len(arr))
for i in arr:
    heap.insert(i)

print(heap.heap_sort())

