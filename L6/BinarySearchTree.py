"""Binary Search Tree"""
#######################################################################
"""I need a tree to "Search" so I found one on the internet""" 
# Copied from https://www.pythonforbeginners.com/data-structures/binary-search-tree-in-python

class BinaryTreeNode:
  def __init__(self, data):
    self.data = data
    self.leftChild = None
    self.rightChild=None

def insert(root, newValue):
    # if binary search tree is empty, create a new node and declare it as root
    if root is None:
        root = BinaryTreeNode(newValue)
        return root
    # if newValue is less than value of data in root, add it to left subtree and proceed recursively
    if newValue < root.data:
        root.leftChild = insert(root.leftChild, newValue)
    else:
        # if newValue is greater than value of data in root, add it to right subtree and proceed recursively
        root.rightChild = insert(root.rightChild, newValue)
    return root

#########################################################################
# My own code starts here

def binarySearchTree(itemSought, currentNode):
       """half of the tree or subtree is eliminated each time its root is examined"""
       print(type(itemSought))
       print(type(currentNode))
       if currentNode == None: 
           return False
       elif itemSought == currentNode:
           return True
       elif itemSought < currentNode:
           if root.leftChild:
               return binarySearchTree(itemSought, root.leftChild)
           else:
               return False
       elif itemSought > currentNode:
           if root.rightChild:
               return binarySearchTree(itemSought, root.rightChild)
           else:
               return False
 
"""Tree data according to textbook page 238"""
root = insert(None,50)
sorted_nums = [27,62,12,9,14,35,28,41,59,71,68,60,52]
for index in sorted_nums:
    insert(root, index)


#Tests
print(binarySearchTree(50,None))
print(binarySearchTree(50,50))
"""These two works well"""

print(binarySearchTree(52,50))
print(binarySearchTree(27, 71))
"""
The "currentNode" is both an "int" type and a "BinaryTreeNode" 
class object type, I don't know how to fix it. Is it related to
the recursion on line 38 and 43?
"""

