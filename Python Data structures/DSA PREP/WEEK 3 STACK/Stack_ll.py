#Stack implementation using linked list

class Node:
    def __init__(self,data=None,next=None,prev=None):
        self.data=data
        self.next=next
        self.prev=prev
    
class StackLL:
    def __init__(self):
        self.head=None
        self.top=None

    def __str__(self):
        if self.head is None:
            return "Stack underflow.Insert first!"
        return f"TOP:{self.top}.\nHEAD:{self.head}"

    def push(self):
        data=int(input("Enter a value:"))
        if self.head is None:
            temp=Node(data)
            self.head=temp
            self.top=temp
        
        else:
            temp=Node(data)
            self.top.next=temp
            self.top=temp

    def pop(self):
        if self.head is None:
            print("Stack underflow.Insert first!")
            return
        
        p=self.head
        while p.next.next:
            p=p.next
        p.next=None
        self.top=p
    
    def update(self,data):
        pass

    def display(self):
        if self.head is None:
            print("Stack underflow.Insert first!")
            return
        
        p=self.head
        while p.next:
            print(f"{p.data}")
            p=p.next
        print(f"{self.top.data}<--TOP")

stackll=StackLL()
stackll.push()
stackll.push()
stackll.push()
stackll.push()
stackll.display()
stackll.pop()
stackll.pop()
stackll.display()