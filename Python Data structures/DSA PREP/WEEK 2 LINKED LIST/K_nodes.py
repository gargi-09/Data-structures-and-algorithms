#Time complexity=O() and space complexity=O()

class Node:
    def __init__(self,data=None,next=None,prev=None):
        self.data=data
        self.next=next
        self.prev=prev

class LinkedList:
    def __init__(self):
        self.head=None

    def display(self):              
        if self.head is None:
            return "Head is Null.Insert First!"
        p=self.head
        while p!=None:
            print(f"-->{p.data}",end='')
            p=p.next
        print()
    
    def k_nodes(self,k):
        while k>0:
            data=int(input("Enter the data:"))
            temp=Node(data)
            if self.head is None:
                self.head=temp
            else:
                p=self.head
                while p.next!=None:
                    p=p.next
                p.next=temp
            k-=1

ll=LinkedList()
ll.k_nodes(2)
ll.display()
ll.k_nodes(4)
ll.display()