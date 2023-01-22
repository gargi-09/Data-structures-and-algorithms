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

    def create_list(self):          
        n=1
        while n!=0:
            data=int(input("Enter data:"))
            temp=Node(data)
            if self.head is None:
                temp.next=None
                self.head=temp
            else:
                p=self.head
                while p.next!=None:
                    p=p.next
                p.next=temp
            n=int(input("If you want to continue press 1 else 0:"))
    
    def insert_at_the_end(self,data):       
        temp=Node(data)
        if self.head is None:
            temp.next=None
            self.head=temp
        else:
            p=self.head
            while p.next!=None:
                p=p.next
            p.next=temp
            temp.next=None

class LinkedList1:
    def __init__(self):
        self.head1=None

    def display(self):              
        if self.head1 is None:
            return "Head is Null.Insert First!"
        p=self.head1
        while p!=None:
            print(f"-->{p.data}",end='')
            p=p.next
    def insert_at_the_end(self,data):       
        temp=Node(data)
        if self.head1 is None:
            temp.next=None
            self.head1=temp
        else:
            p=self.head1
            while p.next!=None:
                p=p.next
            p.next=temp
            temp.next=None
    def create_list(self):          
        n=1
        while n!=0:
            data=int(input("Enter data:"))
            temp=Node(data)
            if self.head1 is None:
                temp.next=None
                self.head1=temp
            else:
                p=self.head1
                while p.next!=None:
                    p=p.next
                p.next=temp
            n=int(input("If you want to continue press 1 else 0:"))

def merge_ll(head1,head2):
    p=head1
    q=head2
    l1=LinkedList()
    while p!=None and q!=None:
        if p.data<=q.data:
            l1.insert_at_the_end(p.data)
            p=p.next
        elif p.data>q.data:
            l1.insert_at_the_end(q.data)
            q=q.next

    while p!=None:
        l1.insert_at_the_end(p.data)
        p=p.next
    while q!=None:
        l1.insert_at_the_end(q.data)
        q=q.next

    l1.display()

ll1=LinkedList()
ll2=LinkedList1()
ll1.create_list()
ll2.create_list()

merge_ll(ll1.head,ll2.head1)