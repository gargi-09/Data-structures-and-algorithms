# Split a linked list into two such that they have alternating nodes

import print_alt_nodes as pan

def split_ll(head,head1,head2,isOdd):
    if not head:
        return head1,head2
    if isOdd:
        pan.insert(head1,head.val)
        return split_ll(head.next,head1.next,head2,False)
    else:
        pan.insert(head2,head.val)
        return split_ll(head.next,head1,head2.next,True)


head = pan.Node(1)
for ele in [2,3,4,5,6,7]:
    pan.insert(head,ele)

pan.display(head)
head1 = pan.Node(0)
head2 = pan.Node(0)
split_ll(head,head1,head2,True)
pan.display(head1.next)
pan.display(head2.next)