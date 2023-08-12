# Print Alternate Nodes in linked list using Recursion

class Node:
    def __init__(self,val,next=None):
        self.val = val
        self.next = next

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

def alt_nodes(head):
    if not head:
        print()
        return
    print(head.val,end=" ")
    if head and head.next:
        alt_nodes(head.next.next)

# head = Node(1)
# for i in [2,3]:
#     insert(head,i)
# display(head)
# alt_nodes(head)