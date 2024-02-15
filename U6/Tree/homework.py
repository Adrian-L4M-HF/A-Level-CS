class node:
    def __init__(self, data, right = None, left = None):
        self.data = data
        self.left = left
        self.right = right

def insert(data, root): # Q1
    if root is None:
        return node(data)
    else:
        if root.data == data:
            return root
        elif root.data > data:
            root.left = insert(data, root.left)
        else:
            root.right = insert(data, root.right)
    return root

def search(data, root): #Q2
    if root is None or root.data == data:
        return root
    if root.data > data:
        return serach(data, root.left)
    return search(data, root.right)

"""
Time Complexity
The worst case is a skewed tree, the aglorithm has to traval from the root to the deepest leaf node.
The height of a worse case skewed tree is n, so the time complexity is O(n).
"""