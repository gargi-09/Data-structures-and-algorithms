# Find middle element of a linked list recursively
import print_alt_nodes as p

def middle_element(head,l,k):
    if not head:
        return head
    if k==l//2:
        return head
    else:
        return middle_element(head.next,l,k+1)

def length(head):
    if not head:
        return 0
    else:
        return length(head.next)+1
    
head = p.Node(1)
for i in [2,3,4,5,6]:
    p.insert(head,i)

p.display(head)
l = length(head)
node = middle_element(head,l,0)
print(node.val)
