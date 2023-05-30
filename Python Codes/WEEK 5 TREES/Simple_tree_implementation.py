#Simple Tree implementation

class TreeNode:

    def __init__(self,data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        p  = self.parent
        while p:
            level+=1
            p = p.parent
        return level
        
    def print_tree(self):
        space = " "*(self.get_level()+3)
        prefix = space + "-->" if self.parent else ""
        print(prefix+str(self.data))
        if len(self.children) > 0:
            for child in self.children:
                child.print_tree()

def build_tree():
    root = TreeNode('Electronics')

    laptop = TreeNode('laptop')
    mac = TreeNode('Macbook')
    dell = TreeNode('Dell')
    laptop.add_child(mac)
    laptop.add_child(dell)

    cell_phones = TreeNode('cell phones')
    iphone = TreeNode('IPhone')
    google = TreeNode('Google pixel')
    cell_phones.add_child(iphone)
    cell_phones.add_child(google)

    tv = TreeNode('TV')
    samsung = TreeNode('samsung')
    sony = TreeNode('Sony')
    tv.add_child(samsung)
    tv.add_child(sony)

    root.add_child(laptop)
    root.add_child(cell_phones)
    root.add_child(tv)
    return root

root = build_tree()
root.print_tree()
