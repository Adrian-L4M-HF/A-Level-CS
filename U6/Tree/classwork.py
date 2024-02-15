class node:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right

class branch(node):
    def __init__(self, data, left, right):
        super().__init__(data, left, right)

class leaf(node):
    def __init__(self, data):
        super().__init__(data, None, None)

#    A (root)
#   / \
#  B   C
#     / \
#    D   E

E = leaf('E')
D = leaf('D')
C = branch('C', D, E)
B = leaf('B')
A = branch('A', B, C)

root = A

def preorder(root): # Q1
    response = []
    if root:
        response.append(root.data)
        response += preorder(root.left)
        response += preorder(root.right)
    return response

print(preorder(root))

def inorder(root): # Q2
    response = []
    if root:
        response = inorder(root.left)
        response.append(root.data)
        response += inorder(root.right)
    return response

print(inorder(root))

def postorder(root): # Q3
    response = []
    if root:
        response = postorder(root.left)
        response += postorder(root.right)
        response.append(root.data)
    return response

print(postorder(root))