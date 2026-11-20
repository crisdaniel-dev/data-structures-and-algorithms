from node import Node

class BinaryTree:
    
    def __init__(self):
        self.__root = None
        
    def set_root(self, data):
        if self.__root:
            return "Root is already exists"
        self.__root = Node(data)
