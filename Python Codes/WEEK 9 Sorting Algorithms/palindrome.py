class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    def insert_at_the_beg(self,val):
        node = Node(val)
        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head = node
            
    def display(self):
        n = self.head 
        while n != None:
            print(n.value,end = "->")
            n = n.next
        print("None")

            

    def insert_at_end(self,val):
        node = Node(val)
        if self.head == None:
            self.head = node
        else:
            
            n = self.head
            while n.next != None:
                n = n.next

            n.next = node
        

    def delete_at_the_beg(self):
        n = self.head
        if self == None:
            return -1
        else :
            self.head = n.next
            del n

    
    # def delete_at_the_end(self):                 # Do i need this inspite of delete_at()
    #     n  = self.head

    #     if self == None:
    #         return -1
    #     else:
    #         p = self.head
    #         while p.next.next  :
    #             p = p.next 
    #         del p.next
    #         p.next = None

    def delete_by_value(self,v):
        n = self.head
        if self == None:
            return 
        elif v == n.value:
            self.head = n.next
            del n 
            return 
        try:
            while n.next.value != v :
                n = n.next
            dval = Node(n.next)
            n.next = n.next.next
            del dval
        except:
            return False
            
    def count_nodes(self):
      count =0 
      n = self.head
      while n != None:
         n = n.next
         count+=1
      return count

    
    def delete_at(self, pos = None ):
         count = self.count_nodes()
         n = self.head
         
         if pos is None:
            pos = count

         elif pos < 0:
            pos = count + pos +1

         elif pos ==0:
            self.head = n.next
            del n 

         if self == None  or abs(pos) > count:
            print("Invalid position!")
            return 

         elif pos == 1:
            self.head = n.next
            del n
            return


         p = 1
         while n and p < pos-1:
            n = n.next
            p+=1

         dval = n.next
         n.next = n.next.next
         del dval
         return

new = LinkedList()
l = [1,2,2,1]

for i in l:
    new.insert_at_the_beg(i)


new.display()

 
def isPalindrome(head) :
        curr = head
        prev = None
        nex = None
        while curr.next:
    
            nex = curr.next
            curr.next = prev
            prev = curr
            curr = nex
        curr = head
        while prev and curr:
            if prev.value != curr.value:
                return False
            prev = prev.next
            curr = curr.next
        return True
print(isPalindrome(new.head))



