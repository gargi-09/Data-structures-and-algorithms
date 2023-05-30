# Implementing Binary Search Tree

class BinaryTreeNode:

    def __init__(self, data):
        self.data = data
        self.left = self.right = None

    def insert(self,data):
        if not self:
            
            return
        q = []
        q.append(self)

        while len(q):
            temp = q.pop(0)
            if not temp.left:
                temp.left = BinaryTreeNode(data)
                break
            else:
                q.append(temp.left)
            
            if not temp.right:
                temp.right = BinaryTreeNode(data)
                break
            else:
                q.append(temp.right)
    
    def delete_deepest(self,d_node):
        q = []
        q.append(self)

        while len(q):
            temp = q.pop(0)

            if temp is d_node:
                temp = None
                return
            if temp.right:
                if temp.right == d_node:
                    temp.right = None
                    return
                else:
                    q.append(temp.right)
            if temp.left:
                if temp.left == d_node:
                    temp.left = None
                    return
                else:
                    q.append(temp.left)
    

    def delete(self,data):
        if not self:
            return
        if not self.left and not self.right:
            if self.data == data:
                return None
        
        key_node = None
        q = []
        q.append(self)
        temp = None

        while len(q):
            temp = q.pop(0)

            if temp.data == data:
                key_node = temp
            if temp.left:
                q.append(temp.left)
            if temp.right:
                q.append(temp.right)
        
        if key_node:
            x = temp.data
            self.delete_deepest(temp)
            key_node.data = x

    def search(self,data):
        if not self:
            return False
        
        q = []
        q.append(self)

        while len(q):
            temp = q.pop(0)
            if temp.data == data:
                return True
            if temp.left:
                q.append(temp.left)
            if temp.right:
                q.append(temp.right)
        return False

        

    def height(self,left_h = 0, right_h = 0):
        if not self:
            return 0
        if self.left:
            left_h = self.left.height()
        if self.right:
            right_h = self.right.height()

        return max(left_h,right_h)+1

    def print_level_order(self):
        h = self.height()

        for i in range(1,h+1):
            self.print_current_level(i)
    
    def print_current_level(self,level):
        if self is None:
            return
        if level == 1:
            print(self.data,end = " ")
        elif level>1:
            if self.left:
                self.left.print_current_level(level-1)
            if self.right:
                self.right.print_current_level(level-1)

    def build_tree(self,elements):
        pass

    def print_tree(self):
        if not self:
            return None
        
        if self.left:
            self.left.print_tree()
        
        print(self.data,end=" ")

        if self.right:
            self.right.print_tree()

