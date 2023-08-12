# Print leaf nodes of a binary tree

import binary_tree as bt

def print_leaf_nodes(root):
    if not root:
        return
    if not root.left and not root.right:
        print(root.val,end=" ")
        return
    if root.left:
        print_leaf_nodes(root.left)
    if root.right:
        print_leaf_nodes(root.right)

root = bt.Node(10)
for ele in [2,30,4,50,6]:
    bt.insert(root,ele)
bt.inorder(root)
print()
print_leaf_nodes(root)