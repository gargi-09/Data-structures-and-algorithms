#Circular Linked List

class Node:
    def __init__(self,data=None,next=None,prev=None):
        self.data=data
        self.next=next
        self.prev=prev

class SCircularLL:
    def __init__(self) -> None:
        self.head=None
        self.last=None
    def __str__(self) -> str:
        if self.head==None:
            return f"Head is Null.Insert first!\n"
        return f"Head node is {self.head.data}.\n"

    def isNone(self):
        if self.head==None:
            return True
        return False

    def search(self,val=None,pos=None):
        if self.isNone():
            return "Empty list."
        else:
            if val!=None:
                p=self.head
                index=0
                while p.data!=val:
                    index+=1
                    p=p.next
                    if index==self.len_l()-1:
                        break
                if p==self.last and p.data!=val:
                    return True
                return index
            elif pos!=None:
                if pos>=self.len_l() or pos<0:
                    return True
                p=self.head
                ind=0
                while ind!=pos:
                    ind+=1
                    p=p.next
                return p.data

    def len_l(self):
        count=0
        if self.isNone():
            return count
        p=self.head
        while p.next!=self.head:
            count+=1
            p=p.next
        count+=1
        return count

    def display(self):
        if self.isNone():
            print("Empty list.")
        else:
            p=self.head
            while True:
                print(f"--->{p.data}",end="")
                p=p.next
                if p==self.head:
                    print()
                    break
    def create_list(self):
        n=1
        while n!=0:
            if self.isNone():
                val=int(input("Enter a value:"))
                temp=Node(val)
                self.head=temp
                self.last=temp
                self.last.next=self.head
                
            else:
                val=int(input("Enter a value:"))
                temp=Node(val)
                temp.next=self.last.next
                self.last.next=temp
                self.last=temp
            n=int(input("If you want to continue enter 1 otherwise 0:"))

    def insert_at_the_beg(self):
        val=int(input("Enter a value:"))
        if self.isNone():
            temp=Node(val)
            self.head=temp
            self.last=temp
            temp.next=self.head
        else:
            temp=Node(val)
            temp.next=self.last.next
            self.head=temp
            self.last.next=temp          

    def insert_at_the_end(self):
        val=int(input("Enter a value:"))
        if self.isNone():
            temp=Node(val)
            self.head=temp
            self.last=temp
            temp.next=self.head
        else:
            temp=Node(val)
            temp.next=self.last.next
            self.last.next=temp
            self.last=temp

    def insert_in_the_middle(self):
        if self.isNone():
            val=int(input("Enter a value:"))
            temp=Node(val)
            self.head=temp
            self.last=temp
            temp.next=self.head
        else:
            i=int(input("Enter an index no.:"))
            if i==0:
                self.insert_at_the_beg()
            elif i==self.len_l()-1:
                self.insert_at_the_end()
            else:
                ind=0
                p=self.head
                while ind!=i-1:
                    p=p.next
                    ind+=1
                val=int(input("Enter a value:"))
                temp=Node(val)
                temp.next=p.next
                p.next=temp
    def delete_at_the_beg(self):
        if self.isNone():
            return "Empty list."
        if self.len_l()==1:
            self.head=None
            self.last=None
        else:
            self.head=self.head.next
            self.last.next=self.head

    def delete_at_the_end(self):
        if self.isNone():
            return "Empty list."
        if self.len_l()==1:
            self.head=None
            self.last=None
        else:
            p=self.head
            while p.next.next!=self.head:
                p=p.next
            p.next=self.last.next
            self.last=p

    def delete_in_the_middle(self):
        if self.isNone():
            return "Empty list."
        else:
            i=int(input("Enter an index value:"))
            if i==0:
                self.delete_at_the_beg()
            elif i==self.len_l()-1:
                self.delete_at_the_end()
            else:
                ind=0
                p=self.head
                while ind!=i-1:
                    p=p.next
                    ind+=1
                p.next=p.next.next
    def delete_mid_by_value(self):
        if self.isNone():
            return "Empty list."
        else:
            i=int(input("Enter the value:"))
            if i==self.head.data:
                self.delete_at_the_beg()
            elif i==self.last.data:
                self.delete_at_the_end()
            else:
                p=self.head
                while p.next.data!=i:
                    p=p.next
                p.next=p.next.next

    def update_by_val(self,oval,nval):
        if self.isNone():
            return "Empty list."
        if self.search(oval)==True:
            print("Value doesn't exist")
        else:
            p=self.head
            while p.data!=oval:
                p=p.next
            p.data=nval
            self.display()
    def update_by_pos(self,val,pos):
        if self.isNone():
            return "Empty list."
        if self.search(None,pos)==True:
            print("Position doesn't exist")
        else:
            ind=0
            p=self.head
            while ind!=pos:
                p=p.next
                ind+=1
            p.data=val
            self.display()


Circle=SCircularLL()
Circle.create_list()
print(Circle.len_l())
print(Circle.search(3))
print(Circle.search(None,2))
Circle.update_by_val(3,0)
Circle.update_by_pos(3,2)
"""
Circle.display()
Circle.delete_at_the_beg()
Circle.display()
Circle.delete_at_the_end()
Circle.display()
Circle.delete_in_the_middle()
Circle.display()
Circle.delete_mid_by_value()
Circle.display()
print(Circle.len_l())
print(Circle.last.data)

Circle.insert_at_the_beg()
Circle.insert_at_the_end()
Circle.insert_in_the_middle()
Circle.display()
Circle.delete_at_the_beg()
Circle.display()
print(Circle)
"""