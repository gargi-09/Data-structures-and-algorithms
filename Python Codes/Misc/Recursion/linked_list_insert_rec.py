# Linked List Insertion using recursion

class Node:
    def __init__(self,val,next=None):
        self.val = val
        self.next = next
    
class LinkedList:
    def __init__(self):
        self.head = None
    
def insert(head,val):
    if not head:
        head = Node(val)
    else:
        head.next = insert(head.next,val)
    return head

def display(head):
    if not head:
        print()
        return
    print(head.val,end=" ")
    display(head.next)

def search(head,val):
    if not head:
        return False
    if head.val==val:
        return True
    else:
        return search(head.next,val)

def deletelist(head):
    if head==None:
        return
    elif head.next==None:
        head = None
        return
    elif head.next:
        head.next = head.next.next
        deletelist(head)

ll = LinkedList()
ll.head = insert(ll.head,1)
ll.head = insert(ll.head,2)
ll.head = insert(ll.head,3)
display(ll.head)
print(search(ll.head,0))
ll.head = deletelist(ll.head)
display(ll.head)

    
