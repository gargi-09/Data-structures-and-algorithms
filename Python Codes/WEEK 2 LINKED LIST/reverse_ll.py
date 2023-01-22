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
    
    def len_l(self):                    
        if self.head is None:
            return "Head is Null.Insert First!"
        count=0
        p=self.head
        while p!=None:
            count+=1
            p=p.next
        return count

    def reverse(self):
        prev=next=None
        curr=self.head
        while curr is not None:
            next=curr.next
            curr.next=prev
            prev=curr
            curr=next
        self.head=prev

l=LinkedList()
l.insert_at_the_end(1)
l.insert_at_the_end(2)
l.insert_at_the_end(9)
l.display()
print(l.len_l())
l.reverse()
l.display()