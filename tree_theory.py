class Node:
    
    def __init__(self, key):
        self.value = key
        self.left = None
        self.right = None

root = Node('A')
root.left = Node('B')
root.left.left = Node('D')
root.right = Node('C')

#print(root.value)
#print(root.right.value)

def insert(root, new_node):  #binary search tree
    if root is None:
        root = new_node
    else:
        if root.value < new_node.value:
            if root.right is None:
                root.right = new_node
            else:
                insert(root.right, new_node)
        else:
            if root.left is None:
                root.left = new_node
            else:
                insert(root.left, new_node)

def inorder(root):
    if root:
        inorder(root.left)
        print(root.value)
        inorder(root.right)
    else:
        None

r = Node(41)
insert(r, Node(45))
insert(r, Node(99))
insert(r, Node(56))
insert(r, Node(44))
insert(r, Node(23))
insert(r, Node(89))
insert(r, Node(67))
insert(r, Node(11))

inorder(r)
