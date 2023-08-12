# Binary Tree Implementation

class Node:
    def __init__(self,val,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

def insert(root,val):
    if not root:
        root = Node(val)
        return root
    
    queue = [root]
    
    while queue:
        temp = queue.pop(0)
        if temp.left:
            queue.append(temp.left)
        else:
            temp.left = Node(val)
            break
        if temp.right:
            queue.append(temp.right)
        else:
            temp.right = Node(val)
            break
    
def inorder(root):
    if not root:
        return
    if root.left:
        inorder(root.left)
    
    print(root.val,end=" ")

    if root.right:
        inorder(root.right)

# root = Node(1)
# for ele in [2,3,4,5,6]:
#     insert(root,ele)
# inorder(root)
