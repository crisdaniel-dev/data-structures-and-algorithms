from node import Node

class BinaryTree:
    
    def __init__(self):
        self.__root = None
        
    def set_root(self, data):
        if self.__root:
            return "Root alrady exists"
        self.__root = Node(data)
        
    def get_root(self):
        return self.__root
    
    def insert_left(self, parent, data):
        if parent.left:
            return "Left child already exists"
        parent.left = Node(data)
        
    def insert_right(self, parent, data):
        if parent.right:
            return "Right child already exists"
        parent.right = Node(data)
        
    def is_empty(self):
        if self.__root:
            return False
        else:
            return True
        
    def count(self):
        def total(node):
            if not node:
                return 0
            return 1 + total(node.left) + total(node.right)
        return total(self.__root)
    
    def count_leaves(self):
        def leaves(node):
            if not node:
                return 0
            if not node.left and not node.right:
                return 1
            return leaves(node.left) + leaves(node.right)
        return leaves(self.__root)
