class node:
    def __init__(self, data : any, left : node, right : node):
        self.data = data
        self.left = left
        self.right = right

class leaf(node):
    def __init__(self, data : any, left : None, right : None):
        self.data = data
        self.left = None
        self.right = None


class branch(node):
    def __init__(self, data : any, left : node, right : node):
        self.data = data
        self.left = left
        self.right = right

class tree:
    def __init__(self, root):
        self.root = root

    def pre_order():
        pass

    def in_order():
        pass

    def post_order():
        pass
