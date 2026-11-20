from node import Node

class PriorityQueue:
    
    def __init__(self):
        self.__front = None
        
    def enqueue(self, priority, data):
        node = Node(priority, data)
        if not self.__front:
            self.__front = node
        elif priority < self.__front.priority:
            node.next = self.__front
            self.__front = node
        else:
            current = self.__front
            while current.next is not None and current.next.priority <= priority:
                current = current.next
            node.next = current.next
            current.next = node
            
    def dequeue(self):
        if not self.__front:
            return None
        front = self.__front.data
        self.__front = self.__front.next
        return front
    
    def peek_data(self):
        if not self.__front:
            return None
        return self.__front.data
    
    def peek_priority(self):
        if not self.__front:
            return None
        return self.__front.priority
    
    def is_empty(self):
        if self.__front:
            return False
        else:
            return True
        
    def clear(self):
        self.__front = None
        
    def count(self):
        count = 0
        current = self.__front
        while current:
            count += 1
            current = current.next
        return count
    
    def display_priority(self):
        if not self.__front:
            return None
        current = self.__front
        output = ""
        while current:
            output += f"[Priority number: {current.priority}]\n"
            current = current.next
        return output.strip()
    
    def display_data(self):
        if not self.__front:
            return None
        current = self.__front
        output = ""
        while current:
            output += f"Data: {current.data}\n"
            current = current.next
        return output.strip()
    
    def display_all(self):
        if not self.__front:
            return None
        current = self.__front
        output = ""
        while current:
            output += f"[Priority: {current.priority}, Data: {current.data}]\n"
            current = current.next
        return output.strip()