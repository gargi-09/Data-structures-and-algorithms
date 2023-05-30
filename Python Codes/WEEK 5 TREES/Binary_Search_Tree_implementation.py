class BST:

    def __init__(self, data=None):
        self.data = data
        self.left = self.right = None

    def insert(self, data):
        if self.data == data:
            return

        if data < self.data:
            if self.left:
                self.left.insert(data)
            else:
                self.left = BST(data)

        elif data > self.data:
            if self.right:
                self.right.insert(data)
            else:
                self.right = BST(data)

    def build_tree(self, elements):

        for i in range(len(elements)):
            self.insert(elements[i])

    def search(self, data):
        if self.data == data:
            return True

        if data < self.data:
            if self.left:
                return self.left.search(data)
            else:
                return False
        elif data > self.data:
            if self.right:
                return self.right.search(data)
            else:
                return False

    def delete_deepest(self, d_node):

        q = []
        q.append(self)

        while len(q):

            temp = q.pop(0)

            if temp is d_node:
                temp = None
                return
            if temp.right:
                if temp.right is d_node:
                    temp.right = None
                    return
                else:
                    q.append(temp.right)
            if temp.left:
                if temp.left is d_node:
                    temp.left = None
                    return
                else:
                    q.append(temp.right)

    def delete_min(self):

        current = self

        while current.left is not None:
            current = current.left
        return current
    
    def delete(self,key):

        if not self:
            return self
        
        if key<self.data:
            self.left = self.left.delete(key)
        elif key>self.data:
            self.right = self.right.delete(key)

        else:

            if self.left is None:
                temp = self.right
                self = None
                return temp
            elif self.right is None:
                temp = self.left
                self = None
                return temp
            
            temp = self.right.delete_min()
            self.data = temp.data
            self.right = self.right.delete(temp.data)
        return self

    def print_root(self):
        if not self:
            return
        print(self.data)

    def preorder_traversal(self):

        print(self.data, end=" ")

        if self.left:
            self.left.preorder_traversal()
        if self.right:
            self.right.preorder_traversal()

    def inorder_traversal(self):

        if self.left:
            self.left.inorder_traversal()

        print(self.data, end=" ")

        if self.right:
            self.right.inorder_traversal()

    def postorder_traversal(self):

        if self.left:
            self.left.postorder_traversal()

        if self.right:
            self.right.postorder_traversal()

        print(self.data, end=" ")

    def print_tree(self):

        if self.left:
            self.left.print_tree()

        print(self.data, end=" ")

        if self.right:
            self.right.print_tree()


tree = BST(0)
tree.build_tree([-3, -4, -2, 2, 3, 1])
tree.print_tree()
print()
#tree.delete(-4)
tree.delete(0)
tree.print_tree()
print()
tree.print_root()

# print(tree.search(3))
# print(tree.search(10))
# tree.preorder_traversal()
# print()
# tree.inorder_traversal()
# print()
# tree.postorder_traversal()
# print()
