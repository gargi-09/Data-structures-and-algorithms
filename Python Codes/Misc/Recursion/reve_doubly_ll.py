# Reverse a doubly linked list using recursion

class Node:
    def __init__(self,val,next=None,prev=None):
        self.val = val
        self.prev = prev
        self.next = next

def reverse(head):
    if not head:
        return None

    head.prev,head.next = head.next,head.prev
    if head.prev is None:
        return head
    return reverse(head.prev)

def insert(head,val):
    if not head:
        head = Node(val)
    if not head.next:
        temp = Node(val)
        head.next = temp
        temp.prev = head
    else:
        head.next = insert(head.next,val)
    return head

def display(head):
    if not head:
        print()
        return
    print(head.val,end=" ")
    display(head.next)

def reverse_display(head):
    if not head:
        print()
        return
    print(head.val,end=" ")
    reverse_display(head.prev)

head = Node(1)
for ele in [2,3,4,5]:
    insert(head,ele)
display(head)
head = reverse(head)
display(head)

