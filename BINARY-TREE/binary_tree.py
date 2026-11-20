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
