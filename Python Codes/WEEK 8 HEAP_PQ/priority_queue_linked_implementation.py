#Priority Queue Implementation using Linked List

class Node:
    def __init__(self,val,prior):
        self.val = val
        self.prior = prior
        self.next = None

class PriorityQueueLinkedList:
    def __init__(self):
        self.head = None
    
    def enqueue(self,val,prior):
        temp = Node(val,prior)
        if self.head == None:
            self.head = temp
            self.head.next = None
            return 1

        else:
            if prior>self.head.prior:
                temp.next = self.head
                self.head = temp
                return 1
            else:
                p = self.head
                while p.next:
                    if p.next.prior <= prior:
                        break
                    p = p.next
                temp.next = p.next
                p.next = temp
                return 1
            


    def peek(self):
        if not self.head:
            return None
        return self.head.val
    
    def dequeue(self):
        if not self.head:
            return None
        self.head = self.head.next
        return 1
    
    def print_pq(self):
        if not self.head:
            return None
        
        p = self.head

        while p:
            print(f"Value : {p.val}, Priority : {p.prior}")
            p = p.next
        
pq = PriorityQueueLinkedList()
pq.enqueue(1,4)
pq.enqueue(2,5)
pq.enqueue(0,5)
pq.enqueue(0,6)
pq.print_pq()

pq.dequeue()
pq.print_pq()
print(pq.peek())