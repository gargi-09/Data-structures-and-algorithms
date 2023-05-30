#Finding max height

import Binary_Search_Tree_implementation as bst

def max_depth(root):

    if root is None:
        return -1
    
    l_depth = max_depth(root.left)
    r_depth = max_depth(root.right)

    if l_depth>r_depth:
        return l_depth+1
    elif l_depth <= r_depth:
        return r_depth+1

root = bst.build_tree([1,2,3,4,5])

root.inorder_traversal()
print()
print(max_depth(root))

