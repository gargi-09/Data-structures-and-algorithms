#Single Linked List

class Node:
    def __init__(self,data=None,next=None,prev=None):
        self.data=data
        self.next=next
        self.prev=prev

class LinkedList:
    def __init__(self):
        self.head=None
    
    def __str__(self) -> str:
        if self.head==None:
            return f"Head is Null.Insert first!"
        return f"Head is {self.head.data}"
    
    def isNone(self):                   #Time complexity=O(1) and space complexity=O(1)
        if self.head==None:
            return True
        return False

    def display(self):                  #Time complexity=O() and space complexity=O()
        if self.isNone():
            return "Head is Null.Insert First!"
        p=self.head
        while p!=None:
            print(f"-->{p.data}",end='')
            p=p.next
        print()
        return

    def len_l(self):                    #Time complexity=O() and space complexity=O()
        if self.isNone():
            return "Head is Null.Insert First!"
        count=0
        p=self.head
        while p!=None:
            count+=1
            p=p.next
        return count

    def search(self,value=None,pos=None):       #Time complexity=O() and space complexity=O()
        if self.isNone():
            return "Head is Null.Insert First!"
        if value!=None:
            p=self.head
            i=0
            
            while p.data!=value and p.next!=None:
                p=p.next
                i+=1
            if p.data==value:
                return i
            else:
                return False
        
        elif pos!=None:
            p=self.head
            i=0

            while i!=pos and p.next!=None:
                p=p.next
                i+=1
            if i==pos:
                return p.data
            else:
                return False

    
    def create_list(self):          #Time complexity=O() and space complexity=O()
        n=1
        while n!=0:
            data=int(input("Enter data:"))
            temp=Node(data)
            if self.isNone():
                temp.next=None
                self.head=temp
            else:
                p=self.head
                while p.next!=None:
                    p=p.next
                p.next=temp
            n=int(input("If you want to continue press 1 else 0:"))
    
    def insert_at_the_beg(self,data):           #Time complexity=O() and space complexity=O()
        temp=Node(data)
        if self.isNone():
            temp.next=None
            self.head=temp
        else:
            temp.next=self.head
            self.head=temp

    def insert_in_the_middle(self,data,pos):        #Time complexity=O() and space complexity=O()
        temp=Node(data)
        if self.isNone():
            temp.next=None
            self.head=temp
        else:
            if pos==0:
                self.insert_at_the_beg(data)
            else:
                i=0
                p=self.head
                while True:
                    if i==pos-1:
                        break
                    p=p.next
                    i+=1
                q=p.next
                p.next=temp
                temp.next=q

    def insert_at_the_end(self,data):       #Time complexity=O() and space complexity=O()
        temp=Node(data)
        if self.isNone():
            temp.next=None
            self.head=temp
        else:
            p=self.head
            while p.next!=None:
                p=p.next
            p.next=temp
            temp.next=None
    

    def delete_at_the_beg(self):        #Time complexity=O() and space complexity=O()
        if self.isNone():
            return "Head is Null.Insert First!"
        
        self.head=self.head.next
    
    def delete_in_the_middle(self,pos):     #Time complexity=O() and space complexity=O()
        if self.isNone():
            return "Head is Null.Insert First!"
        if pos==0:
            self.delete_at_the_beg()
        else:
            p=self.head
            i=0
            while True:
                if i==pos-1:
                    break
                p=p.next
                i+=1
            p.next=p.next.next

    def delete_at_the_end(self):        #Time complexity=O() and space complexity=O()
        if self.isNone():
            return "Head is Null.Insert First!"
        p=self.head
        while p.next.next!=None:
            p=p.next
        p.next=None

    def update_by_value(self,ovalue,nvalue):        #Time complexity=O() and space complexity=O()
        if self.isNone():
            return "Head is Null.Insert First!"
        if type(self.search(ovalue))!=int:
            return f"{ovalue} is not in the list."
        p=self.head
        while p.data!=ovalue:
            p=p.next
        p.data=nvalue

    def update_by_pos(self,value,pos):      #Time complexity=O() and space complexity=O()
        if self.isNone():
            return "Head is Null.Insert First!"
        i=0
        p=self.head
        while i!=pos:
            p=p.next
            i+=1
        p.data=value




#Doubly Linked List

