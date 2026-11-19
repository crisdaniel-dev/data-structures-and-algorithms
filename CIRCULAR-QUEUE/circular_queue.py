from node import Node

class CircularQueue:
    
    def __init__(self):
        self.__front = self.__rear = None
        
    def enqueue(self, data):
        node = Node(data)
        if not self.__front:
            self.__front = self.__rear = node
            self.__rear.next = self.__front
            
    def dequeue(self):
        assert self.__front, "Queue is empty"
        front = self.__front.data
        if self.__front is self.__rear:
            self.__front = self.__rear = None
        else:
            self.__front = self.__front.next
            self.__rear.next = self.__front
        return front
            
    def peek(self):
        assert self.__front, "Queue is empty"
        return self.__front.data
    
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
        while True:
            output += str(current.data) + " "
            current = current.next
            if current is self.__front:
                break
        return output.strip()