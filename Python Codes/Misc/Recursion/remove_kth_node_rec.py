# Remove kth node of a linked list

class Node:
    def __init__(self,val,next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert(self,val):
        temp = Node(val)
        if not self.head:
            self.head = temp
        else:
            p = self.head
            while p.next:
                p = p.next
            p.next = temp
    
    def display(self):
        if not self.head:
            return
        p = self.head
        while p:
            print(p.val,end=" ")
            p = p.next
        print()


def remove(head,k):
    if k==1:
        head.next = head.next.next
        return
    res = remove(head.next,k-1)
    return res

ll = LinkedList()
for ele in [1,2,3,4,5]:
    ll.insert(ele)
ll.display()
k = 1
remove(ll.head,k-1)
ll.display()