class DoublyLinkedList:
    def __init__(self):
        self.head=None

    def __str__(self) -> str:
        if self.head==None:
            return f"Head is Null.Insert first!"
        return f"Head is {self.head.data}"

    def isNone(self):       #Time complexity=O() and space complexity=O()
        if self.head==None:
            return True
        return False

    def len_l(self):        #Time complexity=O() and space complexity=O()
        if self.isNone():
            return "Head is empty.Insert first!"
        p=self.head
        count=0
        while p!=None:
            count+=1
            p=p.next
        return count

    def search(self,value=None,pos=None):       #Time complexity=O() and space complexity=O()
        if self.isNone():
            return "Head is Null.Insert First!"
        if value!=None:
            p=self.head
            i=0

            while p.data!=value and p.next!=None:
                p=p.next
                i+=1
            if p.data==value:
                return i
            else:
                return False
        
        elif pos!=None:
            p=self.head
            i=0

            while i!=pos and p.next!=None:
                p=p.next
                i+=1
            if i==pos:
                return p.data
            else:
                return False

    def display(self):      #Time complexity=O() and space complexity=O()
        if self.isNone():
            return "Head is Null.Insert First!"
        p=self.head
        while p!=None:
            print(f"-->{p.data}<--",end='')
            p=p.next
        print()

    def rev_display(self):          #Time complexity=O() and space complexity=O()
        if self.isNone():
            return "Head is Null.Insert First!"
        p=self.head
        while p.next!=None:
            p=p.next
        while p!=None:
            print(f"-->{p.data}",end='')
            p=p.prev
        print()

    def create_list(self):          #Time complexity=O() and space complexity=O()
        n=1
        while n!=0:
            data=int(input("Enter the data:"))
            temp=Node(data)
            if self.isNone():
                temp.next=None
                self.head=temp
            
            else:
                p=self.head
            
                while p.next!=None:
                    p=p.next
                temp.prev=p
                p.next=temp

            n=int(input("If you want to continue press 1 else 0:"))

    def insert_at_the_beg(self,data):           #Time complexity=O() and space complexity=O()
        temp=Node(data)
        if self.isNone():
            self.head=temp
        else:
            self.head.prev=temp
            temp.next=self.head
            self.head=temp

    def insert_in_the_middle(self,data,pos):            #Time complexity=O() and space complexity=O()
        temp=Node(data)
        if self.isNone():
            self.head=temp
        else:
            i=0
            p=self.head
            while True:
                if i==pos-1:
                    break
                p=p.next
                i+=1
            temp.next=p.next
            temp.prev=p
            p.next.prev=temp
            p.next=temp

    def insert_at_the_end(self,data):           #Time complexity=O() and space complexity=O()
        temp=Node(data)
        if self.isNone():
            self.head=temp
        else:
            p=self.head
            while p.next!=None:
                p=p.next
            temp.prev=p
            p.next=temp
        
    def delete_at_the_beg(self):            #Time complexity=O() and space complexity=O()
        if self.isNone():
            return "Head is Null.Insert First!"
        self.head.next.prev=None
        self.head=self.head.next

    def delete_in_the_middle(self,pos):     #Time complexity=O() and space complexity=O()
        if self.isNone():
            return "Head is Null.Insert First!"
        i=0
        p=self.head
        while True:
            if i==pos-1:
                break
            p=p.next
            i+=1
        p.next.next.prev=p
        p.next=p.next.next

    def delete_at_the_end(self):        #Time complexity=O() and space complexity=O()
        if self.isNone():
            return "Head is Null.Insert First!"
        p=self.head
        while p.next.next!=None:
            p=p.next
        p.next.prev=None
        p.next=None

    def update_by_value(self,ovalue,nvalue):        #Time complexity=O() and space complexity=O()
        if self.isNone():
            return "Head is Null.Insert First!"
        if type(self.search(ovalue))!=int:
            return f"{ovalue} is not in the list."
        p=self.head
        while p.data!=ovalue:
            p=p.next
        p.data=nvalue
        print(p.data)

    def update_by_pos(self,value,pos):          #Time complexity=O() and space complexity=O()
        if self.isNone():
            return "Head is Null.Insert First!"
        i=0
        p=self.head
        while i!=pos:
            p=p.next
            i+=1
        p.data=value
'''
l1=LinkedList()
print(l1)
print(l1.len_l())
l1.insert_at_the_beg(1)
#l1.create_list()
l1.insert_at_the_end(2)
l1.insert_at_the_end(3)
l1.insert_at_the_end(4)
l1.insert_in_the_middle(44,2)
l1.insert_at_the_end(20)
l1.display()
l1.delete_at_the_beg()
l1.display()
l1.delete_in_the_middle(1)
l1.display()
l1.delete_at_the_end()
l1.display()
print(l1.search(2))
l1.update_by_value(2,20)
l1.display()
l1.update_by_pos(2,2)
l1.display()
print(l1.search(4,10))
'''
dll=DoublyLinkedList()
#dll.create_list()
dll.insert_at_the_end(1)
dll.insert_at_the_end(2)
dll.insert_at_the_end(3)
dll.display()
dll.insert_at_the_beg(9)
dll.display()
dll.insert_in_the_middle(44,2)
dll.display()
#dll.delete_at_the_beg()
dll.delete_in_the_middle(2)
dll.display()
dll.delete_at_the_end()
dll.display()
print(dll.search(9))
print(dll.update_by_value(9,0))
dll.display()
dll.update_by_pos(9,2)
dll.display()
