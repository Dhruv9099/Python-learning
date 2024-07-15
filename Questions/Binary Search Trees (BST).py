"""A binary search tree is a binary tree in which each node has at most two children,
and for each node, the left subtree contains only nodes with keys less than the node's key,
and the right subtree contains only nodes with keys greater than the node's key.
"""
# Node class
class BSTNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        

# Insert a node
def insert(root, key):
    if root is None:
        return BSTNode(key)
    if key < root.key:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root

# Inorder traversal
def inorder(root):
    if root:
        inorder(root.left)
        print(root.key, end=" ")
        inorder(root.right)

# Usage
root = None
keys = [10, 5, 20, 3, 7, 15]
for key in keys:
    root = insert(root, key)
inorder(root)
