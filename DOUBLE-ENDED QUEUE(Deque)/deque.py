from node import Node

class Deque:
    
    def __init__(self):
        self.__front = self.__rear = None
        
    def add_front(self, data):
        node = Node(data)
        if not self.__front:
            self.__front = self.__rear = node
        else:
            node.next = self.__front
            self.__front.prev = node
            self.__front = node
            
    def add_rear(self, data):
        node = Node(data)
        if not self.__front:
            self.__front = self.__rear = node
        else:
            node.prev = self.__rear
            self.__rear.next = node
            self.__rear = node
            
    def remove_front(self):
        assert self.__front, "Queue is empty"
        front = self.__front.data
        if self.__front is self.__rear:
            self.__front = self.__rear = None
        else:
            self.__front = self.__front.next
            self.__front.prev = None
        return front
            
    def remove_rear(self):
        assert self.__rear, "Queue is empty"
        rear = self.__rear.data
        if self.__front is self.__rear:
            self.__front = self.__rear = None
        else:
            self.__rear = self.__rear.prev
            self.__rear.next = None
        return rear
        
    def peek_front(self):
        assert self.__front, "Queue is empty"
        return self.__front.data
    
    def peek_rear(self):
        assert self.__rear, "Queue is empty"
        return self.__rear.data
    
    def is_empty(self):
        if self.__front:
            return False
        else:
            return True
        
    def clear(self):
        self.__front = self.__rear = None
        
    def display(self):
        assert self.__front, "Queue is empty"
        current = self.__front
        output = ""
        while current:
            output += str(current.data) + " "
            current = current.next
        return output.strip()