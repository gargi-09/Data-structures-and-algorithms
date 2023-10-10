# Optimal Merge Pattern Implementation

class MinHeap:
    def __init__(self):
        self.heap = []
    
    def parent(self,i):
        return (i-1)//2
    
    def l_child(self,i):
        return (2*i+1)
    
    def r_child(self,i):
        return (2*i+2)
    
    def insert(self,val):
        self.heap.append(val)

        if len(self.heap)==1:
            return
        
        ind = len(self.heap)-1
        while ind!=0 and self.heap[ind]<self.heap[self.parent(ind)]:
            self.heap[ind],self.heap[self.parent(ind)] = self.heap[self.parent(ind)],self.heap[ind]
            ind = self.parent(ind)
            
    def delete(self):
        if len(self.heap)==0:
            return
        n = len(self.heap)
        self.heap[0],self.heap[n-1] = self.heap[n-1],self.heap[0]
        deleted = self.heap.pop()
        self.heapify(0)
        return deleted
    
    def heapify(self,i):
        smallest = i
        n = len(self.heap)
        l = self.l_child(i)
        r = self.r_child(i)
        if l<n and self.heap[l]<=self.heap[smallest]:
            smallest = l
        if r<n and self.heap[r]<=self.heap[smallest]:
            smallest = r
        if smallest!=i:
            self.heap[smallest],self.heap[i] = self.heap[i],self.heap[smallest]
            self.heapify(smallest)

def optimal_merge_pattern(files,n):
    if n<=0:
        return 0
    if n==1:
        return files.heap[0]
    count = 0
    while len(files.heap)!=1:
        temp1 = files.delete()
        temp2 = files.delete()
        count+=(temp1+temp2)
        files.insert(temp1+temp2)
    return count  
  
pq = [2, 3, 4, 5, 6, 7]
h = MinHeap()
for num in pq:
    h.insert(num)
print(optimal_merge_pattern(h,len(h.heap)))


